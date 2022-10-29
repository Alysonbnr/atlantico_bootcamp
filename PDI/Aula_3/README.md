# Atividades de Sala
> Orientações para execução das atividades de sala.

Esse documento exibe as descrições das questões a serem resolvidas em sala

##  Aula 3

### Questão 1

```code1.py```

#### predição entre letra X e K

Neste exemplo você irá classificar uma imagem binária em duas classes : Letra X e Letra K.
Você não possui uma rede neural treinada. Você possui um modelo simples que pode ser usado para classificar letras.
Para classificar vc precisará realizar uma multiplicação de matrizes (letra e modelo), depois somar os elementos da matriz resposta. 
Se a soma for 1, a letra é K, ser for 0, a letra é X.


Note that the functions reshape(), matmul(), and reduce_sum() have been imported from tensorflow and are available for use.

#### Instruções:

1)   Utilize a função  ``reshape ``  do módulo `` tensorflow``  em redimensione o modelo para 3x1.
   
2)   Utilize a função `` matmul `` do módulo `` tensorflow `` e multiplique a letra K pelo modelo

3)   Utilize a função `` reduce_sum `` do módulo  `` tensorflow`` para somar o resultado da multiplicação da letra K pelo modelo.
    
4)   Utilize a função `` matmul `` do módulo `` tensorflow `` e multiplique a letra x pelo modelo

5)   Utilize a função `` reduce_sum `` do módulo  `` tensorflow`` para somar o resultado da multiplicação da letra X pelo modelo.

### Questão 2

```code2.py```

#### A camada densa

O objetivo deste exercicício é criar uma camada densa.

#### Instruções 

1) Utilize a função `` Variable `` do módulo `` tensorflow `` para criar uma matriz de pesos unitários 3x2 e armazene em weights1.
2) Realize uma multimplicação de matrizes de features por weights1.
3) Aplique a ativação  ``sigmoide`` na soma de product1 + bias1, armazene em dense1.
4) Utilize a função `` Variable `` do módulo `` tensorflow `` para criar uma matriz de pesos unitários 2x1 e armazene em weights2.
5) Realize uma multimplicação de matrizes de dense1 por weights2.
6) Aplique a ativação  ``sigmoide`` na soma de product2 + bias2, armazene em prediction.

### Questão 3

```code3.py```

#### Criação da camada densa com API do Keras

Neste exemplo você irá criar uma camada densa, mas com API pronta do Keras.

#### Instruções

1) crie uma camada densa com 7 neurônios, função de ativação 'sigmoid'
2) crie uma camada densa com 3 neurônios, função de ativação 'sigmoid'
3) crie uma camada densa com 1 neurônios, função de ativação 'sigmoid'
5) mostre o shape das camadas.


### Questão 4

```code4.py```

#### Modelo sequencial do keras

Neste exercício você ira aplicar a equalização do histograma da imagem.

#### Instruções

1) Adicione uma camada densa com 16 neurônios com função de ativação ``relu`` .
2) Adicione uma segunda camada densa com 8 neurônios com função de ativação ``relu`` .
3) Adicione uma camada densa de predição com 4 neurônios com função de ativação ``softmax`` .



### Questão 5

```code5.py```

#### Modelo sequencial no keras com compilação simples

 criação de um modelo sequencial e compilação.

#### Instruções
1) Adicione uma camada densa com 16 neurônios com função de ativação ``relu``  e ``input_shape = (784,)`` 
2) Adicione uma camada dropout.
3) Adicione uma camada densa de predição com 4 neurônios com função de ativação ``softmax``  e input_shape de 784.
4) compile o modelo com 'adam' e considere 'categorical_crossentropy' como perda.