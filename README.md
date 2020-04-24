# Unemployment Rates and Emissions Rates in Georgia

In this analysis, I took two data sets, one for unemployment and one for emissions rates. The purpose was to see the relationship between unemployment rates and emissions rates in Georgia from 2005-2015. This range was selected in order to view the affect that the recession had on both sets of data.

### Where to get data

I got the electricity generation data from U.S Energy Information Administration. Download the emissions for Georgia by year. It contains data from 1980-2017. https://www.eia.gov/environment/emissions/state/

I obtained the unemployment data from the Bureau of Labor Statistics. I downloaded United States
unemployment rates by county from 2005-2015.https://www.bls.gov/lau/ Scroll down until
you see County Data. The title for each xls
file is Labor force data by county, x year.

The incomplete dataset for unemployment is from
kaggle. Other than the fact that it only has 47
states, it's a clean data set so I kept it in. https://www.kaggle.com/jayrav13/unemployment-by-county-us/data#

There are 3 python scripts and one GIS section.
They should be run in the order that they are given in the walkthrough. The emissionsbyga.py
sets up the data for it to be used in GIS. I use GIS to make heat maps of the unemployment rates for each map.  
The heatgif.py script makes the heat map gif from the png files made in GIS. The emissions_analyze.py cleans up the emissions data and prints out the total emissions by year.  

#### Python Instructions- emissionsbyga.py

1.) Import pandas as pd
    Import numpy as np
    import zipfile

2.) At this point, you'll see some lines of code to unzip a file and
extract unemployment data from Georgia. I downloaded this zipfile from
kaggle.com and didn't realize that it only contained data from 47 states.
Georgia happened to be one of the states that was excluded from the list.
I'm keeping the code in the script since it is otherwise a clean data set to use
for the states that are actually included.

3.) Set up the first data frame that has unemployment data by county for the entire United States in 2005 by
reading the excel file using pd.read_excel function.

4.) Put the rest of the excel files from 2006-2015 in a list

5.) Loop through the list in order to push them into a single dataset.

6.) Extract the data for Georgia only by using the .loc method on state fips code and create a csv.

7.) Loop over the data for Georgia and create a script that makes the county
fips codes all 3 digits long. It should add two zeros to single digit fips
codes and one zero to double digit fips codes. This is so that GIS can read the codes properly.

8.) In order for GIS to join to the tiger lines shape file properly, create a GEOID
column which adds the state fips code to the county fips code.

9.) Make a variable that calls the .unique method on realunemploy_ga['Year']

10.) Loop through the variable just created in order to create a csv for
each unique year found.

#### QGIS

1.) Open the tiger line shape file for the United States.

2.) Filter to just Georgia by using the state fips code.

3.) Save the result as a geopackage.

4.) Add the csv for unemployment in GA in 2005.

5.) Join the csv to the georgia layer by GEOID for both the target and join field.

6.) Check off the unemployment rate (%) variable in the joined fields and hit apply
and ok in the dialog box.

7.) Choose graduated in the layer styling toolbar and for the value, select
unemployment rate.

8.) Choose 6 classes with equal count (quintile).

9.) I created custom intervals since the data changes dramatically and classify
only uses the data from each year. The range I chose was 0-3.91, 3.91-7.91,
7.91-11.91, 11.91-14.91, 14.91-17.91, and 17.91-22.9. This is because the
highest rate of unemployment from 2005-2015 is 22.9 in the data.

10.) Once you're done with entering the range, click apply. Pro-tip, never hit
classify again when you're adding in the next year. The custom range that you
made will stay put after you've removed the year layer you completed. You just
need to only hit apply after adding in the next year's csv file.

11.) Export the heat map as a png file. Make sure to save it like unemploy_05.
It will be important later to have the _ year format when it comes time to make
a gif.

12.) Complete steps 4-11 for each csv file.

#### Python- Building a Gif of the Heat Map

1.) Import pandas as pd, import glob, import imageio
(you will need to download imageio if you haven't already. It can be done
simply by going into terminal and typing conda install imageio)

2.) Use the pd.read_csv call on 'realunemployforga.csv'

3.) By calling the idx.max and the idx.min method to the unemployment rate (%)
column in the unemployment dataset for Georgia, you can get the lowest and
highest value for the unemployment rate from 2005-2015. This was so that I
could figure out how to develop the intervals that were used in my heat map.

4.) Use glob on .png
(ex: filenames= glob.glob('* .png')
This will pull out
any .png files in your current working directory.

5.) Use list.sort to make sure that the files are ordered from lowest to highest
by year. This is why it was important to do the unemploy_05 format for saving
the png files.
sample code:
list.sort(filenames, key= lambda x: int(x.split('_ ' )[1].split('.png')[0]))

6.) Then make a loop of the images by calling back to filename in filenames.
Use imageio.mimsave to save the result to a gif. In the imageio.mimsave(), have
arguments for the .gif filename, images, and duration. I set duration to .75,
which refers to seconds.

7.) If it was run successfully, there should be a .gif file with the name you
gave it in the directory you're working in.

#### Python- Emissions Analyze

1.) Import pandas as pd and import numpy as np

2.) Add in 'georgia (1).xlsx' using read_excel.

3.) Get the emissions data into a dataframe where the year is the column and
the only data is from row 40, which is the total emissions with discrepancy. In
order to do this, you need to make a loop where nan values are picked out and
an else statement is used to turn the year numerical values into string values.

4.) Join x.columns to intyear by x.columns= intyear.

5.) Print out the values for total emissions by years from 2005 to 2015.
There is a big dip from 2008-2010 which is lines up with the recession.
Unemployment seems to dip with it from looking at the heat map.

**Notes

I wanted to run more analysis but the datasets I found were not cooperating
with me. Sorry for the brief analysis.
