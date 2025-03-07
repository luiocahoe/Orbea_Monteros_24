"""
Módulo para cargar un dataset desde un archivo CSV. Utiliza un separador de punto y coma.
"""

import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Carga un dataset desde un archivo CSV con separador de punto y coma.

    Args:
        file_path (str): La ruta al archivo CSV que contiene los datos.

    Returns:
        pd.DataFrame: Un DataFrame con los datos cargados desde el archivo CSV.
    """
    return pd.read_csv(file_path, sep=';')
