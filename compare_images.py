import cv2
import os
import sys
import glob

# Image detection function

def detect_movement_background_subtraction(image1, image2):
    """
    This function detects movement between two images using background subtraction.

    Args:
        image1: The first image to compare. (OpenCV image object)
        image2: The second image to compare. (OpenCV image object)

    Returns:
        A string indicating if movement was detected or not. It goes to the choose_images() function.
    """

    # Create a background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Apply background subtraction to the images
    fg_mask = bg_subtractor.apply(image1)
    fg_mask = bg_subtractor.apply(image2)

    # Get height and width of images
    mask_height = fg_mask.shape[0]
    mask_width = fg_mask.shape[1]

    # Calculate the number of pixels in the mask
    total_pixels = mask_height * mask_width

    # Count num. of changed pixels
    changed_pixels = cv2.countNonZero(fg_mask)

# CHANGE THRESHOLD TO WHATEVER VALUE YOU WANT. LOWER = MORE LIKELY TO CANCEL THE PRINT. FROM 0-1.
    
    # Check if movement is detected based on a threshold of changed pixels
    if (changed_pixels / total_pixels) > threshold:
        return "Movement detected"
    else:
        return "No movement detected"


# Function to select appropriate images from a directory
def choose_images():
    """
    This function selects the most recent two images from a specified directory.

    Returns:
        A string indicating whether movement was detected or not. It goes to the g-code macro. 
        If this is the first image, it also returns "No movement detected".
    """

    # Check if there are at least two images
    if len(os.listdir('~/klipper-camera-watchdog/Image-files/')) > 1:
        # Sort image paths by creation time (newest first)
        image_paths = sorted(glob.glob('~/klipper-camera-watchdog/Image-files/*'), key=os.path.getctime, reverse=True)

        # Load the two most recent images
        image1 = cv2.imread(image_paths[0])
        image2 = cv2.imread(image_paths[1])

        # Call function to detect movement between the images
        result = detect_movement_background_subtraction(image1, image2)

    else:
        # No movement detection possible with less than two images
        result = "No movement detected"

    return result
