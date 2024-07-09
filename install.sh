# Print a message to the user explaining the purpose of the script and a warning.
echo "This installer will install some files and dependencies on your device. Never install something without knowing what it does."

# Prompt the user for confirmation to continue and store the answer in the response1 variable.
read -r -p "Are you sure you want to continue? (y/N) " response1

# Check if the user entered 'n' or 'N' for the first confirmation.
if [[ "$response1" == [Nn] ]]; then
  # If 'n' or 'N' was entered, print an exit message and exit the script with an error code.
  echo "Exiting..."
  exit 1
fi

# Prints a message to the user explaining the potential risks.
echo "This also installs a g-code macro, which can potentially harm your printer."

# Prompt the user for confirmation to continue and store the answer in the response2 variable.
read -r -p "Are you sure you want to continue? (y/N) " response2

# Check if the user entered 'n' or 'N' for the second confirmation.
if [[ "$response2" == [Nn] ]]; then
  # If 'n' or 'N' was entered, print an exit message and exit the script with an error code.
  echo "Exiting..."
  exit 1
fi

# Print a message indicating the script is installing dependencies.
echo "installing dependencies..."

# Change the directory to the specified location for dependency installation.
cd ~/klippy-env/bin

# Installs the opencv-python dependency using pip.
./python3 -m pip install opencv-python

# Print a message indicating successful dependency installation.
echo "dependencies installed"

# Print a message indicating the script is copying a macro file.
echo "copying macro to config file path..."

# Copy the check_image.cfg file from repository path to your printers config files path.
cp ~/klipper-camera-watchdog/check_image.cfg ~/printer_data/config

# Print a message indicating successful macro file copy.
echo "macro copied"

# Change the directory to the repository directory.
cd ~/klipper-camera-watchdog

# Create a directory named Image-files. This directory holds the images for the python script to check
mkdir Image-files

# Print a message with additional information required for the Python script to function.
echo "for this to work you need to install droans extended_macro repository at https://github.com/droans/klipper_extras/tree/main/extended_macro"
