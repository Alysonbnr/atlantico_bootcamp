
# Import Gaussian filter
from skimage.filters import gaussian
from PDI.src.pdi_utils import load_building_image,show_image
building_image = load_building_image()


# Apply filter sigma = 1
gaussian_image = gaussian(___, sigma=___,multichannel = True)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian with sigma = 1")


# Apply gaussian filter sigma = 5
____

# Show resulting image to compare
show_image(___, "Reduced sharpness Gaussian with sigma = 5")

# Apply filter sigma = 10
____

# Show resulting image to compare
show_image(___, "Reduced sharpness Gaussian with sigma = 10")