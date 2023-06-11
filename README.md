# IEM Database Prototype

## Introduction

### About the project
This webapp is a prototype for *potentially* the largest publically availible database of in ear monitor, IEM, measurements. The goal is to create a platform from which a user can view the average measurement of a given IEM, as well as to see the average predicted preference percentage of said IEM. Which can be used as a rough metric to guage how well a user may enjoy said IEM. Additionally, a user may also compare the measurements of two IEMs, and see the difference between the two. This can be used to see how similar two IEMs are, and how much they differ in sound. To visualize the IEM measurements, frequency response plots are created, so that the user can see the measurements in a more intuitive way.

To achieve this, a pipeline is created with the following steps:

1. Scraping the IEM measurements and coverting to .csv files with only X and Y columns.
2. Grouping the .csv files so that all the measurements for a given IEM are grouped together. In order to achieve this, a manually labeled list of IEM's and their respective name variations is used.
3. Calculating the average measurements, saving them as new .csv files and adding them to a dataframe.
4. Calculating the predicted preference percentage for a given target. 
5. Plotting the top 10 IEM's according to their average predicted preference percentage.

It is worth noting that the aforementioned pipeline for data scraping and calculating average predicted preference percentage was created before the database project was assigned, and it was modified to create .csv files which are ingested into PostgreSQL to create the database which is used for the webapp. Lastly, we feel that it is worth noting the scale of the data which has been collected and used for this project, and the difficulty which was introduced as a result. The data consists of 1400+ unique IEM models, ~12000 Frequency response measurements and 6M+ individual datapoints, excluding those calculated for the average measurements.

The difficulty introduced was as a result of the very nature of this project which was that, naturally every reviewer has their own testing methodologies and naming conventions, hence then need for an average. This lack of a consistent naming convetion meant that there was no way to automatically group the measurements for a given IEM together. This meant that a manually labeled list of IEM's and their respective name variations had to be created. This list consists of 1400+ IEMs and their respective name variations, and was created by manually going through the measurements and grouping them together. This was a very time consuming process, and was the most time consuming part of the project. However, it was necessary to create a consistent naming convention, and to group the measurements together. The list is not perfect, and there are still some IEM's which are not grouped together, however, our aim is to improve the list over time, and to make it as complete as possible.

### E/R Diagram

### Features
The webapp allows for the following functionality:
1. Create a new user account.
2. Login to an existing user account.
3. Delete an existing user account.
4. Update an existing user's password.
5. Searching for an IEM by name.
6. Viewing the average measurement and indivdual measurements of an IEM compared to the chosen target.
7. Viewing the average predicted preference percentage as well as other metrics such as: average error, STDEV, Variance etc. of an IEM compared to the chosen target.
8. Comparing the measurements of two IEMs.
9. Viewing the reviewers who created the measurements used for the given IEM or comparison.

### Credits
The webapp was created by the following students: <br />
Victor Villumsen Bergien | TCG780 | tcg780@alumni.ku.dk | Group 22 <br />
Mateo Anusic | DJZ709 | djz709@alumni.ku.dk | Group 23 <br />
Emil Thorlund | GPV679 | gpv679@alumni.ku.dk | Group 22 <br />
Lucas A. Rosing | QGC922 | qgc922@alumni.ku.dk | Group 23

### Acknowledgements & Data Sources
The data used to create this database has been mainly sourced from squig.link, a website used by reviewers to
host their IEM frequency response measurements. The following reviewers squig.links have been used to scrape data:

- Acho Reviews
- Aftersound
- Animagus
- ankramutt
- Audio Review News
- Bedrock Reviews
- Bry Audio Reviews
- CammyFi
- Elise Audio
- EPLV
- Gizaudio
- Harpo
- Hawaii Bad Boy
- Hi End Portable
- Hobby Talk
- ianfann
- IEM World
- Jacstone
- kr0mka
- Kurin
- Melatonin
- nymz
- Paul Wasabi
- Recode
- Rikuduo Goku
- Shortbus
- Side Salad Audio
- Super* Review
- tgx78
- Vortex Reviews
- VSG
- wdym
- Akros
- freeryder05
- Precogvision

This is made possible as each reviewers squig.link site, hosts their IEM frequency response measurements at
<reviewer's name>.squig.link/data, from which it is possible to scrape and download the raw frequency response measurements.

Please note that the only data that was scraped from these sites are the frequency response measurements, and naturally, the names of the IEM's themselves. Though the database only includes entries for IEM's whose measurements are publically avalible, as it is seen as the most important datapoint per IEM.

## Usage

### How to Compile

Before running the application, the database must be set up as follows:

1. Uncompress `avg_measurement_data.7z` and `measurement_data.7z` and place the resulting `avg_measurement_data.csv` and `measurement_data.csv` files into the `website/data/csv` directory alongside the other .csv files. These files contain necessary data to populate the database.

2. Run `schema_IEM.sql`. This file is used to set up the database schema. In this script, ensure that the correct file paths to the corresponding .csv files are set.

3. Run `schema_ins.sql`. This SQL script should insert data into the database. Again, ensure that the paths to your data files are correct. Both `schema_IEM.sql` and `schema_ins.sql` scripts should be executed within your database command line interface or GUI.

4. Update the connection details in both `plots.py` and `__init__.py` files. These files contain the database connection strings. They need to have the correct details (database server, database name, user, password, etc.) to be able to connect to your database.

After these steps, your database should be set up correctly and the application is ready to be run.

### How to Run

The application can be executed by running the `main.py` file from your terminal or command prompt:

```
python main.py
```

After running the `main.py` script, your local server will start, and the web application will be accessible via your preferred web browser at the localhost (usually `http://127.0.0.1:5000/`). Here is a brief guide on how to interact with the application:

### How to Interact

1. **Create a New User Account**: On the sign-up page, fill in the requested information to create a new user account. It's necessary to be logged in to view and interact with the content.

2. **Login to an Existing Account**: Visit the login page to access your existing account. Simply input your account credentials to log in.

3. **Search for an IEM**: Once you're logged in, you can search for an IEM by its name using the search bar on the home page. Examples of searchable IEMs include "Apple AirPods Pro 2", "Moondrop Variations", "Truthear HEXA", and more. The search feature is case-insensitive and will provide a frequency response plot, a predicted preference percentage, and other associated data for the IEMs if the name is typed in correctly.

4. **Compare IEMs**: Optionally, after an initial search for an IEM, you can use the comparison search bar to compare one IEM against another. This comparison will display a plot comparing the frequency response of the two selected IEMs.

5. **Change User Password**: Navigate to the change password page to update an existing user's password. Remember, this is only possible if you're logged into the user account whose password you wish to change. After changing the password, try logging out and logging back in with the new password to ensure the changes have been applied.

6. **Delete an Account**: To delete an existing user account, visit the login page. Please note that this action can only be performed by the user who wishes to delete their own account.

### Requirements:
Run the code below to install the necessary modules.

```
pip install -r requirements.txt
```

The modules are listed in the requirements.txt file.

## Notes

The target chosen to calculate average predicted preference from is a modified diffuse field target. In which a -1.0dB/octave downward facing slope is applied as well as the addition of a Harman bass shelf below 200Hz. The justification for use of such a target is that it mimics the preference frequency response of speakers in ideal listening conditions. The bass shelf is added to compensate for the lack of a subwoofer, as Harman research shows that the average listener prefers an additional 9-12dB of subbass.
