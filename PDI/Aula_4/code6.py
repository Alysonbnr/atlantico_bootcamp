from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from PDI.src.pdi_utils import load_sign_language_data ,show_image
from matplotlib import pyplot


def plot_filter(n_filters,ix,filters):
    for i in range(n_filters):
        # selecionando o filtro
        f = filters[:, :, :, i]
        # plot de cada canal do filtro

        for j in range(3):
            # especificando subplot
            ax = pyplot.subplot(n_filters, 3, ix)
            ax.set_xticks([])
            ax.set_yticks([])
            pyplot.imshow(f[:, :, j], cmap='gray')
            ix += 1
            # show the figure
    pyplot.show()

def show_features(feature_maps):
    pyplot.imshow(feature_maps[0, :, :], cmap='gray')
    pyplot.show()


#carregando informações do dataset
data_train , label_train , data_val , label_val, data_test , label_test = load_sign_language_data()

#Carregando modelo salvo em diretório
model = ___('___.h5')

#obtendo filtros de pesos e bias da primeira cada
filters, biases = model.___[__].get_weights()

#normalização dos valores dos filtros para poder visualizar em forma e imagem
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

# plotar os 6 primeiros filtros
n_filters, ix = 6, 1
plot_filter(n_filters,ix,filters)

#inicialização do modelo com saída na ultima camada convolucional
model = Model(inputs=model.inputs, outputs=model.____[__].output)

#extraindo atributos com predict
features = model.predict(____)

#separando em feature_maps somente uma imagem do dataset
feature_maps = _____

#exibindo imagem original
show_image(____)

#exibindo imagem com extração de atributos
show_features(____)