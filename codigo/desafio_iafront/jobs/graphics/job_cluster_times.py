import click
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.palettes import Category20
from bokeh.plotting import figure

from desafio_iafront.data.dataframe_utils import read_partitioned_json,read_data_partitions
from desafio_iafront.jobs.common import filter_date
from functools import partial

@click.command()
@click.option('--data-path', type=click.Path(exists=True))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--file_output_name')

def main(data_path: str, data_inicial , data_final, file_output_name : str):
    
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(data_path, filter_function=filter_function)

    dataframe = dataframe.drop_duplicates().reset_index().drop('index',axis=1)
    ranged=sorted(list(dataframe['data'].unique()))
    clusters = list(dataframe['cluster_label'].unique())

    p = figure(title='Desempenho dos Clusters no tempo',x_range=ranged)
    p.xaxis.major_label_orientation = "vertical"
    p.yaxis.axis_label = 'Taxa de conversão'
    p.xaxis.axis_label = 'Data'

    colors=Category20[len(clusters)]
    n=0

    for cluster in clusters:
        df_plot = dataframe[dataframe['cluster_label']==cluster]  
        df_plot = df_plot.sort_values(by='data')
        p.line(x=ranged, y=list(df_plot['convertido']), line_width=2, color=colors[n], legend_label='cluster = '+str(cluster))
        n=n+1

    output_file(str(file_output_name)+".html" )
    show(p)

if __name__ == '__main__':
    main()
