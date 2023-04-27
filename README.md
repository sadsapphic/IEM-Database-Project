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

### Links to find reviewers whose measurements were used:

\n<reviewer_1> | link_1 | ... | link_n
\n<reviewer_2> | link_1 | ... | link_n
\n...
\n<reviewer_n-1> | link_1 | ... | link_n
\n<reviewer_n> | link_1 | ... | link_n

This is made possible as each reviewers squig.link site, hosts their IEM frequency response measurements at
<reviewer's name>.squig.link/data, from which it is possible to scrape and download the raw frequency response measurements.

Please note that the only data that was scraped from these sites are the frequency response measurements, and naturally, the names of the IEM's themselves.
All other data as been synthesized by curating a database containing the IEM names, from which the remaining data was manually collected by researching the IEM's individually. Though the database only includes entries for IEM's whose measurements are publically avalible, as it is seen as the most important datapoint per IEM.

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

## Dependencies:

## Installation:

## Note:
