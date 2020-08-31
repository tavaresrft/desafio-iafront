import click
from bokeh.io import output_file, save, show
from bokeh.layouts import gridplot
from bokeh.palettes import Category20
from bokeh.plotting import figure

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from bokeh.plotting import figure, output_file, save
import plotly
from bokeh.io import output_file,show, output_notebook
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource

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
    dataframe = dataframe.groupby(["cluster_label"]).convertido.mean().reset_index()

    xis = list(dataframe['cluster_label'])
    right = list(dataframe['convertido'])
    for i in range(len(xis)):
        xis[i]='cluster_' + str(xis[i])
    for i in range(len(right)):
        right[i]=right[i]*100.0

    data = {'clusters':xis,'percentual_conversao':right}

    p= figure(y_range=xis,title='Percentual de conversão',tools="hover")
    p.hbar(right='percentual_conversao',y='clusters',height=0.8,color='green',source=data)
    p.yaxis.axis_label = 'Cluster'
    p.xaxis.axis_label = 'Percentual de conversão'
    p.hover.tooltips = [('Percentual de conversão',"@percentual_conversao""%")]
    show(p)

if __name__ == '__main__':
    main()
