import click
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot

from desafio_iafront.jobs.graphics.utils import scaled_scatter_plot, scatter_plot
from desafio_iafront.data.dataframe_utils import read_partitioned_json,read_data_partitions



@click.command()
@click.option('--data-path', type=click.Path(exists=True))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--file_output_name')
@click.option('--transformation'))

def main(data_path: str,data_inicial , data_final, file_output_name : str, transformation: str):
    
    dataframe = read_data_partitions(data_inicial,data_final, data_path)
    figura_transformed=scaled_scatter_plot(dataframe, 'longitude', 'latitude', title="mapa transformado pelo metodo "+transformation)
    figura = scatter_plot(dataframe, 'longitude', 'latitude', title="mapa normal") 
    
    output_file(str(file_output_name)+"mapas.html" )
    print('Saving graph') 
    show(gridplot([[figura,figura_transformed]]))

if __name__ == '__main__':
    main
