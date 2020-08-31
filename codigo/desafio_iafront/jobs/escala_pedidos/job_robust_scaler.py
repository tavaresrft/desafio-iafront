import click
import os
import shutil

from sklearn.preprocessing import RobustScaler

from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.common import prepare_dataframe, transform
from desafio_iafront.jobs.contants import lista_departamentos

@click.command()
@click.option('--visitas-com-conversao', type=click.Path(exists=True))
@click.option('--saida')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--departamentos', type=str, help="Departamentos separados por virgula")
def main(visitas_com_conversao, saida, data_inicial, data_final, departamentos):
    
    if departamentos.lower() == "todos":
        departamentos_lista = lista_departamentos()
    else:
        departamentos_lista = [departamento.strip() for departamento in departamentos.split(",")]
        
    result = prepare_dataframe(departamentos_lista, visitas_com_conversao, data_inicial, data_final)

    result_scaled = transform(result, RobustScaler())

    if os.path.exists(saida) == True:
    	shutil.rmtree(saida)

    save_partitioned(result_scaled, saida, ['data', 'hora'])

if __name__ == '__main__':
    main()
