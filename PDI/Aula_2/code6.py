# Import the module and the rotate and rescale functions
from PDI.src.pdi_utils import show_image,load_rotate_cat

image_cat = load_rotate_cat()
from skimage.___ import ___, ____

# Rotate the image 90 degrees clockwise
rotated_cat_image = ____(image_cat, ____)

# Rescale with anti aliasing
rescaled_with_aa = ____(rotated_cat_image, 1/4, ___=__, __=__)

# Rescale without anti aliasing
rescaled_without_aa = ____

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")