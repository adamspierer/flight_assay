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
## Python functions and script #########################################
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

## Check directory is valid
try:
  if os.path.isdir(argv[1]):
    csvDirectory = argv[1]
    print('Reading files from directory:',csvDirectory)
except:
  print('No command line arguments entered.\nReading files from hard coded directory:',csvDirectory)


## Concatenate DataFrames
d = pd.concat([create_df(csvDirectory,item) for item in os.listdir(csvDirectory) if item.endswith('csv')])

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

## Save results
h.to_csv(saveDirectory + "results.csv")
print('END')