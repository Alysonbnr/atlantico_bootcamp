from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
from PDI.src.pdi_utils import load_sign_language_data


#carregando informações do dataset
data_train , label_train , data_val , label_val, _ , _  = load_sign_language_data()

#inicialização do modelo sequencial do keras
model = keras.__

#adição de uma cada convolucional 2D
model.add(___(___, kernel_size=(__, ___), activation= '___',input_shape=data_train.shape[1:],padding='___'))

#adição de uma camada de redução maxpooling
model.__(___(pool_size=(__,__),____='___'))

#transformação dos dados em 1 dimensão
___.___(____)

#adição da camada densa (MLP)
__.__(___(__,___='___'))

#compilação do modelo
model.___(loss='___', optimizer='____',metrics=['sparse_categorical_accuracy'])

# treinamento do modelo
model.__(___, __, validation_data= (__, __), epochs=__)
