## 1. Contrast Stretching Transformation in OpenCV

### Overview

This documentation provides an overview of a Python script that performs contrast stretching transformation on an input grayscale image using OpenCV. The script follows a series of steps to enhance the image's contrast.

### Steps

1. **Load the Image**:
   - The script starts by loading an input image, which should be in grayscale format (e.g., 'BoneScan.jpg').
   - ![Original Image](https://github.com/dhananjayjm/Image-Processing-and-Data-Visualization-WiSe-22-23/blob/main/BoneScan.jpg)

2. **Set Minimum and Maximum Intensity Values**:
   - You can customize the minimum and maximum intensity values (`min_val` and `max_val`) to define the desired intensity range for the contrast stretching transformation. These values determine the range over which the transformation is applied.

3. **Create a Lookup Table (LUT)**:
   - A lookup table (`lut`) is created, consisting of 256 elements, one for each possible pixel intensity value (0 to 255).
   - The LUT is used to map each pixel's intensity value to a new value based on the specified minimum and maximum values.
   - Pixels with intensity values below `min_val` are mapped to 0.
   - Pixels with intensity values above `max_val` are mapped to 255.
   - Pixels with intensity values within the specified range are linearly stretched to cover the full intensity range (0 to 255).

4. **Apply the LUT to the Image**:
   - The script applies the lookup table (`lut`) to the input image using the `cv2.LUT` function. This step performs the contrast stretching transformation on the image.

5. **Save the Enhanced Image**:
   - The enhanced image is saved in the same folder with a specified filename (e.g., 'Enhanced_BoneScan_Image.jpeg') using the `cv2.imwrite` function.
   -![Enhanced Image](https://github.com/dhananjayjm/Image-Processing-and-Data-Visualization-WiSe-22-23/blob/main/Enhanced_BoneScan_Image.jpeg)

### Usage
To use this script:
   - Replace 'BoneScan.jpg' with the filename of your input grayscale image.
   - Customize `min_val` and `max_val` to control the intensity range for contrast stretching.
   - Run the script, and it will generate the enhanced image.

## 2. Median Filter Noise Reduction with OpenCV

### Overview

This documentation provides an overview of a Python script that demonstrates the application of a median filter to reduce noise in a grayscale image using OpenCV, NumPy, and SciPy libraries.

### Steps

1. **Import Libraries**:
   - The script imports the following libraries:
     - OpenCV: Used for image processing.
     - NumPy: Used for numerical operations and array manipulation.
     - SciPy: Specifically, the `median_filter` function is imported from SciPy's `ndimage` module for applying the median filter.

2. **Read the Grayscale Image**:
   - The script reads a grayscale image named "BrainNoise.jpeg."
   - ![](https://github.com/dhananjayjm/Image-Processing-and-Data-Visualization-WiSe-22-23/blob/main/BrainNoise.jpeg)

3. **Apply Median Filter**:
   - A median filter is applied to the grayscale image to reduce noise. The filter's kernel size is set to 3.

4. **Conversion to 8-bit Unsigned Integer Format**:
   - The filtered image is converted to an 8-bit unsigned integer format, suitable for displaying and storing image data.

5. **Concatenate Original and Filtered Images**:
   - The script creates a side-by-side comparison of the original and filtered images by concatenating them horizontally.

6. **Add Titles**:
   - Titles are added to both the original and filtered images to label them accordingly.

7. **Display the Images**:
   - The comparison image is displayed, showing the impact of the median filter on noise reduction in the original image.
   - ![](https://github.com/dhananjayjm/Image-Processing-and-Data-Visualization-WiSe-22-23/blob/main/Denoised%20brain%20image.png)

### Usage
   - Replace 'BrainNoise.jpeg' with the filename of your own grayscale image if needed.
   - Customize the `kernel_size` variable to adjust the filter's window size.
   - Run the script to see the effect of the median filter on noise reduction.

## 3. Image Processing with Sobel, Laplacian, and Canny Filters

### Overview

This documentation provides an overview of a Python script that demonstrates the usage of Sobel, Laplacian, and Canny filters for image processing. The script applies these image processing techniques to a single input image and displays the results.

### Steps

1. **Import Libraries**:
   - The script imports the following libraries:
     - OpenCV (`cv2`): Used for image processing.
     - Matplotlib (`plt`): Used for displaying images.

2. **Read the Input Image**:
   - An image named 'Brain_autopsy_lateral_view_wiki.jpeg' is read in grayscale.

3. **Resize the Image**:
   - The dimensions of the image are set to a width of 300 pixels and a height of 200 pixels using the `cv2.resize` function. The interpolation method used is `cv2.INTER_LINEAR`.
   
4. **Convert to RGB Format**:
   - The resized image is converted from BGR to RGB format for compatibility with Matplotlib.

5. **Apply Filters**:
   - The resized image is passed through the following filters:
     - Horizontal Sobel Filter (`cv2.Sobel` with `cv2.CV_64F` and horizontal kernel)
     - Vertical Sobel Filter (`cv2.Sobel` with `cv2.CV_64F` and vertical kernel)
     - Laplacian Filter (`cv2.Laplacian`)
     - Canny Edge Detection Filter (`cv2.Canny`)

6. **Display Images**:
   - The script displays the original image and the images processed with Sobel, Laplacian, and Canny filters using Matplotlib subplots.
   
7. **Label Subplots**:
   - Each subplot is labeled with its corresponding filter name.

### Usage
   - Replace 'Brain_autopsy_lateral_view_wiki.jpeg' with the filename of your own input image.
   - Run the script to observe the effects of Sobel, Laplacian, and Canny filters on the image.
   - Press any key to close the displayed images.
