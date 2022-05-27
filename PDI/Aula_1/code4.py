from PDI.src.pdi_utils import show_image , load_chess_image
from skimage.color import rgb2gray

# Import the otsu threshold function
______


chess_pieces_image = load_chess_image()

# Make the image grayscale using rgb2gray
chess_pieces_image_gray = __

#show original image
__(__,'Original image')

# Obtain the optimal threshold value with otsu
thresh = __

# Apply thresholding to the image
binary = __

# Show the binary image
__(__, 'Binary image')