import psycopg2
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.cm as cm
from matplotlib.lines import Line2D
import random

x_values = np.logspace(np.log10(20), np.log10(20000), num=5000)

cool_colors = ['teal', 'darkcyan', 'cadetblue', 'steelblue', 'dodgerblue', 'royalblue', 'slateblue', 'darkorchid', 'darkmagenta']

warm_colors = ['orangered', 'darkorange', 'orange', 'crimson']

conn = psycopg2.connect(
    host="localhost",
    database="IEM",
    port="5432",
    user="postgres",
    password="root"
)

# A function to find the mean of a dataset in a given range
def find_mean_in_range(data, x_min, x_max):
    indices = (x_values >= x_min) & (x_values <= x_max)
    return np.mean(data[indices])

# A function to apply a moving average filter to a dataset
# This is used to smooth out the data
def moving_average(data, window_size=3):
    window = np.ones(window_size) / window_size
    return np.convolve(data, window, mode='same')

# A function to read in a dataframe and interpolate it to the x_values
# This is done so that the plots have the same x-values
# also, the data is shifted so that the average in the range of 50-70 dB is 60 dB
def read_and_interpolate(df, x_values):
    if df.empty:
        return np.zeros_like(x_values)

    min_x = df['x'].min()
    max_x = df['x'].max()
    x_values_interp = x_values[(x_values >= min_x) & (x_values <= max_x)]

    f = interp1d(df['x'], pd.to_numeric(df['y'], errors='coerce'), kind='linear', fill_value='extrapolate')

    y_values = np.empty_like(x_values)
    y_values[:] = np.nan
    y_values[(x_values >= min_x) & (x_values <= max_x)] = f(x_values_interp)

    # Calculate the mean in the dB range of 50-70
    avg_in_range = find_mean_in_range(y_values, 40, 10000)

    # If the average is valid, subtract it from 60 to find the shift value
    if np.isfinite(avg_in_range):
        shift = 60 - avg_in_range
    else:
        shift = 0

    # Apply the shift to all y-values
    y_values += shift

    return y_values

# A function to plot the preference curve for an IEM
# The plot includes the following:
#   - The average of all measurements
#   - The target curve
#   - The individual measurements
def plot_preference(iem):

    cur = conn.cursor()

    # add error handling if input is empty
    if iem == '':
        # do nothing
        return
    # else if in case nothing is plotted
    elif iem == 'None':
        # do nothing
        return

    # Query for the IEM (case-insensitive)
    sql_iem = "SELECT x, y FROM avg_measurement_data WHERE LOWER(IEM_name) = LOWER(%s)"
    sql_target = "SELECT x, y FROM target"
    sql_measurements = "SELECT measurement_num, x, y FROM measurement_data WHERE LOWER(iem_name) = LOWER(%s)"

    # Create a dataframe for the IEM
    cur.execute(sql_iem, (iem,))
    rows = cur.fetchall()
    df_iem = pd.DataFrame(rows, columns=['x', 'y'])

    # Create a dataframe for the target
    cur.execute(sql_target)
    rows = cur.fetchall()
    df_target = pd.DataFrame(rows, columns=['x', 'y'])

    # Create a dataframe for the measurements
    cur.execute(sql_measurements, (iem,))
    rows = cur.fetchall()
    df_measurements = pd.DataFrame(rows, columns=['measurement_num', 'x', 'y'])

    x_values = np.logspace(np.log10(20), np.log10(20000), num=5000)

    input_data = read_and_interpolate(df_iem, x_values)
    target_data = read_and_interpolate(df_target, x_values)

    # Create a color map for the measurements
    # colors = cm.gray(np.linspace(0.1, 1, len(df_measurements['measurement_num'].unique())))

    plt.figure(figsize=(20, 10))

    plt.ylim(30, 85)
    plt.xlim(20, 20000)

    # Plot each measurement
    for i, measurement_num in enumerate(df_measurements['measurement_num'].unique()):
        df_measurement = df_measurements[df_measurements['measurement_num'] == measurement_num]
        measurement_data = read_and_interpolate(df_measurement, x_values)
        plt.plot(x_values, measurement_data, color='gray', linewidth=1.5, alpha=0.1)

        # plt.plot(x_values, measurement_data, color=colors[i], linewidth=1)

    # Plot target data (dotted line)
    plt.plot(x_values, target_data, color='gray', linestyle='--', linewidth=2, label='Target')

    colors = cool_colors + warm_colors

    # Plot input data (colored line) using a random color
    color = random.choice(colors)
    plt.plot(x_values, input_data, color=color, linewidth=3, label=f'{iem}')

    # plt.plot(x_values, input_data, color='red', linewidth=3, label='Input')

    # Color the areas where the input plot deviates from the target plot
    plt.fill_between(x_values, input_data, target_data, where=(input_data > target_data), facecolor=color, alpha=0.25)
    plt.fill_between(x_values, input_data, target_data, where=(input_data < target_data), facecolor=color, alpha=0.25)

    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('dB')

    # Customize X-axis
    x_ticks = np.array([
        20, 30, 40, 50, 60, 80, 100, 150,
        200, 300, 400, 500, 600, 800,
        1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000,
        10000, 15000, 20000
    ])

    labels = [
        f'{int(x)}Hz' if x == 20
        else f'{int(x)}' if x < 1000
        else f'{x/1000:.1f}k' if x == 1500
        else f'{x//1000:.0f}k' if x != 20000
        else '20kHz' for x in x_ticks
    ]

    plt.xticks(x_ticks, labels=labels, fontsize=12)
    plt.yticks(np.arange(30, 85, 5))

    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    # Create custom legend
    custom_lines = [
        Line2D([0], [0], color='gray', lw=2, linestyle='--'),
        Line2D([0], [0], color=color, lw=3),
        Line2D([0], [0], color='gray', lw=1.5, alpha=0.5)
    ]

    plt.legend(custom_lines, ['Target', f'{iem}', 'Individual Measurements'], loc='upper right', fontsize=12)
    # plt.show()
    plt.savefig(f'website/static/{iem}.png')
    # Close the cursor
    #cur.close()

# A function 'compare_iems' that takes two IEM names as arguments and plots the frequency response of both IEMs on the same plot
def compare_iems(iem1, iem2):

    cur = conn.cursor()

    # Query for the IEM (case-insensitive)
    sql_iem = "SELECT x, y FROM avg_measurement_data WHERE LOWER(IEM_name) = LOWER(%s)"
    sql_target = "SELECT x, y FROM target"

    # Create a dataframe for the target
    cur.execute(sql_target)
    rows = cur.fetchall()
    df_target = pd.DataFrame(rows, columns=['x', 'y'])

    # Create a dataframe for the IEM
    cur.execute(sql_iem, (iem1,))
    rows = cur.fetchall()
    df_iem1 = pd.DataFrame(rows, columns=['x', 'y'])

    # Create a dataframe for the IEM
    cur.execute(sql_iem, (iem2,))
    rows = cur.fetchall()
    df_iem2 = pd.DataFrame(rows, columns=['x', 'y'])

    x_values = np.logspace(np.log10(20), np.log10(20000), num=5000)

    input_data1 = read_and_interpolate(df_iem1, x_values)
    input_data2 = read_and_interpolate(df_iem2, x_values)
    target_data = read_and_interpolate(df_target, x_values)

    plt.figure(figsize=(20, 10))

    plt.ylim(30, 85)
    plt.xlim(20, 20000)

    # Plot target data (dotted line)
    plt.plot(x_values, target_data, color='gray', linestyle='--', linewidth=2, label='Target')

    cool_colors = ['teal', 'darkcyan', 'cadetblue', 'steelblue', 'dodgerblue', 'royalblue', 'slateblue', 'darkorchid', 'darkmagenta']

    warm_colors = ['orangered', 'darkorange', 'orange', 'crimson']

    # Plot input data (colored line)
    plt.plot(x_values, input_data1, color=random.choice(warm_colors), linewidth=3, label=f'{iem1}')
    plt.plot(x_values, input_data2, color=random.choice(cool_colors), linewidth=3, label=f'{iem2}')

    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('dB')

    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('dB')

    # Customize X-axis
    x_ticks = np.array([
        20, 30, 40, 50, 60, 80, 100, 150,
        200, 300, 400, 500, 600, 800,
        1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000,
        10000, 15000, 20000
    ])

    labels = [
        f'{int(x)}Hz' if x == 20
        else f'{int(x)}' if x < 1000
        else f'{x/1000:.1f}k' if x == 1500
        else f'{x//1000:.0f}k' if x != 20000
        else '20kHz' for x in x_ticks
    ]

    plt.xticks(x_ticks, labels=labels, fontsize=12)
    plt.yticks(np.arange(30, 85, 5))

    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    plt.legend(loc='upper right', fontsize=12)
    plt.savefig(f'website/static/{iem1}_{iem2}.png')
    #plt.show()
