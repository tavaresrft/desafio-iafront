# Relatório para o Desafio iafront da B2WDigital.

### Autor: Romulo Ferreira Tavares, 31/08/2020

### Introdução

No relatório abordo como as transformações de escala e os métodos de clusterização podem afetar o processo de escolha.

Escolhi as duas primeiras primeiras semanas, de 01/06/2020 até 14/06/2020, para um departamento escolhido aleatoriamente utilizando a função __randint__, que teve como resultado o departamento __alimentos_bebidas__. Escolhi a coluna __prazo__ para fazer as análises, pois foi a que apresentou o menor quociente entre a média e o desvio padrão q,
q = mean(x)/std(x).

### Escalonamento dos dados.

Dados podem apresentar diversas características que podem ser indesejáveis quando vamos fazer uma análise detalhada. Por exemplo, podemos ter que lidar com dados que variam em diversas faixas de tamanho, dados que contenham diferentes unidades de uma mesma grandeza, dentre outras. Para resolver esse problema podemos fazer um escalonamento nos dados.

Para fazer o escalonamento usei, como o sugerido, os métodos Normalizer,
StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler e PowerTransformer.
Como métodos de Clusterização escolhi, KMeans, MiniBatchKMeans, Birch,
AgglomerativeClustering e SpectralClustering.

O método __Normalizer__ faz uma transformação linear nos dados de uma amostra no qual a soma das variáveis ao quadrado ou norma euclidiana, para cada amostra é igual a 1,
x_i'=x_i/\sum_j x_j^2.
 A figura1 e a figura2 mostram como a variável preço se comporta na primeira e segunda semanas, respectivamente.

![figura1](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_prazo_Normalizer.html "figura1") e ![figura2](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_prazo_Normalizer.html "figura2")

Podemos notar que do ponto de vista dos prazos brutos, há pouca diferença nas distribuições para as semanas escolhidas, porém após a transformação há uma grande diferença na distribuição entre os valores. Antes da transformação a frequência dos dados se distribuem mais uniformemente pelos valores, já após a transformação Normalizer há uma maior distribuição para valores menores da transformação. Vemos também
que dentro da variável prazo a transformação é não linear, pois a linearidade se mantém dentro das variáveis das amostras e não dentro da variável como um todo.

O método __StandardScaler__ faz uma transformação linear nas variáveis como um todo.
A variável escalonada é de tal forma que sua média é nula e seu desvio padrão é igual a um.
Para fazer essa transformação podemos fazer,
x_i'=(x_i-m)/std,
onde m é a média do conjunto original e std, seu desvio padrão.
A figura3 e a figura4 mostram os resultados da transformação StandardScaler
para a primeira e segunda semana consideradas, respectivamente.

![figura3](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_prazo_StandardScaler.html "figura3") e ![figura4](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_prazo_StandardScaler.html "figura4")

Notamos também que não há grande diferença entre as distribuições das duas semanas, já que a transformação linear não causa mudanças no comportamento dos dados escalonados.

O método __MinMaxScaler__ escalona os dados levando em consideração os valores
máximos e mínimos de uma variável em um conjunto de dados através da equação,
x_i' = x_{std}(max(X) - min(X)) + min(X)
x_{std}=(x_i - min(X)) / (max(X) - min(X)).

Novamente a transformação é linear para a variável em questão, como podemos ver na figura5 e a figura6. Assim como na transformação anterior, os valores escalonados não sofrem grandes alterações de uma semana para outra.

![figura5](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_MinMaxScaler.html "figura5") e ![figura6](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_preco_MinMaxScaler.html "figura6")

O método __MaxAbsScaler__ transforma os dados da seguinte maneira,
x_i'=x_i/max(abs(X)).
Dessa maneira os dados podem ficar escalonados entre -1 e 1 e essa transformação é linear na variável. A figura7 e a figura8 mostram como se dá a transformação.

![figura7](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_MaxAbsScaler.html "figura7") e ![figura8](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_preco_MaxAbsScaler.html "figura8")

Como a distribuição dos preços não sofreu muita alteração entre as semanas e o escalonamento MinMaxScaler faz transformações lineares, não houve uma mudança significativa entre as semanas para os dados escalonadas.

O método __RobustScaler__ leva em conta a mediana (med) e os quartis (Q) maior e menor através da equação,
x_i = (x_i'-med(X))/(Q75%-Q25%). Essa transformação também é linear e não altera a distribuição dos dados,
porém essa transformação é menos suscetível a outliers, caso existam no conjunto.
A figura9 e a figura10 mostram as mudanças desse escalonamento,

![figura9](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_RobustScaler.html "figura9") e ![figura10](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_preco_RobustScaler.html "figura10").

O método __PowerTransformer__ faz com que uma distribuição de dados se torne mais gaussiana, portanto essa transformação
é não linear nos dados. A figura11 e a figura12 mostram como os dados se transformam 
![figura11](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana1_preco_PowerTransformer.html "figura11") e ![figura12](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/plot_semana2_preco_PowerTransformer.html "figura12").

### Clusterização

Para fazer a clusterização dos dados escolhi os métodos KMeans, Mini-Batch-KMeans, BIRCH, AgglomerativeClustering e SpectralClustering.
Tive problemas para usar os métodos AgglomerativeClustering e SpectralClustering por falta de memória mesmo tentando reduzir a dimensionalidade dos dados através da Análise de Componentes Principais (PCA).

Notei que a clusterização depende mais do método de transformação dos dados que do método de clusterização. Os dados transformados pelo método Normalizer ficou bem clara a separação dos clusters entre as variáveis preço e frete como mostra a ![figura13](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/preco_frete_cluster.html "figura 13"). Os dados transformados pelo método RobustScaler ficaram clusterizados pelo mapa geográfico como mostra a ![figura14](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/mapa_robust_scaler.html "figura 14").

Portanto utilizei o método KMeans para clusterizar os dados de acordo com as transformações acima e fiz as interpretações dos gráficos de conversão no tempo. Pela normalização podemos ver que pela ![figura15](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/desempenho_normalizer.html "figura 15") o cluster 3 teve o melhor desempenho, porém muito próximo aos outros.
 Podemos separar os clusters de acordo com o ângulo que o eixo frete (y) faz com o eixo preço (x) de acordo com a ![figura13](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/preco_frete_cluster.html "figura 13"). O cluster 3 é o cluster onde o preço tende a ser mais relevante que o frete, porém essa relevância não é tão grande como no cluster 1, onde o ângulo é menor ainda. Já o cluster 0 teve o pior desempenho, e é o cluster onde o frete tem mais relevância que o preço. Esse resultado é esperado já que nesse clusters os consumidores
tendem a acreditar que estão pagando mais para a transportadora levar o produto do que pelo produto em si.

Utilizando o KMeans para os dados transformados pelo RobustScaler temos como a conversão se dá por regiões geográficas. De acordo com a ![figura16](https://github.com/tavaresrft/desafio-iafront/blob/master/codigo/desempenho_robust_scaler.html "figura16") o cluster de melhor desempenho é o cluster 1, onde aparantemente, representa uma região mais central do país enquanto que o cluster 3 foi o de pior desempenho e aparentemente representa a região do país.

Pelos dados obtidos através da transformação Normalizer, o cluster com fretes altos para preços baixos tem um mal desempenho em relação aos outros. Investimentos em setores que minimizem os custos da entrega podem influenciar positivamente a conversão de visitas em compras.

Dentro da semana estudada não houve uma variação significativa na conversão dos dados





