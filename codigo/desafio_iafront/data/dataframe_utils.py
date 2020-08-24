import json
from typing import Sequence, Dict

import pandas as pd
import os
from datetime import timedelta
from functools import reduce
from dataset_loader import Dataset


def read_csv(file_path: str, datetime_columns: Sequence[str] = ()) -> pd.DataFrame:
    if datetime_columns:
        data_frame = pd.read_csv(file_path, header=0,
                                 infer_datetime_format=True,
                                 parse_dates=datetime_columns)
    else:
        data_frame = pd.read_csv(file_path, header=0)

    return data_frame


def read_partitioned_json(file_path: str, filter_function=lambda _: True) -> pd.DataFrame:
    data_source = Dataset(base_path=file_path, extension="json", filter_function=filter_function,
                          loader_function=_json_loader_function, ignore_partitions=False)
    return data_source.to_pandas()


def join_datasets(join_column: str, how: str, *args) -> pd.DataFrame:
    return reduce(lambda dataset_1, dataset_2: dataset_1.join(dataset_2.set_index(join_column), how=how,
                                                              on=join_column), args)


def keep_columns(data_frame: pd.DataFrame, kept_columns: Sequence[str]) -> pd.DataFrame:
    return data_frame[kept_columns]


def encode_columns(data_frame: pd.DataFrame, columns: Sequence[str]) -> pd.DataFrame:
    columns_head = columns[0]
    columns_tail = columns[0:]

    if columns:
        encoded = pd.get_dummies(data_frame[columns_head], prefix=columns_head)
        encoded_data_frame = data_frame.join(encoded)

        return encode_columns(encoded_data_frame, columns_tail)
    else:
        return data_frame


def rename_columns(data_frame: pd.DataFrame, column_renames: Dict[str, str]) -> pd.DataFrame:
    return data_frame.rename(columns=column_renames)


def extract_date(data_frame: pd.DataFrame, timestamp_column: str, date_column: str) -> pd.DataFrame:
    result_data_frame = data_frame.copy(deep=True)
    result_data_frame[date_column] = [date_time.date() for date_time in data_frame[timestamp_column]]

    return result_data_frame


def extract_hour(data_frame: pd.DataFrame, timestamp_column: str, hour_column: str) -> pd.DataFrame:
    result_data_frame = data_frame.copy(deep=True)
    result_data_frame[hour_column] = [date_time.hour for date_time in data_frame[timestamp_column]]

    return result_data_frame


def _json_loader_function(filename: str) -> Sequence[Dict]:
    with open(filename) as json_file:
        lines = json_file.readlines()
        json_list = list(map(_read_json_line, lines))
        return json_list


def _read_json_line(json_line: str) -> dict:
    return json.loads(json_line.rstrip('\n'))

def read_data_partitions(data_inicial,data_final, data_path):
    
    delta: timedelta = (data_final - data_inicial)
    date_partitions = [data_inicial.date() + timedelta(days=days) for days in range(delta.days)]
    
    for data in date_partitions:
        hour_partitions = list(range(0, 24))

        for hour in hour_partitions:
            hour_snnipet = f"hora={hour}"

            data_str = data.strftime('%Y-%m-%d')
            date_partition = f"data={data_str}"

            data_partition = os.path.join(data_path, date_partition, hour_snnipet)
            dataframe = read_partitioned_json(data_partition)
            dataframe["id_produto"] = dataframe["id_produto"].astype(str)
            dataframe["id_visita"] = dataframe["id_visita"].astype(str)

            dataframe["data"] = data_str
            dataframe["hora"] = hour

    return dataframe
