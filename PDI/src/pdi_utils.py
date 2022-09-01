import matplotlib.pyplot as plt
import numpy as np


def load_red_roses():
    return plt.imread("imgs//red_roses.png")

def load_page_image():
    return plt.imread("imgs//page.jpg")

def load_chess_image():
    return plt.imread("imgs//chess_gray.png")

def load_woman():
    return plt.imread("imgs//woman.png")

def load_flipped_seville():
    return plt.imread("imgs//flipped_seville.png")

def load_lena():
    return plt.imread("imgs//lena.png")

def load_lools_image():
    return plt.imread("imgs//shapes52.jpg")

def load_soaps_image():
    return plt.imread("imgs//soaps.jpg")

def load_building_image():
    return plt.imread("imgs//toa-sharp-def-3.jpg")

def load_chest_ray_x():
    return plt.imread("imgs//contrast_00000109_005.png")

def load_aerial_image():
    return plt.imread("imgs//aerial.png")

def load_rotate_cat():
    return plt.imread("imgs//cat.jpg")

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def manual_rgb2gray(rgb_img):
    return np.array((rgb_img[:,:,0]*0.29 + rgb_img[:,:,1]*0.59 + rgb_img[:,:,2]*0.11)).astype(int)
