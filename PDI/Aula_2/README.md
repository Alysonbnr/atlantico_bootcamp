# Atividades de Sala
> Orientações para execução das atividades de sala.

Esse documento exibe as descrições das questões a serem resolvidas em sala

##  Aula 2

### Questão 1

```code1.py```

#### Limiarização automatica

Neste primeiro exercício você deve realizar o processo de binarização com a limiarização de Otsu

#### Instruções:

1)  Importe  ``threshold_otsu `` e  do módulo `` filters`` da `` skimage ``.
   
2)  Importe `` rgb2gray `` do módulo `` color `` da `` skimage ``

3)  Use a função `` rgb2gray`` do modulo `` color `` para converter a imagem para tom de cinza.
    
4) Calcule o limiar de otsu utilizadno a função `` threshold_otsu``

5) Realize a binarização da imagem verificando os pixels que são maiores que `` thresh``

### Questão 2

```code2.py```

#### FIltragem de alta frequencia

O objetivo deste exercicício é realcar as regiões de contorno dos objetos da imagem.

#### Instruções 

1) Importe `` rgb2gray `` do módulo `` color `` da `` skimage ``.
2) Importe  ``sobel `` e  do módulo `` filters`` da `` skimage ``.
3) Realce os contornos da imagem usando  a função ``sobel ``.
4) Mostre a imagem resultado e a imagem original.

### Questão 3

```code3.py```

#### Filtragem de baixa frequencia

Neste exercicio você deve diminuir a importância do contorno dos objetos da imagem.

#### Instruções

1) Utilize a função ``gaussian`` para filtrar a imagem ``building_image`` com sigma = 1
2) mostre a imagem original e o resultado.
3) Utilize a função ``gaussian`` para filtrar a imagem ``building_image`` com sigma = 5
4) mostre a imagem resultado.
5) Utilize a função ``gaussian`` para filtrar a imagem ``building_image`` com sigma = 10
6) mostre a imagem resultado.


### Questão 4

```code4.py```

#### Equalização de histograma

Neste exercício você ira aplicar a equalização do histograma da imagem.

#### Instruções

1) Importe o módulo ``exposure`` da ``skimage``.
2) Calcule o histograma da imagem ``chest_xray_image`` com a função``hist`` da ``matplotlib.pyplot`` . Informe o parâmetro bins = 255.
3) Com o modulo ``exposure`` use a função ``equalize_hist`` para equalizar o histograma da imagem.
4) Mostre a imagem equalizada.
5) Calcule e mostre o histograma equalizado.


### Questão 5

```code5.py```

#### Extração de atributos da imagem

 Vamos ver neste exercicio alguns atributos que podem ser extraídos da imagem, como média, variância e dados do histograma.

#### Instruções
1) Calcule e mostre o histograma da imagem original.
2) Equalize o histograma da imagem original.
3) Calcule o histograma da imagem equalizada e mostre.
4) Utilizando a função ``mean`` da ``numpy``, determine a média dos valores dos pixels da imagem original.
5) Utilizando a função ``mean`` da ``numpy``, determine a média dos valores dos pixels da imagem equalizada.
6) Utilizando a função ``var`` da ``numpy``, determine a variância dos valores dos pixels da imagem original.
7) Utilizando a função ``var`` da ``numpy``, determine a variância dos valores dos pixels da imagem equalizada
8) Determinar os pixels que ocorrem com frequência inferior a 20% da máxima frequência do histograma imagem original. A função ``max`` da ``numpy`` determina o maximo valor de um array.
9) Determinar os pixels que ocorrem com frequência inferior a 20% da máxima frequência do histograma imagem equalizada. A função ``max`` da ``numpy`` determina o maximo valor de um array. 
10) Determinar a média do valor dos pixels que ocorrem com baixa frequência da imagem não equalizada.
11) Determinar a media do valor dos pixels que ocorrem com baixa frequência da imagem equalizada.
12) Determinar a entropia do histograma da imagem original com a função ``compute_entropy``
13) Determinar a entropia do histograma da imagem equalizada com a função ``compute_entropy``
14) Mostre os números obtidos   