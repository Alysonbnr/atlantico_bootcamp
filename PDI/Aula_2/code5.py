# Import the required module
from skimage import exposure
from PDI.src.pdi_utils import show_image,  load_aerial_image, compute_entropy
from scipy.stats import entropy
import matplotlib.pyplot as plt
import numpy as np


image_aerial = load_aerial_image()

# calcular e mostrar o histograma da imagem
hist_n_eq = plt.hist(image_aerial.ravel(), bins=255)
plt.show()

# realizar a equalização do histograma
image_eq =  exposure.equalize_hist(image_aerial)

# calcular e mostrar o histograma da imagem equalizada
hist_eq = plt.hist(image_eq.ravel(), bins=255)
plt.show()

# determinar a media do valor dos pixels que ocorrem na imagem não equalizada
img_mean_n_eq = np.mean(image_aerial)*255

# determinar a media do valor dos pixels que ocorrem na imagem  equalizada
img_mean_eq = np.mean(image_eq)*255

# determinar a variancia do valor dos pixels que ocorrem na imagem não equalizada
img_var_n_eq = np.var(image_aerial)*255

# determinar a variancia do valor dos pixels que ocorrem na imagem  equalizada
img_var_eq = np.var(image_eq)*255

# determinar os pixels que ocorrem com menor frequência da imagem não equalizada
l_freq = 0.2
low_freq_region_n_eq = np.where(hist_n_eq[0] < l_freq  * np.max(hist_n_eq[0]))

# determinar os pixels que ocorrem com menor frequência da imagem equalizada
low_freq_region_eq = np.where(hist_eq[0] < l_freq  * np.max(hist_eq[0]))

# determinar a media do valor dos pixels que ocorrem com menor frequência da imagem não equalizada
mean_pixel_low_freq_n_eq = np.mean(low_freq_region_n_eq[0])

# determinar a media do valor dos pixels que ocorrem com menor frequência da imagem equalizada
mean_pixel_low_freq_eq = np.mean(low_freq_region_eq[0])

# determinar a entropia do histograma da imagem não equalizada
hist_entropy_n_eq = compute_entropy(hist_n_eq[0], base=2)

# determinar a entropia do histograma da imagem equalizada
hist_entropy_eq = compute_entropy(hist_eq[0], base=2)

#Mostrar os valores calculdos
print("media de valores de pixel na imagem não eq: ", img_mean_n_eq)
print("media de valores de pixel  na imagem eq: ", img_mean_eq)

print("variancia de valores de pixel na imagem não eq: ", img_var_n_eq)
print("variancia de valores de pixel  na imagem eq: ", img_var_eq)

print("entropia de valores do histograma da imagem não eq: ", hist_entropy_n_eq)
print("entropia de valores do histograma da imagem eq: ", hist_entropy_eq)

print("numero de pixels com probabilidde de ocorrencia menor que,", l_freq , " na imagem não eq: ", len(low_freq_region_n_eq[0]))
print("numero de pixels com probabilidde de ocorrencia menor que,", l_freq , " na imagem eq: ", len(low_freq_region_eq[0]))

print("media de valores de pixel de baixa probablidade de ocorrencia na imagem não eq: ", mean_pixel_low_freq_n_eq)
print("media de valores de pixel de baixa probablidade  de ocorrencia na imagem eq: ", mean_pixel_low_freq_eq)

# Show the original and resulting image
show_image(image_aerial, 'Original')

show_image(image_eq, 'Resulting image')