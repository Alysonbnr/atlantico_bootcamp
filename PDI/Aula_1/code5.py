from skimage.color import rgb2gray
from PDI.src.pdi_utils import load_page_image,show_image,manual_rgb2gray
# Import the otsu threshold function
from skimage.____ import ____

page_image = manual_rgb2gray(load_page_image())
# Show original image
show_image(page_image, 'Global thresholding')

# Obtain the optimal otsu global thresh value
global_thresh = ____(page_image)

# Obtain the binary image by applying global thresholding
binary_global = page_image ____ ____

# Show the binary image obtained
show_image(binary_global, 'Global thresholding')

# Set the block size to 35
block_size = ____

# Obtain the optimal local thresholding
local_thresh = ____(____, ____, offset=10)

# Obtain the binary image by applying local thresholding
binary_local = page_image ____ ____

# Show the binary image
show_image(binary_local, 'Local thresholding')