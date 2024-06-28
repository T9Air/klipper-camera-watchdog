import cv2
import os
import sys

# Image detection function

def detect_movement_background_subtraction(image1, image2, threshold):
    # Create background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()
    
    # Apply background subtraction to the images
    fg_mask = bg_subtractor.apply(image1)
    fg_mask = bg_subtractor.apply(image2)
   
    # Get height and width of images
    mask_height = fg_mask.shape[0]
    mask_width = fg_mask.shape[1]

    # Calculate num. of pixels in mask
    total_pixels = mask_height * mask_width

    # Count num. of changed pixels
    changed_pixels = cv2.countNonZero(fg_mask)
    
    # Check if movement is detected
    if (changed_pixels / total_pixels) > threshold:    
        return "Movement detected"
    else:
        return "No movement detected"

# REPLACE IMAGE PATHS WITH YOUR IMAGES
def choose_images():
    image1 = cv2.imread('image1_path.jpg')
    image2 = cv2.imread('image2_path')

    # Get threshold value

    threshold = sys.argv[0]

    
    # Send results back to macro
    
    result = detect_movement_background_subtraction(image1, image2, threshold)
    return result
