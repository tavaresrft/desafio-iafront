from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PowerTransformer

COLUNA_PRODUCT_ID = "product_id"
COLUNA_DATA = "data"
COLUNA_HORA = "hora"
COLUNA_DEPARTAMENTO = "departamento"
COLUNA_LATITUDE = "geolocation_lat"
COLUNA_LONGITUDE = "geolocation_lng"
PREFIXO_CEP_RAW = "geolocation_zip_code_prefix"

transformations=[Normalizer(),StandardScaler(),MinMaxScaler(),MaxAbsScaler(),RobustScaler(),PowerTransformer()]
transform_save=['Normalizer','StandardScaler','MinMaxScaler','MaxAbsScaler','RobustScaler','PowerTransformer']

def lista_departamentos():
    departamentos = ['perfumaria', 'artes', 'esporte_lazer', 'bebes',
       'utilidades_domesticas', 'instrumentos_musicais', 'cool_stuff',
       'moveis_decoracao', 'eletrodomesticos', 'brinquedos',
       'cama_mesa_banho', 'construcao_ferramentas_seguranca',
       'informatica_acessorios', 'beleza_saude', 'malas_acessorios',
       'ferramentas_jardim', 'moveis_escritorio', 'automotivo',
       'eletronicos', 'fashion_calcados', 'telefonia', 'papelaria',
       'fashion_bolsas_e_acessorios', 'pcs', 'casa_construcao',
       'relogios_presentes', 'construcao_ferramentas_construcao',
       'pet_shop', 'eletroportateis', 'agro_industria_e_comercio', 'nan',
       'moveis_sala', 'sinalizacao_e_seguranca', 'climatizacao',
       'consoles_games', 'livros_interesse_geral',
       'construcao_ferramentas_ferramentas',
       'fashion_underwear_e_moda_praia', 'fashion_roupa_masculina',
       'moveis_cozinha_area_de_servico_jantar_e_jardim',
       'industria_comercio_e_negocios', 'telefonia_fixa',
       'construcao_ferramentas_iluminacao', 'livros_tecnicos',
       'eletrodomesticos_2', 'artigos_de_festas', 'bebidas',
       'market_place', 'la_cuisine', 'construcao_ferramentas_jardim',
       'fashion_roupa_feminina', 'casa_conforto', 'audio',
       'alimentos_bebidas', 'musica', 'alimentos',
       'tablets_impressao_imagem', 'livros_importados',
       'portateis_casa_forno_e_cafe', 'fashion_esporte',
       'artigos_de_natal', 'fashion_roupa_infanto_juvenil',
       'dvds_blu_ray', 'artes_e_artesanato', 'pc_gamer', 'moveis_quarto',
       'cine_foto', 'fraldas_higiene', 'flores', 'casa_conforto_2',
       'portateis_cozinha_e_preparadores_de_alimentos',
       'seguros_e_servicos', 'moveis_colchao_e_estofado',
       'cds_dvds_musicais']
    return departamentos