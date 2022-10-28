# Import the required module
import matplotlib.pyplot as plt
from PDI.src.pdi_utils import show_image, load_chest_ray_x
from skimage import exposure

chest_xray_image = load_chest_ray_x()

# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=255)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq = exposure.equalize_hist(chest_xray_image)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')

# Show the histogram equalized
plt.hist(xray_image_eq.ravel(), bins=255)
plt.show()
