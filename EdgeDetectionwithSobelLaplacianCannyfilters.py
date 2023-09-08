'''
The objective of the code is to demonstrate the usage Sobel, Laplacian and Canny filters
and effect of these image processing techniques on a single input image.
'''

'''
Image Processing and Data Visualization Winter Sem 2022 2023
University of Wuppertal
Dhananjay Mandalkar
'''

# imports the openCV library and the matplotlib library
import cv2
import matplotlib.pyplot as plt

# reads an image named 'Brain_autopsy_lateral_view_wiki.jpeg' in grayscale

img = cv2.imread("Brain_autopsy_lateral_view_wiki.jpeg",0)

# The dimensions of the image are set to width = 300 and height = 200
width = 300
height = 200
dim = (width, height)

# using the cv2.resize function
resized = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

# Convert the images from BGR to RGB
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

# The resized image is then passed through Sobel, Laplacian
# and Canny filters
# using the cv2.Sobel, cv2.Laplacian and cv2.Canny functions.
img1 = cv2.Sobel(resized,cv2.CV_64F,1,0,5) # Horizontal Sobel
img2 = cv2.Sobel(resized,cv2.CV_64F,0,1,5) # Vertical Sobel
img3 = cv2.Laplacian(resized,cv2.CV_64F)
img4 = cv2.Canny(resized,50,150)

#cv2.imshow("Original Image",resized)
#cv2.imshow("Horizontal Sobel",img1)
#cv2.imshow("Vertical Sobel",img2)
#cv2.imshow("Laplacian",img3)
#cv2.imshow("Canny",img4)

# Create a figure with 5 subplots
fig, axs = plt.subplots(1, 5, figsize=(150,75))

# Display the images
axs[0].imshow(resized)
axs[1].imshow(img1)
axs[2].imshow(img2)
axs[3].imshow(img3)
axs[4].imshow(img4)

# labeled with their corresponding filter names

axs[0].set_title("Original Image")
axs[1].set_title("Horizontal Sobel")
axs[2].set_title("Vertical Sobel")
axs[3].set_title("Laplacian")
axs[4].set_title("Canny")

# Show the plot
plt.tight_layout()
plt.show()

# the windows are closed when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
