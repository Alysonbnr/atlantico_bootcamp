from skimage.color import rgb2gray
from PDI.src.pdi_utils import load_page_image,show_image,manual_rgb2gray
# Import the otsu threshold function
from skimage.filters import threshold_otsu, threshold_local

page_image = manual_rgb2gray(load_page_image())
# Show original image
show_image(page_image, 'Global thresholding')

# Obtain the optimal otsu global thresh value
global_thresh = threshold_otsu(page_image)

# Obtain the binary image by applying global thresholding
binary_global = page_image > global_thresh

# Show the binary image obtained
show_image(binary_global, 'Global thresholding')

# Set the block size to 35
block_size = 35

# Obtain the optimal local thresholding
local_thresh = threshold_local(page_image, block_size, offset=10)

# Obtain the binary image by applying local thresholding
binary_local = page_image > local_thresh
# Show the binary image
show_image(binary_local, 'Local thresholding')