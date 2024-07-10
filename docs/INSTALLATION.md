Required modules:
    1. cv2 - pip install opencv-python
    2. droans klipper_extras repo: https://github.com/droans/klipper_extras

# Installation
Run these steps if you do not have a Creality printer with built-in Klipper (Ender 3 V3 KE, K1 series etc.):
1. SSH into your Raspberry Pi and run the following commands:
 ```
cd ~/
git clone https://github.com/T9Air/klipper-camera-watchdog.git
cd ~/klipper-camera-watchdog
bash install.sh
```
2. Install [droans](https://github.com/droans) extended macros repo using the instructions over there: https://github.com/droans/klipper_extras
3. Install timelapse for your printer: https://github.com/mainsail-crew/moonraker-timelapse

If you do have a Creality printer with Klipper already installed run these steps: 
1. SSH into your printer and install [droans](https://github.com/droans) extended macros repo using the instructions over there: https://github.com/droans/klipper_extras
2. After you install the extended macro repo, run the install script and choose option 2 to load the Moonraker config.
3. Write down the directory under Klippy Environment and then exit the installer.
4. Navigate to the directory that you wrote down in step 3
5. Run the following commands
 ```
./python3 -m pip install opencv-python
cp ~/klipper-camera-watchdog/check_image.cfg "path" # CHANGE "PATH" TO THE PATH WHERE YOUR CONFIG FILES ARE STORED
cd ~/klipper-camera-watchdog
mkdir Image-files
```
6. Install timelapse for your printer: https://github.com/mainsail-crew/moonraker-timelapse

# Setup
1. In moonraker.conf change the output path to ~/klipper-camera-watchdog/Image-files/
2. Add check_image.cfg to your config path (where all your config files are. ex: ~/printer_data/config)
3. In printer.cfg add [include check_image.cfg]
4. In all of the files (check_image.cfg, compare_images.py, and config.yaml) you will need to change the directory paths to your user

>WARNING: In the Python script, the threshold after which to cancel the print has not been calibrated and will need to be changed.
