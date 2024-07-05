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

Thank you to @droans for the extended_macros repo, and the all the help you gave when I had trouble setting it up.
