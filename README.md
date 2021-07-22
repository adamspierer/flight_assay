# README - Flight Assay

This repository provides documentation, scripts, and example images for running the flight performance assay. The assay was adapted from the publication: [An Improved Method for Accurate and Rapid Measurement of Flight Performance in Drosophila](https://www.jove.com/t/51223/an-improved-method-for-accurate-rapid-measurement-flight-performance), and differs in the image capture set up and data processing.

This repository contains three sections:

<ol>
	<li>Capturing Images</li>
	<li>Processing Images</li>
	<li>Concatenating Data</li>
</ol>

Scripts, `README`, and example files for each section are contained in the respective folder. This repository is not meant to be run as is, but instead pulled from an adapted to each computer that needs to use the scripts.

### 1. Capturing Images

In the original protocol, image capture was originally done by laying the plastic sheet on a table and capture a picture with a handheld camera. The present protocol builds on this by placing the plastic sheet on a white poster board, propping it against a wall, and using a Raspberry Pi and PiCamera V2 (mounted to a fixed position with a MakerBeam kit) to record and name images.

The Python2 script provided will run a graphical user interface (GUI) on the Raspberry Pi and allow the user to enter experimental conditions that are pertinent to downstream analysis (ex. genotype, sex, condition).


### 2. Processing Images

Images are processed using [FIJI/ImageJ](https://imagej.net/software/fiji/downloads) and a custom macro (provided) that loops through all files in a specified folder with a specified suffix (ex. png, tif, jpg). The macro will crop the image to a user-specified region of interest and perform the 'Find Maxima...' function located under the 'Process' menu. This function will generate a list of x,y coordinates for each spot which should be spot checked by the user to ensure the 'Prominence' or detection threshold is appropriately set.

An additional step should be taken during set up to calculate the number of pixels per meter so final y-outputs can be converted from pixels to the metric system.


### 3. Concatenating Data

Output data is processed by stripping the experimental metadata from the file name, converting pixels to metric units, and concatenating data points into a larger file for the entire experiment. This final file can be used for data visualization and statistical analysis.


## Citation
These scripts were originally designed to improve on the throughput of the published protocol. It is used in the [PLOS Genetics paper](https://doi.org/10.1371/journal.pgen.1008887). Please cite accordingly.