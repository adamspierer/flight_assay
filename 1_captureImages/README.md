# README - Performing the Flight Assay and operating the Raspberry Pi

Written on July 22, 2021 by Adam Spierer

The purpose of this documentation is to provide instruction on how to run the flight assay set up in the Rand Lab at Brown University.

The flight assay was originally described in  the JoVE article: [An Improved Method for Accurate and Rapid Measurement of Flight Performance in Drosophila](https://www.jove.com/t/51223/an-improved-method-for-accurate-rapid-measurement-flight-performance). These instructions build on the analysis of data from this publication, though setting up and running the assay are largely the same.
__


## Setup - Assay

Assay setup is identical to what is described in the linked protocol above. Follow the instructions for the flight column set up, but not the photographing section. A shopping list is provided in the article in case parts break or others wish to recreate this assay.

One area of emphasis comes in the application of the TangleTrap adhesive. Coat the surface of the plastic sheet with a uniform and thin layer of the adhesive. There isn't a set thickness to how much is needed, though a quarter to half a fly's thickness might be a good starting point. Use the plastic fins to spread the adhesive uniformly across the sheet. The adhesive often builds up in the middle so make sure there is sufficient levels on the edges.

Once the adhesive is applied, roll the plastic sheet length-wise and feed it into the column. This can be tricky and the lower corners may overlap. This isn't the worst thing, but also isn't the best, so take care to minimize if possible. Finally, line the flight column beneath the funnel so flies will drop straight down into the dish of mineral oil if they do nothing, or can fly to the edge if they are able.


## Setup - Computer and camera

Turn on the Raspberry Pi by plugging the labeled cords: power, HDMI, USB - keyboard, and USB - mouse, into the appropriate ports. This will take a minute to boot, but will result in a desktop that can be clicked around.

<img src="https://github.com/adamspierer/flight_assay/blob/main/images/begin_flightAssay.png" width="600" height="400" align="center">

Right click the `flightAssay.py` icon on the Desktop and open with `Text Editor`. This file contains the script for running the flight assay program. *The user should adjust the first few lines so the program outputs the images in the appropriate directory (creating a new directory if the desired one doesn't exist), as well as the experimental condition categories.* The default is three `field_label`s (mtDNA, nDNA, sex), though these names/labels can be changed in the first few lines of the code. They ultimately don't matter and serve as  a guide for the user to differentiate field names. More fields can be added, but this requires modification of the GUI window parameters, and how many fields & boxes are specified. The simplest solution to including more than three experimental conditions is to double up on conditions in a single field and separate with an underscore (`_`). Downstream programs look for that delimiter to parse the file name.

[image?]

Next, click the Terminal icon on the top menu (black square with white `>_` inside) and type:
`python ~/Desktop/flightAssay.py`

*NOTE*: Users should move the `1_captureImages.py` script from this repo's scripts folder to the Desktop of the Pi and rename it `flightAssay.py`. The script provided is meant to be a template, not a final solution.

<img src="https://github.com/adamspierer/flight_assay/blob/main/images/running_flightAssay.png" width="600" height="400" align="center">

At this point, the program is running and can be quit by pressing the `Quit` button or by closing the GUI. Performing a `KeyboardInterrupt` (ctrl + c) in the Terminal will freeze the program and require closing that instance of the Terminal to end it completely.

The Terminal will prompt the user for a desired time to preview the camera image. This is useful for making sure the camera and poster board are appropriate distances apart and that the lighting is good. If the user decides to press the `Preview` button on the GUI, it will preview for the number of seconds specified in the first few lines of the script (default: 10 seconds)

Once all is good, the camera is setup.

*NOTE*: Consider putting the directory for output images on a removable USB drive so the Pi's harddrive does not fill up during the experiment. This is not required, but will also save a step later on because the files will need to be transfered off the computer so FIJI can be used.

## Run - Assay

Tap vials of 20 flies down so flies are at the bottom. Quickly, unplug and invert the vial into the chute. This can be tricky and requires practice. Once the flies are sent through, pull the chute up, remove the vial, and place in a discard bin. Theoretically, up to 200 flies can be tested on a single sheet of plastic, though I generally stayed with around 100. More is better.

Once all flies have been flown, pull the column out from under the funnel. Grasp the plastic sheet by the top and pull up. Make sure to keep a set of hands around the sheet when it is pulled or it will spring open and flies will dislodge. Take the sheet to the poster board and use the binder clips at the top to hold the plastic sheet to the poster board. Set the board against the wall.

A key difference between the linked protocol and this one is how the plastic sheet is photographed. In this protocol, we are placing the plastic sheet on a piece of white poster board and affixing the two with binder clips at the top. The board is then placed against a wall and photographed in the vertical position. Because the sheet is held vertically and the flies are largely immobilized, there is a chance that flies will wander if the experimenter waits too long to record the image. This wandering contributes to an insignificant level of variation in the data, but is best to minimize by capturing the image in a reasonable period of time. Follow instructions below for running the camera.

Before running the next set of flies, make sure to count and remove the flies that fall through the column and into the shallow dish/weigh boat of mineral oil. These flies are not included in the final score, but represent their own phenotype ( fallen / ( fallen + identified ) ).


## Run - Camera

Running the camera is simple. Enter the experimental conditions into the GUI fields and press the `Capture` button. 

*If a file with that same name already exists, no image will be captured.* A very brief live view of the camera will be displayed immediately after the image is captured to make sure the user knows the image was recorded. If no image is displayed, the no image was captured.


## Resetting the assay

An important part of the assay is picking off the flies from the adhesive. This is best done with foreceps and a small piece of paper towel (have a stack of paper towels on hand, preferably standard lab paper towels cut roughly into thirds). Pick flies off so there are no leftover heads, since these can get picked up in the next image. Wings are trickier and on their own don't get picked up, but build up of enough can darken the background and decrease the detection ability.

The adhesive does not need to be scraped between runs. This would constitute a large and unnecessary time addition to the protocol. Instead, inspect the plastic and adhesive every so often and make sure there is generally even coverage across the sheet. Over time, there will be spots with less coverage. These can be filled in by smoothing over the adhesive, or by filling in with additional adhesive and then smoothing over.


## Cleaning up the assay

Use the plastic scraper to remove the adhesive from the plastic sheet. The adhesive will come off in globs, so use a paper towel to remove it from the scraper. The sheet and surrounding surfaces can be cleaned using the orange-scented cleaner. It is not essential to the next round of assays to remove all the adhesive, but it makes for a clear work environment.

The computer can be turned of by pressing the Raspberry logo on the left side of the top menu and selecting the shutdown option, and then the shutdown option again.
