'''
1) The code imports the OpenCV, numpy, and scipy libraries 
2) reads a grayscale image called "BrainNoise.jpeg,"
3) applies a median filter with a kernel size of 3 to it to reduce noise.
4) The goal of the code is to demonstrate the median filter's impact on noise reduction in images.
'''

'''
Image Processing and Data Visualization Winter Sem 2022 2023
Dhananjay Mandalkar
University of Wuppertal
'''

# the OpenCV library, which is used for image processing
import cv2

# the numpy library, which is used for numerical operations such as array manipulation
import numpy as np

# the numpy library, which is used for median filtering of the image
from scipy.ndimage import median_filter

# Load the image
img = cv2.imread('BrainNoise.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size for the median filter
kernel_size = 3

# Perform median filtering
filtered_img = median_filter(img, size=kernel_size)

# Convert the filtered image to 8-bit unsigned integer format
filtered_img = np.uint8(filtered_img)

# Concatenate the original and filtered images side by side
comparison_img = np.hstack((img, filtered_img))

# Add title for original image
cv2.putText(comparison_img,"Original Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

# Add title for filtered image
cv2.putText(comparison_img,"Filtered Image", (img.shape[1]+10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

# Display the images
cv2.imshow("Comparison", comparison_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
