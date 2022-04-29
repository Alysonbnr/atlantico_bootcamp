# Atividades de Sala
> Orientações para execução das atividades de sala.

Esse documento exibe as descrições das questões a serem resolvidas em sala

##  Aula 1

### Questão 1

```code1.py```

#### Praticando expressões regulares: re.split() e re.findall()

Agora você terá a chance de escrever algumas expressões regulares para combinar dígitos, strings e caracteres não alfanuméricos. Dê uma olhada em ``my_string`` primeiro imprimindo-a, para determinar como você pode combinar melhor as diferentes etapas.

Observação: é importante prefixar seus padrões regex com ``r`` para garantir que seus padrões sejam interpretados da maneira que você deseja. Caso contrário, você pode encontrar problemas relacionados a sequências de escape em strings. Por exemplo, ``"\n"`` em Python é usado para indicar uma nova linha, mas se você usar o prefixo ``r``, ele será interpretado como a string bruta ``"\n"`` - ou seja, o caractere ``"\"`` seguido pelo caractere ``"n"`` - e não como uma nova linha.

O módulo de expressão regular ``re`` já foi importado para você.

Lembre-se que a sintaxe da biblioteca ``regex`` é sempre passar primeiro o padrão e depois a string.

#### Instruções:

1) Divida ``my_string`` em cada final de frase. Para fazer isso:
Escreva um padrão chamado ``sentence_endings`` para corresponder às terminações de sentença ``.?!``.
   
2) Use ``re.split()`` para dividir ``my_string`` no padrão e imprimir o resultado.

3) Encontre e imprima todas as palavras em maiúsculas em ``my_string`` escrevendo um padrão chamado ``capitalized_words``, usando ``re.findall()``.
Você se lembra do padrão ``[a-z]`` mostrado para corresponder aos grupos de letras minúsculas?  Modifique esse padrão adequadamente para corresponder aos grupos de letras maiúsculas.
   
3) Escreva um padrão chamado ``spaces`` para corresponder a um ou mais espaços ``"\s+"`` e então use ``re.split()`` para dividir ``my_string`` neste padrão, mantendo toda a pontuação intacta. Imprima o resultado.

4) Encontre todos os dígitos em ``my_string`` escrevendo um padrão chamado digits ``"\d+"`` e usando ``re.findall()``. Imprima o resultado.

### Questão 2

```code2.py```

####Tokenização com NLTK

Aqui, você usará a primeira cena do Santo Graal do Monty Python, que foi pré-carregada como ``scene_one``. Sinta-se à vontade para conferir.

Seu trabalho neste exercício é utilizar ``word_tokenize`` e ``sent_tokenize`` da ``nltk.tokenize`` para tokenizar palavras e sentenças. Neste caso, a primeira cena do Santo Graal do Monty Python.

#### Instruções 

1) Importe as funções ``sent_tokenize`` e ``word_tokenize`` de ``nltk.tokenize``.
2) Tokenize todas as frases em ```scene_one``` usando a função ````sent_tokenize()``.
3) Tokenize a quarta sentença em ``sentences``, que você pode acessar como ``sentences[3]``, usando a função ``word_tokenize()``.
4) Encontre os tokens exclusivos em toda a cena usando ``word_tokenize()`` em ``scene_one`` e, em seguida, convertendo-os em um conjunto usando ``set()``.
5) Imprima os tokens exclusivos encontrados. 

### Questão 3

```code3.py```

#### Mais regex com re.search()

Neste exercício, você utilizará ``re.search()`` e ``re.match()`` para encontrar tokens específicos. Tanto a pesquisa quanto a correspondência esperam padrões regex, semelhantes aos que você definiu em exercício anterior. Você aplicará esses métodos de biblioteca ``regex`` ao mesmo texto Monty Python.

Você tem ``scene_one`` disponível.

#### Instruções

1) Use ``re.search()`` para procurar a primeira ocorrência da palavra ``"coconuts"`` em scene_one. Armazene o resultado em match.
2) Imprima os índices inicial e final da correspondência usando seus métodos ```.start()``` e ```.end()```, respectivamente.
3) Escreva uma expressão regular chamada ``pattern1`` para encontrar qualquer coisa entre colchetes.
4) Use ``re.search()`` com o padrão para encontrar o primeiro texto entre colchetes em ``scene_one`` . Imprima o resultado.
5) Crie um padrão para corresponder à notação que indica a ação de um personagem por exemplo, ``Fulano:``, atribuindo o resultado a ``pattern2``. Lembre-se que você vai poder combinar quaisquer palavras ou espaços que precedem o ``:``.
6) Use ``re.match()`` com seu novo padrão para localizar e imprimir o padrão encontrado na quarta sentença de ``sentences``.

### Questão 4

```code4.py```

#### Regex com tokenização na NLTK

O Twitter é uma fonte frequentemente usada para texto e tarefas de NLP. Neste exercício, você construirá um tokenizer mais complexo para tweets com hashtags e menções usando nltk e regex. A classe ``nltk.tokenize.TweetTokenizer`` fornece alguns métodos e atributos extras para analisar tweets.

Aqui, você recebe alguns tweets de exemplo para analisar usando ``TweetTokenizer`` e ``regexp_tokenize`` do módulo ``nltk.tokenize``. Esses tweets de exemplo foram pré-carregados nos tweets variáveis. Sinta-se à vontade para explorá-los!

Ao contrário da sintaxe da biblioteca ``regex``, com ``nltk_tokenize()`` você passa o padrão como segundo argumento.

#### Instruções

1) De ``nltk.tokenize``, importe ``regexp_tokenize`` e ``TweetTokenizer``.
2) Um padrão regex para encontrar hashtags chamado ``pattern1`` foi definido para você. Chame ``regexp_tokenize()`` com este padrão de hashtag no primeiro tweet de ``tweets`` e atribua o resultado à  ``hashtags``.
3) printe hashtags.
4) Escreva um novo padrão chamado ``pattern2`` para combinar menções e hashtags. Uma menção é algo como @bootcamp.
5) Em seguida, chame ``regexp_tokenize()`` com seu novo padrão de hashtag no último tweet de ``tweets`` e atribua o resultado a ``mentions_hashtags``. Você pode acessar o último elemento de uma lista usando -1 como índice, por exemplo, ``tweets[-1]``.
6) Imprima ``mentions_hashtags``.
7) Crie uma instância de ``TweetTokenizer`` chamada ``tknzr`` e use-a dentro de uma compreensão de lista para tokenizar cada tweet em uma nova lista chamada ``all_tokens``.
   Para fazer isso, use o método ```.tokenize()``` de tknzr, com ``t`` como sua variável iteradora.
8) Imprima all_tokens.


### Questão 5

```code5.py```

#### Prática de gráficos

Tente usar suas novas habilidades para encontrar e traçar o número de palavras usando matplotlib. O script do Santo Graal é carregado para você e você precisa usar regex para encontrar as palavras por linha.

Usar compreensões de lista aqui acelerará seus cálculos. Por exemplo: ``my_lines = [tokenize(l) for l in lines]`` chamará uma função ``tokenize`` em cada ``l`` em ``lines``. A nova lista transformada será salva na variável ``my_lines``.

#### Instruções

1) Divida o script ``holy_grail`` em linhas usando o comando ``'\n'``.
2) Use ``re.sub()`` dentro de uma compreensão de lista para substituir as strings como ARTHUR: e SOLDIER #1 por`` ''``. O padrão foi escrito para você.
3) Use uma compreensão de lista para tokenizar ``lines`` com ``regexp_tokenize()``, mantendo apenas palavras. Lembre-se de que o padrão para palavras é ``"\w+"``.
4) Use uma compreensão de lista para criar uma lista de comprimentos de linha chamada ``line_num_words``.
5) Use ``t_line`` como sua variável iteradora para iterar sobre ``tokenized_lines`` e, em seguida, a função ``len()`` para calcular o tamanho da linha.
6) Trace um histograma de ``line_num_words`` usando ``plt.hist()``. Não se esqueça de usar ``plt.show()`` também para exibir o gráfico.

