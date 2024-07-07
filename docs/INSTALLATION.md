Required modules:
    1. cv2 - pip install opencv-python
    2. droans klipper_extras repo: https://github.com/droans/klipper_extras

# Setup
1. SSH into your Raspberry Pi and run the following commands:
 ```
cd ~/
git clone https://github.com/T9Air/klipper-camera-watchdog.git
cd ~/klippy-env/bin
./python3 -m pip install opencv-python
cd ~/klipper-camera-watchdog
mkdir Image-files
```
2. Install @droans extended macros repo using the instructions over there: https://github.com/droans/klipper_extras
3. Setup timelapse for your printer: https://github.com/mainsail-crew/moonraker-timelapse
4. In moonraker.conf change the output path to ~/klipper-camera-watchdog/Image-files/
5. Add check_image.cfg to your config path (where all your config files are. ex: ~/printer_data/config)
6. In printer.cfg add [include check_image.cfg]
7. In all of the files (check_image.cfg, compare_images.py, and config.yaml) you will need to change the directory paths to your user

>WARNING: In the Python script, the threshold after which to cancel the print has not been calibrated and will need to be changed.