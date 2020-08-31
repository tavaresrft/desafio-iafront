import click
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from functools import partial

from desafio_iafront.jobs.graphics.utils import compare_plot,hist_plot,scaled_hist_plot
from desafio_iafront.data.dataframe_utils import read_partitioned_json,read_data_partitions
from desafio_iafront.jobs.common import filter_date


@click.command()
@click.option('--data-path', type=click.Path(exists=True))
@click.option('--x_axis')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--file_output_name')
@click.option('--transformation')
def main(data_path: str, x_axis:str, data_inicial , data_final, file_output_name : str, transformation: str):

    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)

    dataframe = read_partitioned_json(file_path=data_path, filter_function=filter_function)
    
    scatter=compare_plot(dataframe, x_axis, x_axis+": valores brutos x transformados pelo metodo "+transformation)
    hist_antes=hist_plot(dataframe, x_axis, title='valores brutos de '+x_axis)
    hist_depois=scaled_hist_plot(dataframe, x_axis, title='valores de '+x_axis+' transformados pela '+transformation)

    output_file(str(file_output_name)+x_axis+"_"+transformation+".html" )

    show(gridplot([[scatter,hist_antes,hist_depois]]))

if __name__ == '__main__':
    main()
