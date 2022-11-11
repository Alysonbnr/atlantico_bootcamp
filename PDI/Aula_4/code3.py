from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint,ReduceLROnPlateau
from PDI.src.pdi_utils import load_sign_language_data


data_train , label_train , data_val , label_val, _ , _  = load_sign_language_data()

#inicialização do modelo sequencial do keras
__=___

#adição de camada convolucional 2D
__.__

#adição da camada de redução maxpooling
__.__

#transoformação dos dados em 1 dimensão
__.__

#adição da camada densa
__.__

#compilação do modelo
__.__

#definição do nome do modelo
model_file = '__.h5'

#callback para salvar o melhor modelo do treinamento
mcp_save = ModelCheckpoint(__ ,save_best_only=__, monitor='___', mode='___')

#callback para interromper o treinamento quando não existir evolução do modelo
earlyStopping = EarlyStopping(monitor='___', patience=__, verbose=__, mode='__')

#callback para diminuir a taxa de aprendizagem quando os dados de acerto não evoluírem
reduce_lr_loss = ReduceLROnPlateau(monitor='__', factor=__, patience=__, verbose=__,min_delta=1e-4,mode='__')

#treinamento do modelo
__.__(__, __ , __, ___, ___,callbacks=[___, ___, ___])