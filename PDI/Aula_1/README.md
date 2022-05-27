# Atividades de Sala
> Orientações para execução das atividades de sala.

Esse documento exibe as descrições das questões a serem resolvidas em sala

##  Aula 1

### Questão 1

```code1.py```

#### Convertendo a imagem para Tom de cinza

Neste primeiro exercício você deve realizar o processo de conversão de imagem em RGB
para ton de cinza.

#### Instruções:

1)  Importe os módulos `` color `` e `` data ``  da `` skimage ``.
   
2)  carregue a imagem `` rocket `` do módulo `` data ``

3)  Use a função `` rgb2gray`` do modulo `` color `` para converter a imagem para tom de cinza.
    
4) Mostre a imagem original com a função `` show_image``

5) Mostre a imagem convertida com a função `` show_image``

### Questão 2

```code2.py```

#### Manipulando imagens com  Numpy

Neste caso temos uma imagem que está  "de cabeça para baixo" originalmente. 
A proposta é utilizar a lib ``numpy`` para corrigir a imagem.

#### Instruções 

1) Utilizando a função ``show_image`` mostre a imagem original.
2) Faça um flip vertical na imagem com a função ``flipud`` da ``numpy``.
3) Mostre a imagem resultado da operaçao anterior.
4) Faça um flip horizontal na imagem com a função ``fliplr`` da ``numpy``..
5) Mostre a imagem resultado da operaçao anterior.

### Questão 3

```code3.py```

#### Histograma e Canais RGB

Neste exercicio você poderá acessar os canais individuais de uma imagem ``RGB`` e poderá também verificar
o histograma.

#### Instruções

1) Mostre a imagem original em RGB
2) Obtenha a matriz que representa o canal vermelho.
3) Mostre a matriz com a função ``show_image``
4) Determine o historama da matriz que representa o canal vermelho

### Questão 4

```code4.py```

#### Limiarização automática

Neste exercício você ira aplicar a limiarização de otsu para binarizar uma imagem.

#### Instruções

1) Importe a função para limiarização de Otsu.
2) Converta a imagem para tom de cinza.
3) Mostre a imagem convertida com a função ``show_image``
4) Calcule o limiar de Otsu.
5) Aplique o processo de limiarização da imagem.
6) Mostre a imagem binária.

### Questão 5

```code5.py```

#### Limiar global vs Limiar Local

 Em alguns tipos de imagens a definição de um único limiar na imagem completa pode 
 proporcionar perda de informações importantes para um processamento posterior. Neste caso, faz-se necessário
 limiarização por regiões da imagem.

#### Instruções
1) importe a limiarização de ostu e a limiarização local da ``skimage``.
2) Mostre a imagem em tom de cinza com a função ``show_image``.
3) Calcule o limiar local com a função de Otsu.
4) Aplique a limiarização.
5) Visualize o resultado da lmiarização global.
6) Estabeleça uma máscara de tamanho 35.
7) Calcule o limiar local.
8) Aplique a limiarização local
9) Visualize a limiarização local e compare


### Questão 6

```code6.py```

#### Testando vários limiares

Em determinados testes se faz necessário testar com várias técnicas de limiarização
para que possa observar a melhor opção para o processamento posterior.

#### Instruções
1) Importe a ``try_all_threshold`` da `skimage.filters`.
2) Importe a função para converter para tom de cinza a imagem em RGB.
3) Use a função ``try_all_threshold``na imagem em tom de cinza.
4) Visualize os testes.
