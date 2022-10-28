import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import entropy


def load_red_roses():
    return plt.imread("PDI//Aula_1//imgs//red_roses.png")

def load_page_image():
    return plt.imread("PDI//Aula_1//imgs//page.jpg")

def load_chess_image():
    return plt.imread("PDI//Aula_1//imgs//chess_gray.png")

def load_woman():
    return plt.imread("PDI//Aula_1//imgs//woman.png")

def load_flipped_seville():
    return plt.imread("PDI//Aula_1//imgs//flipped_seville.png")

def load_lena():
    return plt.imread("PDI//Aula_1//imgs//lena.png")

def load_lools_image():
    return plt.imread("PDI//Aula_2//imgs//shapes52.jpg")

def load_soaps_image():
    return plt.imread("PDI//Aula_2//imgs//soaps.jpg")

def load_building_image():
    return plt.imread("PDI//Aula_2//imgs//toa-sharp-def-3.jpg")

def load_chest_ray_x():
    return plt.imread("PDI//Aula_2//imgs//contrast_00000109_005.png")

def load_aerial_image():
    return plt.imread("PDI//Aula_2//imgs//aerial.png")

def load_rotate_cat():
    return plt.imread("PDI//Aula_2//imgs//cat.jpg")

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def manual_rgb2gray(rgb_img):
    return np.array((rgb_img[:,:,0]*0.29 + rgb_img[:,:,1]*0.59 + rgb_img[:,:,2]*0.11)).astype(int)

def compute_entropy(labels, base=None):
    value,counts = np.unique(labels, return_counts=True)
    return entropy(counts, base=base)
