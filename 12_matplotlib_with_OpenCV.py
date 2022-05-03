import cv2
import numpy
import numpy as np
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread('z.jpg', cv2.IMREAD_GRAYSCALE)
# Create a mask from image
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Define kernel to 2x2 size
kernel = numpy.ones((2,2), np.uint8)

# Dilation increase the area of mask
dilation = cv2.dilate(mask, kernel, iterations=2)
# Erosion, remove the corner of mask
erosion = cv2.erode(mask, kernel, iterations=1)
# Apply erosion then dilation on the mask
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# Apply dilation then erosion on the mask
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# Different between dilation and erosion of image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
# Different mask and opening of image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

# Define the title of the images
titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Open', 'Close', 'Gradient', 'TopHat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

# Iterate 8 times to show all the images in the pyplot
for i in range(8):
    # Plot 2 row, 4 column
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    # Show the titles on top of images
    plt.title(titles[i])
    # Remove plot ticks
    plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()
