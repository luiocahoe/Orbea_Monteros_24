"""
Módulo que contiene funciones para anonimizar los datos de los ciclistas,
como asignar nombres falsos y eliminar ciclistas no participantes.
"""

import pandas as pd
from faker import Faker

def name_surname(df: pd.DataFrame) -> pd.DataFrame:
    """
    Asigna un nombre y apellido falso a los ciclistas en el dataframe.

    Args:
        df (pd.DataFrame): El dataframe que contiene los datos de los
        ciclistas, debe tener una columna 'biker'.

    Returns:
        pd.DataFrame: El dataframe con la columna 'biker' actualizada
        con nombres falsos generados.
    """
    fake = Faker()
    df['biker'] = df['biker'].apply(lambda _: fake.name())
    return df


def remove_non_participants(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra el dataframe para eliminar a los ciclistas que no
    participaron (tiempo '00:00:00').

    Args:
        df (pd.DataFrame): El dataframe con los datos de los ciclistas.

    Returns:
        pd.DataFrame: El dataframe filtrado, excluyendo a los ciclistas
        que no participaron.
    """
    return df[df['time'] != '00:00:00']


def get_cyclist_by_dorsal(df: pd.DataFrame, dorsal_number: int) -> pd.DataFrame:
    """
    Busca un ciclista por su dorsal en el dataframe.

    Args:
        df (pd.DataFrame): El dataframe que contiene los datos de los
        ciclistas.
        dorsal_number (int): El número de dorsal del ciclista a buscar.

    Returns:
        pd.DataFrame: Un dataframe con los datos del ciclista con
        el dorsal especificado.
    """
    return df[df['dorsal'] == dorsal_number]
