import pandas as pd
from PDI.src.pdi_utils import load_sign_language_data
import numpy as np
import matplotlib.pyplot as plt

# carregando as inforções do dataset
label_train ,info_list = load_sign_language_data(dataset_downsample=___, load_info_only=True)

# criando uma dataframe
df = _____

#calculando histograma dos atribubtos do dataset
_____

#plotando histograma calculado.
labels = info_list
x = np.arange(0,29)
rangey = 3500
y = np.arange(0,rangey, rangey*.1)
plt.xticks(ticks = x ,labels = labels, rotation = 'vertical')
plt.yticks(y)
plt.show()

