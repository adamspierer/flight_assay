## Script for processing flight data
## Written August 3, 2021 by Adam Spierer
## 
## The purpose of this script is to take the result tables created by 
##    FIJI/ImageJ macro for analyzing flight performance data and bringing
##    the result files into a single file with all spots (all_flies.csv)
##    and an aggregated results file with the mean, standard deviation,
##    and counts for each combination in the `experimental_details` 
##    variable (results.csv).
##
## Areas of this script to modify by experiment:
##  1. The user can input the directory with the csv files for each analyzed 
##    image as either a command line argument, or as a hardcoded input [line 33/34]. 
##    If the user enters a command line argument, then the files created by this 
##    program will save to the same directory. If hardcoded, the user can change 
##    the saveDirectory path.
##  2. The user should go into FIJI/ImageJ to figure out the conversion factor
##    for pixels per meters and modify the corresponding variable [line 37].
##  3. The user should change the `experiment_details` [line 40] to represent
##    the column names corresponding with the underscore-separated fields in
##    the image file name. The number of items in this list should match those 
##    in the image file name.
##
## To run this script:
##    python <path_to_script> <optional_path_to_csv_directory>
##
##
##
########################################################################
## User specified variables ############################################
########################################################################
## Location of csv files
csvDirectory="/Users/aspierer/Documents/Postdoc/FlightAssay/2_processImages/csv/"
saveDirectory="/Users/aspierer/Documents/Postdoc/FlightAssay/3_concatenateData/"

## Conversion factor for pixels per meter
pixels_per_meter = 784

## User specified list of experimental details contained within file name
experiment_details=['condition','genotype','sex','replicate']

########################################################################
## Python functions ####################################################
########################################################################

## Load libraries
import pandas as pd
import os
from numpy import repeat
from sys import argv

## Function to strip suffix and split 
def scrape_details(filename):
  filename = filename.split('.')[0]
  filename = filename.split('_')[:]
  return filename

## Function to read and format DataFrame
def create_df(csvDirectory, File):
  _d = pd.read_csv(csvDirectory + File, usecols=['X','Y'])
  
  ## Assign experimental details to DataFrame
  name = scrape_details(File)	
  for col,detail in zip(experiment_details,name):
    _d[col] = repeat(detail,_d.shape[0])
    _d[col] = _d[col].astype('str')
    
  ## Convert pixels to meters
  _d['Y'] = _d.Y/pixels_per_meter
  ## Convert metric so it is distance fallen
  _d['Y'] = 1 - _d.Y
  return(_d)

########################################################################
## Python script #######################################################
########################################################################

## Check directory is valid
try:
  if os.path.isdir(argv[1]):
    csvDirectory = argv[1]
    saveDirectory = argv[1]
    print('Reading files from directory:',csvDirectory)
    print('Saving result.csv file to:   ',saveDirectory)
except:
  print('No command line arguments entered.\nReading/saving files from/to hard coded directory:',csvDirectory)

## Concatenate DataFrames
d = pd.concat([create_df(csvDirectory,item) for item in os.listdir(csvDirectory) if (item.endswith('csv') and item != 'all_flies.csv' and item != 'results.csv')])

## Groupby functions
##   Mean
e = d.groupby(experiment_details).Y.mean().reset_index()
e = e.rename({'Y':'mean'}, axis = 1).reset_index()
##   Standard Deviation
f = d.groupby(experiment_details).Y.std().reset_index()
f = f.rename({'Y':'std'}, axis = 1).reset_index()
##   Count
g = d.groupby(experiment_details).Y.count().reset_index()
g = g.rename({'Y':'count'}, axis = 1).reset_index()

## Merge DataFrames together
h = pd.merge(e,f)
h = pd.merge(h,g).drop(['index'],axis=1)

## Save file with aggregated results
h.to_csv(saveDirectory + "results.csv")

## Save file with all flies
d.to_csv(saveDirectory + "all_flies.csv")

print('END')