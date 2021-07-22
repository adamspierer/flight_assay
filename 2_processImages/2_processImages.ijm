// FIJI/ImageJ Flight Assay automated analysis
// Written on July 21, 2021 by Adam Spierer
// 
// The purpose of this script is to take images captured for a flight assay
//    and automate the identification of the fly landing heights.
// 
// To do for each experiment:
//    1. Specify input and output directories [lines 19 & 20]
//    2. Specify image file suffix [line 22]
//    3. Define the boundaries of the rectangle to crop (add padding to edge of plastic sheet)[line 35]
//    4. Confirm the maxima spot detection (prominence) threshold [line 39]
//    5. Spot check the images and the corresponding spots to ensure accurate parameters
//
// NOTE: When analyzing the only important column is the Y
//
// Defining image directories and image suffix

inputDirectory="/Users/aspierer/Downloads/png/";
outputDirectory="/Users/aspierer/Downloads/csv/";
imageSuffix=".png";

// Create a list of all files in the specified directory
filelist = getFileList(inputDirectory) 

for (i = 0; i < lengthOf(filelist); i++) { //
    if (endsWith(filelist[i], imageSuffix)) { 
        // Open each file that ends with /png
        filename=filelist[i];
        print(filename);
        open(inputDirectory + filename);
        
		// Crop the window and convert to 8-bit image
		selectWindow(filename);
		makeRectangle(477, 40, 295, 773);
		run("Crop");
		run("8-bit");
		
		// Locate individual flies
		run("Find Maxima...", "prominence=35 light output=[Point Selection]");
		run("Measure");

		// Save output and close windows
		saveFile = outputDirectory + replace(filename,".png",".csv");
		saveAs("Results",saveFile);
		close();
		Table.deleteRows(0, 9999);
    	} 
}