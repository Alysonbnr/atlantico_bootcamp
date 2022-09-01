# Import the color module
from ____ import ____

# Import the filters module and sobel function
from skimage.____ import ____

from PDI.src.pdi_utils import load_soaps_image,show_image

soaps_image = load_soaps_image()

# Make the image grayscale
soaps_image_gray = ____.____(soaps_image)

# Apply edge detection filter
edge_sobel = ____(____)

# Show original and resulting image to compare
show_image(soaps_image, "Original")
show_image(edge_sobel, "Edges with Sobel")