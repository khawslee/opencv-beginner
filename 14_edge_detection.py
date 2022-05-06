import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in grayscale mode
img = cv2.imread('./asset/tennis.jpg', cv2.IMREAD_GRAYSCALE)

# Laplacian gradient method
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
# Sobel X gradient method
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
# Sobel Y gradient method
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
# Combine sobelX and sobelY
sobelCombine = cv2.bitwise_or(sobelX, sobelY)
# Canny edge detection method
canny = cv2.Canny(img, 80, 180)

# Define the title of the images
titles = ['Image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombine', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombine, canny]

# Iterate 8 times to show all the images in the pyplot
for i in range(6):
    # Plot 2 row, 3 column
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    # Show the titles on top of images
    plt.title(titles[i])
    # Remove plot ticks
    plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()
