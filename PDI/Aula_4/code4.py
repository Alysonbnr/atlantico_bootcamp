
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint,ReduceLROnPlateau,TensorBoard
from PDI.src.pdi_utils import load_sign_language_data


#carregando informações do modelo
data_train , label_train , data_val , label_val, _ , _  = load_sign_language_data()

#inicialização de um modelo sequencial do keras
___

#adição da camada convolucional 2D
___

#adição da camada de redução maxpooling2D
__

#transformação dos dados em 1 dimensão
__

#adição da camada densa
___

#compilaçao do modelo
___


#definição do nome do modelo
model_name = "__"

#definição do arquivo salvo do modelo
model_file = model_name+'.h5'

#callback para usar tensorboard
tensorboard = __(log_dir="logs/{}".format(___))

#callback para salvar o modelo
mcp_save= __
#callback para interromper o treinamento quando não houver mais aprendizado
earlyStopping= __

#callback para reduzira a taxa de aprendizagem do modelo
reduce_lr_loss =__

#treinamento do modelo
____