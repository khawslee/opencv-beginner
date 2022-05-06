import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('./asset/girl1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define kernel to 5x5 size
kernel = np.ones((5,5), np.float32) / 25

# 2D convolution filter
dst = cv2.filter2D(img, -1, kernel)
# Blur filter
blur = cv2.blur(img, (5, 5))
# Gaussian blur filter
gaublur = cv2.GaussianBlur(img, (5, 5), 0)
# Median blur filter
medianblur = cv2.medianBlur(img, 5)
# Bilateral filter
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

# Define the title of the images
titles = ['Image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateral']
images = [img, dst, blur, gaublur, medianblur, bilateralFilter]

# Iterate 6 times to show all the images in the pyplot
for i in range(6):
    # Plot 2 row, 3 column
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    # Show the titles on top of images
    plt.title(titles[i])
    # Remove plot ticks
    plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()
