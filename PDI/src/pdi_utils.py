import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
import requests


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

def load_sign_language_data(asl_train = 'dataset/asl_alphabet_train', dataset_downsample = 0.1, load_info_only = False):

    data = []
    label_data = []

    classes =  list(os.listdir(asl_train))
    for classe in range(len(classes)):

        path = os.path.join (asl_train, classes[classe])
        dir_list  = list(os.listdir(path))

        for  id, dir in enumerate(dir_list):
            letter_path =  os.path.join(path,dir)
            print('[INFO]- carregando letra ',dir )
            img_list = list(os.listdir(letter_path))
            for img in img_list[:int(dataset_downsample * len(img_list))]:
                if load_info_only:
                    label_data.append(id)
                else:
                    img_array = cv2.imread(os.path.join(letter_path, img), cv2.IMREAD_COLOR)
                    img_array = cv2.resize(img_array, (100, 100))
                    data.append(img_array)
                    label_data.append(id)

    if load_info_only:
        return label_data, dir_list

    data_train,data_val,label_train,label_val = train_test_split(data,label_data,test_size=0.3)
    data_val,data_test,label_val,label_test = train_test_split(data_val,label_val,test_size=0.2)

    data_train = np.array(data_train )/255
    data_val= np.array(data_val)/255
    data_teste = np.array(data_test)/255

    return data_train , np.array(label_train) , data_val , np.array(label_val), data_teste , np.array(label_test)


