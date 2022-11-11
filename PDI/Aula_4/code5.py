
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint,ReduceLROnPlateau,TensorBoard
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
from PDI.src.pdi_utils import load_sign_language_data

#função para salvar sumario
def save_sumary(name):

    with open('sumary/'+name +'.txt', 'w') as f:
        model.summary(print_fn=lambda x: f.write(x + '\n'))

#função para definir callbacks
def callbacks(model_name):

    tensorboard = TensorBoard(log_dir="logs/{}".format(model_name))
    mcp_save = ModelCheckpoint(model_file ,save_best_only=True, monitor='val_loss', mode='min')
    earlyStopping = EarlyStopping(monitor='val_loss', patience=2, verbose=1, mode='min')
    reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.05, patience=2, verbose=1,min_delta=1e-4,mode='min')
    return tensorboard,mcp_save,earlyStopping,reduce_lr_loss


#carregando informaçoes do dataset
data_train , label_train , data_val , label_val, _ , _  = load_sign_language_data()

#definição da quantidade de filtros em cada camada convolucional
conv_node=[__,__,__,__,]

#definição da quantidade de neuronios da ultima camada
output = __

#definição da quantidade de filtros da primeira camada
first_node = __

#iteração para determinar as variações de cnn
for cnn in  range(len(conv_node)):

    #inicialização do modelo sequencial do keras
    __=__

    #adição da primeira camada convolucional
    _____

    #adição da camada de redução maxpooling
    ___

    #adição da camada dropout para eliminar 25% de dados aleatórios do treinamento
    model.add(___)

    #iteração para criar blocos adicionais de caamdas convolucionais.
    for node in conv_node[:cnn]:
        #adição de camada convolucional
        ____

        #adição de camada de redução maxpooling
        ____

    #transormaçao dos dados em 1 dimensão
    ____

    #adição da camada de densa de saída
    ____

    #compilação do modelo
    ___

    #definição do nome do modelo salvo em arquivo
    model_file = 'models/{}-block-{}-convNode.h5'.format(cnn,conv_node[:cnn])

    #nome do log que será analisado pelo tensorboard
    model_name = "{}-block-{}-convNOde".format(cnn,conv_node[:cnn])

    #definição dos callbacks
    tensorboard,mcp_save,earlyStopping,reduce_lr_loss = callbacks(___)

    #salvando sumario dos modelos
    save_sumary(___)

    #treinando modelo
    ____
