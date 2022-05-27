from PDI.src.pdi_utils import load_lena
import matplotlib.pyplot as plt

from PDI.src.pdi_utils import load_red_roses,show_image
import matplotlib.pyplot as plt

image = load_red_roses()

# Show original image
__(__,'image RGB')

# Obtain the red channel
red_channel = __

# Show original image
__(__,'image red channel')

# Plot the red histogram with bins in a range of 256
plt.__(__, bins=__)

# Set title and show
plt.title('Red Histogram')
plt.show()