import os
import click
from datetime import timedelta
import shutil

from desafio_iafront.data.dataframe_utils import read_csv, read_partitioned_json
from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.pedidos.contants import SAVING_PARTITIONS
from desafio_iafront.jobs.pedidos.utils import _prepare,remove_na_df,method_name


#@click.command()
#@click.option('--pedidos', type=click.Path(exists=True))
#@click.option('--visitas', type=click.Path(exists=True))
#@click.option('--produtos', type=click.Path(exists=True))
#@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
#@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
#@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
def main(pedidos, visitas, produtos, saida, data_inicial, data_final):
    
        # Evita que dados antigos permaneçam
    if os.path.exists(saida) == True:
        shutil.rmtree(saida)
    
    produtos_df = read_csv(produtos)
    produtos_df["product_id"] = produtos_df["product_id"].astype(str)
    produtos_df = remove_na_df(produtos_df)

    delta: timedelta = (data_final - data_inicial)
    date_partitions = [data_inicial.date() + timedelta(days=days) for days in range(delta.days)]

    for data in date_partitions:
        hour_partitions = list(range(0, 24))

        for hour in hour_partitions:
            method_name(data, hour, pedidos, produtos_df, saida, visitas)
            print(f"Concluído para {data} {hour}h")


if __name__ == '__main__':
    main()
