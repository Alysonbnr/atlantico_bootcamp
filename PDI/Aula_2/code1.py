# Import threshold and gray convertor functions
from skimage.____ import ____
from skimage.color import ____
from PDI.src.pdi_utils import show_image, load_lools_image
gray_tools_image = rgb2gray(tools_image)

# Turn the image grayscale
gray_tools_image = ____

# Obtain the optimal thresh
thresh = ____(gray_tools_image)

# Obtain the binary image by applying thresholding
binary_image = gray_tools_image > ____


# Show the original image
show_image(tools_image, 'original image')
# Show the resulting binary image
show_image(binary_image, 'Binarized image')