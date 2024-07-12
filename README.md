# klipper-camera-watchdog
3d print error detector that catches errors before normal AI spaghetti detectors.
> Note: The background on how I decided to start this project is at the bottom of the page since it is a few paragraphs long, and I do not want to bore people who just want to get to all the important stuff.

# Installation and setup
Go to https://github.com/T9Air/klipper-camera-watchdog/blob/main/docs/INSTALLATION.md

# Contributing
Go to https://github.com/T9Air/klipper-camera-watchdog/blob/main/docs/CONTRIBUTING.md

# Code of Conduct
Go to https://github.com/T9Air/klipper-camera-watchdog/blob/main/docs/CODE_OF_CONDUCT.md

# Roadmap
These are my plans for the future. Go to https://github.com/T9Air/klipper-camera-watchdog/blob/main/docs/ROADMAP.md

# Releases
The releases are more of a way to make official separations to be able to tell how the project has evolved over time. I plan on making enough changes to the code to have a new release every 1-3 weeks. 

After every new release, all branches will be updated to match the master branch. This may cause that branch to be deleted and a new branch with the same name to be created.

# Warning
This repository includes a g-code macro which can potentially damage your printer. Never use a macro unless you understand what it does.

# Background
I saw a post on [reddit](https://www.reddit.com/r/3Dprinting/comments/1dmbpg0/instead_of_detecting_spaghetti_why_not_detect_a/) where the [OP](https://www.github.com/markcarroll) asked why most software looks for spaghetti since spaghetti is usually caused by the object moving on the print bed. The OP thought that maybe we should just take images after each layer, and see if the object moved in between layers. After seeing this I decided to try to make something that would do this, because who knows? Also, I figured that be detecting when the object itself moves, you should be able to catch errors earlier, and who does not want to do that?

So I started working and chose to use Python as the language that will be run to check the images for movement. Luckily, it was very easy to find the library that I could use to check for differences between the images just by looking it up. That library is called [cv2](https://pypi.org/project/opencv-python/). I then tried to see if I could take images using the Python script but then realized that it would not work since the camera is already being used so that I can view my printer through Fluidd or Mainsail. Therefore I decided to take images using a timelapse but save the images to a location that the script can access. 

After creating the macro to move the printer to a specified location to take the timelapse frame, I ran into another problem. How would I run the Python script from the macro, and then cancel the print if movement is detected? First I tried running the Python script from a shell script (I forget what repository I used to get the ability to run a shell script from a macro), but I could not figure out how to pass back to the macro whether to cancel the print or not. Luckily, I found [droans](https://github.com/droans) [extended_macros](https://github.com/droans/klipper_extras) repo, which allowed me to run a Python script from inside a g-code macro. After that, it was easy to figure out how to tell the macro to cancel the print by just returning a value, and based on that, the macro would decide whether to cancel the print or not.

And that is basically why I decide to start this project, and how I set the main code up! I do have a few things that I would like to add, some more and some less complicated, but for now, everything is working. I only have 1 problem, which is what the threshold value for canceling the printing should be. Any help with trying to figure it out would be greatly appreciated.

# Thank you's
Thank you to [droans](https://github.com/droans) for the [extended_macros](https://github.com/droans/klipper_extras) repo, and all the help you gave when I had trouble setting it up.
