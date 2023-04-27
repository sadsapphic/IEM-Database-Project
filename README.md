# IEM Database Project
Databases and Information Systems (NDAB21010U) Project

## Credits:
Victor Villumsen Bergien | TCG780 | tcg780@alumni.ku.dk

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
- Mention measurement rig differences (IEC711, Gras, BK 5128, etc)
- Explore the idea of grouping measurements by reviewer (so one reviewer does not saturate the average for a given IEM)

## Dependencies:

## Installation:

## Note:
