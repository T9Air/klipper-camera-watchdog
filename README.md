# klipper-camera-watchdog
Spaghetti detection and messed up layer detection using a camera with timelapse.

# Installation and setup
Got to https://github.com/T9Air/klipper-camera-watchdog/blob/Docs/docs/INSTALLATION.md

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
