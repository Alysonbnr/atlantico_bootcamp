# Import the required module
import matplotlib.pyplot as plt
from PDI.src.pdi_utils import show_image, load_chest_ray_x
from ____ import ____

chest_xray_image = load_chest_ray_x()
# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.____(____.ravel(), bins=____)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq =  ____.____(chest_xray_image)


# Show the resulting image
show_image(____, 'Resulting image')