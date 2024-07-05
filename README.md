# klipper-camera-watchdog
Spaghetti detection and messed up layer detection using a camera with timelapse.

Required modules:
    1. cv2 - pip install opencv-python
    2. droans klipper_extras repo: https://github.com/droans/klipper_extras

# Setup
1. SSH into your Raspberry Pi and run the following commands:
 ```
cd ~/
git clone https://github.com/T9Air/klipper-camera-watchdog.git
```
2. Install @droans extended macros repo using the instructions over there: https://github.com/droans/klipper_extras
3. Install cv2: go to /home/$USER/klippy-env/bin, and run ./python3 -m pip install opencv-python
4. Setup timelapse for your printer: https://github.com/mainsail-crew/moonraker-timelapse
5. In moonraker.conf change the output path to ~/klipper-camera-watchdog/Images/
6. Add check_image.cfg to your config path (where all your config files are. ex: ~/printer_data/config)
7. In printer.cfg add [include check_image.cfg]
8. In all of the files (check_image.cfg, compare_images.py, and config.yaml) you will need to change the directory paths to your user

>WARNING: In the Python script, the threshold after which to cancel the print has not been calibrated and will need to be changed.

# Contributing
Any help in developing this repo is greatly appreciated. However, I have a few requests to make:

1. Please do not fork and PR against the main branch. Anything in the main branch should be considered live, released code.
2. If you are making changes to the Python script please fork and PR to the Python-Script-Additions branch (do not make any changes to the G-Code macro when making a PR to this branch)
3. Likewise with any changes to the G-Code macro (do not make any changes to the Python script when making a PR to this branch)
4. If you are making changes that require both the Python script and the G-Code macro to be changed fork and PR to the development branch
5. Do not PR to the development branch if you are changing both the Python script and the G-Code macro, but the changes to each are not needed for the other, make 2 individual PRs to the Python-Script-Additions branch and the G-Code-Macro-Additions branch)
6. Any changes that are not to the G-Code macro or the Python script should be to the Development branch
7. Please name your commits accordingly, and add some context as to what you have added.

# Thank you's
Thank you to @droans for the extended_macros repo, and the all the help you gave when I had trouble setting it up.
