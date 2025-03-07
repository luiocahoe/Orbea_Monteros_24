"""
Módulo para filtrar ciclistas por club en un dataframe. Filtra los ciclistas 
que pertenecen a un club especificado basado en la columna 'club_clean'.
"""

import pandas as pd


def select_club(df: pd.DataFrame, club_name: str) -> pd.DataFrame:
    """
    Filtra el dataframe para obtener los ciclistas que pertenecen al
    club especificado.

    Args:
        df (pd.DataFrame): El dataframe que contiene los datos de los ciclistas.
        club_name (str): El nombre del club por el cual se desea filtrar.

    Returns:
        pd.DataFrame: Un nuevo dataframe con los ciclistas que pertenecen
        al club especificado.
    """
    club_name_clean = club_name.upper()
    filtered_df = df[df['club_clean'] == club_name_clean]

    return filtered_df
