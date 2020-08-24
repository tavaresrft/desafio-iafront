import click
import os
import shutil

from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PowerTransformer

from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.common import prepare_dataframe, transform
from desafio_iafront.jobs.contants import transformations, transform_save, lista_departamentos

#@click.command()
#@click.option('--visitas-com-conversao', type=click.Path(exists=True))
#@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
#@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
#@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
#@click.option('--departamentos', type=str, help="Departamentos separados por virgula")
def main(visitas_com_conversao, saida, data_inicial, data_final, departamentos):
    
    if departamentos.lower() == "todos":
        departamentos_lista = lista_departamentos()
    else:
        departamentos_lista = departamentos
        
    result = prepare_dataframe(departamentos_lista, visitas_com_conversao, data_inicial, data_final)

    transformacoes_lista = transformations
    
    for i in range(len(transformations)):
        # Faz a escala dos valores
        result_scaled = transform(result, transformations[i])

        if os.path.exists(saida+transform_save[i]) == True:
            shutil.rmtree(saida+transform_save[i])
        # salva resultado
        save_partitioned(result_scaled, saida+transform_save[i], ['data', 'hora'])


if __name__ == '__main__':
    main()
