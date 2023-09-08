'''
1) Code loads an image, sets the minimum and maximum intensity values for the contrast stretching transformation

2) Creates a lookup table (LUT) to perform the transformation, applies the LUT to the image using the cv2.LUT function, 

3) Saves the enhanced image using the cv2.imwrite function. 

4) The LUT is an array of 256 elements, one for each possible pixel intensity value, 
and it is used to replace the intensity value of each pixel with the corresponding value from the LUT.
'''

'''
Image Processing and Data Visualization Winter Sem 2022 2023
Dhananjay Mandalkar
University of Wuppertal
'''

import cv2
import numpy as np

# Load the image

img = cv2.imread('BoneScan.jpg', cv2.IMREAD_GRAYSCALE)

# Define the minimum and maximum intensity values

min_val = 30
max_val = 150

# A lookup table (LUT) is a simple data structure that can be used to perform 
# image processing operations such as contrast stretching.

lut = np.zeros(256, dtype = img.dtype )
for i, v in enumerate(lut):
    if i < min_val:
        lut[i] = 0
    elif i > max_val:
        lut[i] = 255
    else:
        lut[i] = (i - min_val) * (255 / (max_val - min_val))

# Apply the lookup table to the image
img = cv2.LUT(img, lut)

# Save the enhanced image in the same folder
cv2.imwrite('Enhanced_BoneScan_Image.jpeg', img)