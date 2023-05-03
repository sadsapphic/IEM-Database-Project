# IEM Database Project
Databases and Information Systems (NDAB21010U) Project by Group 22 & Group 23

## Credits:
Victor Villumsen Bergien | TCG780 | tcg780@alumni.ku.dk | Group 22 <br />
Mateo Anusic | DJZ709 | djz709@alumni.ku.dk  | Group 23 <br />
Emil Thorlund | GPV679 | gpv679@alumni.ku.dk  | Group 22 <br />
Lucas A. Rosing | QGC922 | qgc922@alumni.ku.dk | Group 23 

### Data Sources:
The data used to create this database has been mainly sourced from squig.link, a website used by reviewers to
host their IEM frequency response measurements. The following reviewers squig.links have been used to scrape data:

Acho Reviews, 
Aftersound, 
Animagus, 
Audio Review News, 
Bedrock Reviews, 
Bry Audio Reviews, 
CammyFi, 
Elise Audio, 
EPLV, 
Gizaudio, 
Harpo, 
Hawaii Bad Boy, 
Hi End Portable, 
Hobby Talk, 
ianfann, 
IEM World, 
Jacstone, 
kr0mka, 
Kurin, 
Melatonin, 
nymz, 
Paul Wasabi, 
Recode, 
Rikuduo Goku, 
Shortbus, 
Side Salad Audio, 
Super* Review, 
tgx78, 
Vortex Reviews, 
VSG, 
wdym, 
Akros

With plans to add:
freeryder05, 
Precogvision

This is made possible as each reviewers squig.link site, hosts their IEM frequency response measurements at
<reviewer's name>.squig.link/data, from which it is possible to scrape and download the raw frequency response measurements.

Please note that the only data that was scraped from these sites are the frequency response measurements, and naturally, the names of the IEM's themselves.
All other data as been synthesized by curating a database containing the IEM names, from which the remaining data was manually collected by researching the IEM's individually. Though the database only includes entries for IEM's whose measurements are publically avalible, as it is seen as the most important datapoint per IEM.

### Links to find reviewers whose measurements were used:

<reviewer_1> | link_1 | ... | link_n <br />
<reviewer_2> | link_1 | ... | link_n <br />
... <br />
<reviewer_n-1> | link_1 | ... | link_n <br />
<reviewer_n> | link_1 | ... | link_n

## Introduction:
This project consists of a comprehensive (possibly the largest) database of IEM's (In-Ear Monitors).
Each IEM has the following data:

- IEM Name
- Brand
- Price ($)
- ANC Capability
- Sensitivity (dB/mW)
- Impedance (Ω)
- \# of Drivers
- Driver Configuration
- Connection Type
- Microphone
- IP Rating	
- Measurement(s)
- Misc Measurement(s) (DSP Modes)
- \# of Measurements
- Contributing Reviewers

From which the following can be calculated:

- Average Measurement
- Preference % (The adherence the IEM's FR measurements has to a given target, as a %)
- Average  Error (dB)
- Slope of Error
- STDEV of Error
- Variance

Where the preference % can be used to rank the IEM's within the database based off of their audio quality performance, thus applying data to rank a traditionally subjective matter. As each person has their own HRTF (Head Related Transfer Function), despite this, it is still possible to make judgements on audio performance based off an average preference targets, such as the Harman targets. Though the database does also include a plethora of other targets to match the users preference.

Plan to allow user-uploadable targets.

## Write in future:
- Reference other IEM databases: Crinacle, Banbeu, etc.
- None offer functionality to display preference %
- Explain where idea for preference % came from (Harman research)
- Mention measurement rig differences (IEC711, Gras 43AG, B&K 5128, etc)
- Explore the idea of grouping measurements by reviewer (so one reviewer does not saturate the average for a given IEM)
- Mention difficulty caused by difference reviewers using different naming schemes, resulting in multiple names for the same IEM.

## Dependencies:

## Installation:

## Note:

# To Do List:
- ~~Scrape squig.link for all IEM measurements and download them locally~~
- ~~The measurements should be sorted into folders based off what reviewers produced the measurements~~
- ~~The .txt files are to be converted into .csv files with only X,Y columns. All excess data is to be discarded~~
- ~~These .csv files should be grouped together in the dataframe (or similar) where all measurements for a specific model of IEM are grouped together.~~ Target csv files should be identified and grouped seperately. (There are still some targets that need to be grouped correctly)
- For IEM’s with multiple measurements, calculate average frequency response
- Now that each IEM only has one corresponding measurement, calculate the Predicted Preference %
- Update the current preference % function to include the following functionality:
	- Variance
- Create a dataframe to store the following information:
	- Brand, IEM, Preference %, Avg Measurement, Contributing Measurements, # of Measurements, Contributing Reviewers, Avg  Error (dB), Slope of Error, STDEV of Error, Variance, Best Preference %, Worst Preference %
- Sort this dataframe based off the Predicted Preference %
- Generate plots of highest ranking IEM's, these plots should include the same information as in the dataframe

### Short-term To Do:
- Fix the # of measurements in the dataframe/create new logic to count the # of contributing .csv files used to derive an average
- Fix the spikes seen at 20Hz in some of the average frequency response plots
- Create a function to calculate the best and worst preference % so that it can be stored in the dataframe
- Similarly, in addition to using the average measurement to calculate standard deviation and variance, use all contributing measurements to calculate standard deviation and variance as well
- Add the following reviewer(s) to the list of reviewers: progvision

### Long-term To Do:
- Create (at least) three seperate dataframes, one for the main information, one for the average measurements and one for the reviewers
- Export these dataframes as .csv files, and import these into SQL
- Create web app to interact with said SQL database
	This web app could have the following functionality:
	- Allow the user to select either a target or IEM to get information about the preference %
	- Ability to show individual measurements instead of the average (useful in cases where an IEM has different modes/reviewers using different eartips etc)
	- Ability to plot the X,Y values for the measurements

### Possibly To Do:
- Gather additional information for each IEM's, such as:
	- Price ($), ANC, Sensitivity dB/mW, Impedance (Ω), # of Drivers, Driver Configuration, Connection Type, Microphone, IP Rating
- Create compensation curve for each reviewer to normalize measurements based off their rig
