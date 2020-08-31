from setuptools import setup, find_packages

setup(
    name='desafio_iafront',
    version='',
    packages=find_packages(),
    url='',
    license='',
    author='Time IA-FRONT',
    author_email='',
    description='',
    install_requires=[
        "scikit-learn==0.23.1",
        "click==7.1.2",
        "bokeh==2.1.1",
        "dataset-loader==1.6",
        'pandas==1.1.0',
        'numpy==1.19.1'
    ],
    entry_points={
        'console_scripts': [
            'prepara_pedidos=desafio_iafront.jobs.pedidos.job:main',
            'normalizer=desafio_iafront.jobs.escala_pedidos.job_normalizer:main',
            'standardscaler=desafio_iafront.jobs.escala_pedidos.job_standard_scaler:main',
            'minmaxscaler=desafio_iafront.jobs.escala_pedidos.job_minmax_scaler:main',
            'maxabsscaler=desafio_iafront.jobs.escala_pedidos.job_maxabs_scaler:main',
            'robustscaler=desafio_iafront.jobs.escala_pedidos.job_robust_scaler:main',
            'powertransformer=desafio_iafront.jobs.escala_pedidos.job_power_transformer:main',
            'kmeans=desafio_iafront.jobs.clusters.job_kmeans:main',
            'mbk=desafio_iafront.jobs.clusters.job_mbk:main',
            'birch=desafio_iafront.jobs.clusters.job_birch:main',
            'spectralclustering=desafio_iafront.jobs.clusters.job_spectral_clustering:main',
            'agglomerativeclustering=desafio_iafront.jobs.clusters.agglomerative_clustering:main',
            'convert=desafio_iafront.jobs.clusters.job_conversion:main',
            'plotclustertime=desafio_iafront.jobs.graphics.job_cluster_times:main',
            'plotcompare=desafio_iafront.jobs.graphics.job_compare:main',
            'plotmap=desafio_iafront.jobs.graphics.job_map:main',
            'plottotalcluster=desafio_iafront.jobs.graphics.job_plot_cluster:main',
            'plotconversion=desafio_iafront.jobs.graphics.job_total_conversion:main',
        ]
    }
)
