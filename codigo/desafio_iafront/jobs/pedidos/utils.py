import pandas as pd
import os

from desafio_iafront.jobs.pedidos.contants import KEPT_COLUNS, COLUMN_RENAMES
from desafio_iafront.data.dataframe_utils import read_csv, read_partitioned_json
from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.pedidos.contants import SAVING_PARTITIONS
#from desafio_iafront.jobs.pedidos.utils import _prepare


def _prepare(pedidos_joined: pd.DataFrame) -> pd.DataFrame:
    # Remove colunas resultantes do merge
    result_dataset = drop_merged_columns(pedidos_joined)
    # Remove colunas que não serão usadas
    result_dataset = result_dataset[KEPT_COLUNS]
    # Renomeia colunas
    result_dataset = result_dataset.rename(columns=COLUMN_RENAMES)

    return result_dataset


def drop_merged_columns(data_frame: pd.DataFrame) -> pd.DataFrame:
    result_dataset = data_frame.copy(deep=True)
    for column in data_frame.columns:
        if column.endswith("_off"):
            result_dataset = data_frame.drop(column, axis=1)
    return result_dataset

   #create_pedidos_df faz praticamente a mesma coisa, então não vi necessidade de criar uma função a mais
def create_visitas_df(date_partition: str, hour_snnipet: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    df_partition = os.path.join(dataframe, date_partition, hour_snnipet)
    df = read_partitioned_json(df_partition)
    df["product_id"] = df["product_id"].astype(str)
    df["visit_id"] = df["visit_id"].astype(str)
    return df

def merge_visita_produto(data_str: str, hour: int, pedidos_df: pd.DataFrame, produtos_df: pd.DataFrame, visitas_df: pd.DataFrame) -> pd.DataFrame:
    visita_com_produto_df = visitas_df.merge(produtos_df, how="inner", on="product_id", suffixes=("", "_off"))
    visita_com_produto_e_conversao_df = visita_com_produto_df.merge(pedidos_df, how="left",on="visit_id", suffixes=("", "_off"))
    visita_com_produto_e_conversao_df["data"] = data_str
    visita_com_produto_e_conversao_df["hora"] = hour
    return visita_com_produto_e_conversao_df

def save_prepared(saida: str, visita_com_produto_e_conversao_df: pd.DataFrame):
    prepared = _prepare(visita_com_produto_e_conversao_df)
    save_partitioned(prepared, saida, SAVING_PARTITIONS)

def method_name(data: str, hour: int, pedidos: str, produtos_df: pd.DataFrame, saida: str, visitas: str) -> pd.DataFrame:
    hour_snnipet = f"hora={hour}"
    data_str = data.strftime('%Y-%m-%d')
    date_partition = f"data={data_str}"

    visitas_df = create_visitas_df(date_partition, hour_snnipet, visitas)

    pedidos_df = create_visitas_df(date_partition, hour_snnipet, pedidos)

    visita_com_produto_e_conversao_df = merge_visita_produto(data_str, hour, pedidos_df, produtos_df, visitas_df)

    save_prepared(saida, visita_com_produto_e_conversao_df)

def remove_na_df(produtos_df):
    
    produtos_df['product_category_name'].fillna(value='no_name',inplace=True)
    produtos_df[['product_name_lenght','product_description_lenght','product_photos_qty']]=produtos_df[['product_name_lenght','product_description_lenght','product_photos_qty']].fillna(value=0)
    produtos_df['product_weight_g']=fill_mean(produtos_df['product_weight_g'])
    produtos_df['product_length_cm']=fill_mean(produtos_df['product_length_cm'])
    produtos_df['product_height_cm']=fill_mean(produtos_df['product_height_cm'])
    produtos_df['product_width_cm']=fill_mean(produtos_df['product_width_cm'])
    return produtos_df

def fill_mean(column):
    mean=column.mean()
    column=column.fillna(value=mean)
    return column


