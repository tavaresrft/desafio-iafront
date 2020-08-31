
explain:
	@echo "prepara"
	@echo "    Prepara os dados a partir dos arquivos contidos nas pastas pedidos e visitas e o produtos.csv."
	@echo "transform"
	@echo "    Faz o escalonamento dos dados. Podem ser escolhidos os métodos:"
	@echo "    normalizer, standardscaler, minmaxscaler, maxabsscaler, robustscaler, powertransformer"
	@echo "plot_semana1"
	@echo "    Faz o plot de como os dados se transformam na primeira semana."
	@echo "plot_semana2"
	@echo "    Faz o plot de como os dados se transformam na segunda semana."
	@echo "clustering"
	@echo "    Faz a clusterização dos dados. Podem ser escolhido os métodos:"
	@echo "    kmeans, mbk, birch, agglomerativeclustering e spectralclustering."
	@echo "converting"
	@echo "    Calcula o percentual de conversões por dia e por cluster."
	@echo "time_plot"
	@echo "    Faz o plot do percentual de conversão de cada cluster no tempo."
	@echo "total_conversion"
	@echo "    Faz o plot do percentual de conversão de cada cluster levando em conta a data inicial e final."
	@echo "plot_cluster"
	@echo "    Mostra como as variáveis preço, prazo, frete, latitude e longitude foram clusterizadas."

install:
	pip3 install -e .


prepara:
	prepara_pedidos \
	--pedidos='desafio_iafront/dataset-desafio-ia-front-master/pedidos' \
	--visitas='desafio_iafront/dataset-desafio-ia-front-master/visitas' \
	--produtos='desafio_iafront/dataset-desafio-ia-front-master/produtos.csv' \
	--saida='saida' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020'

transform:
	normalizer \
	--visitas-com-conversao='saida' \
	--saida='saida_scaled' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020' \
	--departamentos='alimentos_bebidas'

plot_semana1:
	plotcompare \
	--data-path='saida_scaled' \
	--x_axis='prazo' \
	--data-inicial='01/06/2020' \
	--data-final='08/06/2020' \
	--file_output_name='plot_semana1' \
	--transformation='Normalizer'

plot_semana2:
	plotcompare \
	--data-path='saida_scaled' \
	--x_axis='prazo' \
	--data-inicial='08/06/2020' \
	--data-final='15/06/2020' \
	--file_output_name='plot_semana2' \
	--transformation='Normalizer'


clustering:
	kmeans \
	--dataset='saida_scaled' \
	--number_of_cluster=4 \
	--saida='saida_cluster' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020'

converting:
	convert \
	--data-path='saida_cluster' \
	--saida='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020'

time_plot:
	plotclustertime \
	--data-path='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020' \
	--file_output_name='plot_conversion_time'

total_conversion:
	plotconversion \
	--data-path='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020' \
	--file_output_name='plot_total_conversion'

plot_cluster:
	plottotalcluster \
	--data-path 'saida_cluster' \
	--data-inicial='01/06/2020' \
	--data-final='02/06/2020' \
	--file_output_name='plot_scatter_cluster'
run:
	prepara_pedidos \
	--pedidos='desafio_iafront/dataset-desafio-ia-front-master/pedidos' \
	--visitas='desafio_iafront/dataset-desafio-ia-front-master/visitas' \
	--produtos='desafio_iafront/dataset-desafio-ia-front-master/produtos.csv' \
	--saida='saida' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020'
	normalizer \
	--visitas-com-conversao='saida' \
	--saida='saida_scaled' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020' \
	--departamentos='alimentos_bebidas'
	plotcompare \
	--data-path='saida_scaled' \
	--x_axis='prazo' \
	--data-inicial='01/06/2020' \
	--data-final='08/06/2020' \
	--file_output_name='plot_semana1' \
	--transformation='Normalizer'
	plotcompare \
	--data-path='saida_scaled' \
	--x_axis='prazo' \
	--data-inicial='08/06/2020' \
	--data-final='15/06/2020' \
	--file_output_name='plot_semana2' \
	--transformation='Normalizer'
	kmeans \
	--dataset='saida_scaled' \
	--number_of_cluster=4 \
	--saida='saida_cluster' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020'
	convert \
	--data-path='saida_cluster' \
	--saida='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020'
	plotclustertime \
	--data-path='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020' \
	--file_output_name='plot_conversion_time'
	plotconversion \
	--data-path='saida_converted' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020' \
	--file_output_name='plot_total_conversion'
	plottotalcluster \
	--data-path 'saida_cluster' \
	--data-inicial='01/06/2020' \
	--data-final='15/06/2020' \
	--file_output_name='plot_scatter_cluster'

