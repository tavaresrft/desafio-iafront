# Relatório para o Desafio iafront da B2WDigital.

### Autor: Romulo Ferreira Tavares, 31/08/2020

### Introdução

No relatório abordo como as transformações de escala e os métodos de clusterização podem afetar o processo de escolha.

Escolhi as duas primeiras primeiras semanas, de 01/06/2020 até 14/06/2020, para um departamento escolhido aleatoriamente utilizando a função 
__randint__ . O departamento escolhido para fazermos a análise foi o departamento __alimentos_bebidas__.

### Escalonamento dos dados.

Dados podem apresentar diversas características que podem ser indesejáveis quando vamos fazer uma análise detalhada dos dados. Por exemplo, podemos ter que lidar com dados que variam em diversas faixas de tamanho, dados que contenham diferentes unidades de uma mesma grandeza dentre outras. Para resolver esse problema podemos fazer um escalonamento nos dados.

Para fazer o escalonamento nos dados usei, como o sugerido, os métodos Normalizer,
StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler e PowerTransformer.
Como método de Clusterização escolhi os métodos KMeans, MiniBatchKMeans, Birch ,
AgglomerativeClustering e SpectralClustering.

O método __Normalizer__ faz uma transformação linear nos dados de uma amostrana qual a soma das variáveis ao quadrado, norma euclidiana, para uma amostra é igual a 1,
x_i'=x_i/\sum x_i^2.
 A figura1 e a figura2 mostram como a variável preço se comporta na primeira e segunda semanas, respectivamente.

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_Normalizer.html "figura1")

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_Normalizer.html "figura2")

Podemos notar que do ponto de vista dos preços brutos, quase não há diferença na distribuição, porém após a transformação há uma diferença mais notável, indicando que outras variáveis tiveram maior mudança entre as semanas estudadas. Vemos também
que dentro da variável preço a transformação é não linear, já que a linearidade se mantém dentro da amostras e não dentro da variável como um todo.

O método __StandardScaler__ faz uma transformação linear na variável estudada.
A variável escalonada é tal que sua média é nula e seu desvio padrão é igual a um.
Para fazer essa transformação podemos fazer,
x_i'=(x_i-m)/std,
onde m é a média do conjunto original e std, seu desvio padrão.
A figura3 e a figura4 mostram os resultados da transformação StandardScaler
para a primeira e segunda semana consideradas, respectivamente.

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_StandardScaler.html "figura3")

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_StandardScaler.html "figura4")

Notamos também que não grande diferença entre as duas semanas. Já que o comportamento dos preços quase não mudou, é previsível que uma transformação linear não causaria grandes mudanças no comportamento dos dados escalonadas.

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_StandardScaler.html "figura3")

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_StandardScaler.html "figura4")

O método __MinMaxScaler__ escalona os dados levando em consideração os valores
máximos e mínimos de uma variável em um conjunto de dados através da equação,
x_i' = x_{std}(max(X) - min(X)) + min(X)
x_{std}=(x_i - min(X)) / (max(X) - min(X)).

Novamente a transformação é linear para a variável em questão, como podemos ver na figura5 e a figura6. Assim como na transformação anterior, os valores escalonados não sofrem grandes alterações de uma semana para outra

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_MinMaxScaler.html "figura5")

![Alt text](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_MinMaxScaler.html "figura6")
