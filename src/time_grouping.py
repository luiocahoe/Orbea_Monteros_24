"""
Módulo para agrupar tiempos en intervalos de 20 minutos, agrupar por variable y
generar histogramas basados en los datos agrupados.
"""

import pandas as pd
import matplotlib.pyplot as plt


def minutes_002040(time_str: str) -> str:
    """
    Redondea los minutos de la cadena de tiempo en intervalos de 20 minutos.

    Args:
        time_str (str): Tiempo en formato "hh:mm:ss".

    Returns:
        str: Tiempo en formato "hh:mm", redondeado en intervalos de 20 minutos.
    """
    hh, mm, _ = map(int, time_str.split(':'))

    if mm < 20:
        mm = 0
    elif mm < 40:
        mm = 20
    elif mm < 60:
        mm = 40
    else:
        mm = 0
        hh += 1

    time_formatted = f"{hh:02}:{mm:02}"
    return time_formatted


def group_by_variable(df: pd.DataFrame, variable: str) -> pd.DataFrame:
    """
    Agrupa un DataFrame por una variable específica y cuenta el número de
    elementos en cada grupo.

    Args:
        df (pd.DataFrame): El DataFrame que contiene los datos.
        variable (str): El nombre de la columna por la cual se agruparán los datos.

    Returns:
        pd.DataFrame: Un nuevo DataFrame con los valores agrupados y sus
        correspondientes conteos.
    """
    return df.groupby(variable).size().reset_index(name='count')


def make_histogram(grouped_time_df: pd.DataFrame,
                   output_path: str = 'img/histograma.png'):
    """
    Genera un histograma a partir de un DataFrame agrupado por tiempo y
    lo guarda como imagen.

    Args:
        grouped_time_df (pd.DataFrame): El DataFrame con los tiempos agrupados y
        sus conteos.
        output_path (str): La ruta donde se guardará la imagen del histograma.
        El valor por defecto es 'img/histograma.png'.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_time_df['time_grouped'], grouped_time_df['count'])
    plt.xlabel('Tiempo agrupado (hh:mm)')
    plt.ylabel('Número de ciclistas')
    plt.title('Tiempo de finalización agrupado')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
