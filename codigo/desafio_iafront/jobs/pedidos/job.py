import os
import click
from datetime import timedelta

from desafio_iafront.data.dataframe_utils import read_csv, read_partitioned_json
from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.pedidos.contants import SAVING_PARTITIONS
from desafio_iafront.jobs.pedidos.utils import _prepare


@click.command()
@click.option('--pedidos', type=click.Path(exists=True))
@click.option('--visitas', type=click.Path(exists=True))
@click.option('--produtos', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
def main(pedidos, visitas, produtos, saida, data_inicial, data_final):
    produtos_df = read_csv(produtos)
    produtos_df["product_id"] = produtos_df["product_id"].astype(str)

    delta: timedelta = (data_final - data_inicial)
    date_partitions = [data_inicial.date() + timedelta(days=days) for days in range(delta.days)]

    for data in date_partitions:
        hour_partitions = list(range(0, 23))

        for hour in hour_partitions:
            hour_snnipet = f"hora={hour}"

            data_str = data.strftime('%Y-%m-%d')
            date_partition = f"data={data_str}"

            visitas_partition = os.path.join(visitas, date_partition, hour_snnipet)
            visitas_df = read_partitioned_json(visitas_partition)
            visitas_df["product_id"] = visitas_df["product_id"].astype(str)
            visitas_df["visit_id"] = visitas_df["visit_id"].astype(str)

            pedidos_partition = os.path.join(pedidos, date_partition, hour_snnipet)
            pedidos_df = read_partitioned_json(pedidos_partition)
            pedidos_df["visit_id"] = pedidos_df["visit_id"].astype(str)

            visita_com_produto_df = visitas_df.merge(produtos_df, how="inner", on="product_id", suffixes=("", "_off"))
            visita_com_produto_e_conversao_df = visita_com_produto_df.merge(pedidos_df, how="left",
                                                                            on="visit_id", suffixes=("", "_off"))

            visita_com_produto_e_conversao_df["data"] = data_str
            visita_com_produto_e_conversao_df["hora"] = hour

            prepared = _prepare(visita_com_produto_e_conversao_df)
            save_partitioned(prepared, saida, SAVING_PARTITIONS)
            print(f"Concluído para {date_partition} {hour}h")


if __name__ == '__main__':
    main()
