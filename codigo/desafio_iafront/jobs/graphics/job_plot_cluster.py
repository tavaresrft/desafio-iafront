import click
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.palettes import Category20
from bokeh.plotting import figure

#from desafio_iafront.jobs.graphics.utils import compare_plot,hist_plot,scaled_hist_plot
from desafio_iafront.data.dataframe_utils import read_partitioned_json,read_data_partitions
from desafio_iafront.jobs.common import filter_date
from functools import partial

@click.command()
@click.option('--data-path')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--file_output_name')

def main(data_path: str, data_inicial , data_final, file_output_name : str):
    
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(data_path, filter_function=filter_function)

    x1=list(dataframe['longitude'])
    y1=list(dataframe['latitude'])
    preco=list(dataframe['preco'])
    prazo=list(dataframe['prazo'])
    frete=list(dataframe['frete'])

    clusters = list(dataframe['cluster_label'].unique())
    colors=Category20[len(clusters)]
    cores = [colors[x] for x in dataframe['cluster_label']]

    p1 = figure(title='Mapa_Cluster')
    p1.xaxis.axis_label = 'longitude'
    p1.yaxis.axis_label = 'latitude'
    p1.circle(x=x1,y=y1,size=10,color=cores)

    p2 = figure(title='Preco x Prazo Cluster')
    p2.xaxis.axis_label = 'preco'
    p2.yaxis.axis_label = 'prazo'
    p2.circle(x=preco,y=prazo,size=10,color=cores)

    p3 = figure(title='Preco x Frete Cluster')
    p3.xaxis.axis_label = 'preco'
    p3.yaxis.axis_label = 'frete'
    p3.circle(x=preco,y=frete,size=10,color=cores)

    p4 = figure(title='Frete x Prazo Cluster')
    p4.xaxis.axis_label = 'frete'
    p4.yaxis.axis_label = 'prazo'
    p4.circle(x=frete,y=prazo,size=10,color=cores)

    output_file(str(file_output_name)+".html" )
    show(gridplot([[p1,p2],[p3,p4]]))

if __name__ == '__main__':
    main()
