# README - Analyzing flight assay images with FIJI/ImageJ

Written on July 22, 2021 by Adam Spierer

The purpose of this documentation is to provide instruction on how to extract the x,y-landing coordinates of flies from an image.

[FIJI](https://imagej.net/software/fiji/downloads) is an open-source, image analysis program released by the NIH. Here, we can use it to identify the landing heights for the flies, which can be used to get a distribution and mean.


### Converting pixels to meters

It is helpful to have a meter stick in the frame of the image to measure how long it is in pixels, and then convert to meters.

To do this, open an image and select the `straight` tool (line segment icon, fifth from the left on the main GUI). Click the top of the meter stick and drag to the bottom. Press `cmd + m` (Process > Measure) and a new window with a table containing a `Length` field will appear. Write down this length because it is used later.


### Particle detection with FIJI

The key steps are:
<ol> 
	<li>File > Open; test image</li>
	<li>Select the rectangle tool and draw a box bounding the top and bottom of the plastic sheet with a little bit of space on either side of the lateral edges.
	<li>Image > Crop</li>
	<li>Image > Type > 8-bit</li>
	<li>Process > Find Maxima... (select light background, 35 > prominence, and check the `preview point selection` box to visualize where the spots are)</li>
	<li>If all looks good, then Analyze > Measure</li>
	<li>File > Save as...; the output table to a directory of choice</li>
</ol>

When doing this for many images, it can become rote and tiring. So a custom FIJI macro (`2_processImages.ijm`) is available in the `2_processImages` directory. This macro runs through each of these steps, but in quick succession. To run this macro, click on the main GUI window and select Plugins > Macros > Edit... Select the `2_processImages.ijm` macro. This will open in a new window that the user can both edit and run from.

While there are instructions for running the macro in the text, it is important to do the following:

<ol>
	<li>Specify input and output directories [lines 19 & 20] </li>
	<li>Specify image file suffix [line 22]</li>
	<li>Define the boundaries of the rectangle to crop (add  padding to edge of plastic sheet) [line 35]</li>
	<li>Confirm the maxima spot detection (prominence) threshold [line 39]</li>
	<li>Spot check the images and the corresponding spots to ensure accurate parameters</li>
</ol>

Once these steps are complete, press the `Run` button. If the directories are correct, the program should generate csv files for each image processed.