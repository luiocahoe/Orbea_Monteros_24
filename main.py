"""
Módulo principal para ejecutar los ejercicios de la PEC.

Este archivo contiene las funciones para la ejecución de los ejercicios y
los cálculos relacionados con los ciclistas.

Funciones:
    - ejercicio_1: Importa y realiza un análisis preliminar del dataset.
    - ejercicio_2: Anonimiza a los ciclistas y limpia el dataset.
    - ejercicio_3: Agrupa los tiempos y genera un histograma.
    - ejercicio_4: Limpia la variable 'club' y agrupa los datos.
    - ejercicio_5: Realiza un análisis sobre el mejor ciclista de la UCSC.
"""

import argparse
from src.data_loader import load_dataset
from src.anonymize import name_surname, remove_non_participants, get_cyclist_by_dorsal
from src.time_grouping import minutes_002040, group_by_variable, make_histogram
from src.clean_club import clean_club
from src.select_club import select_club


def ejercicio_1():
    """
    Realiza la importación del dataset y un análisis exploratorio de los datos.
    Retorna el DataFrame con los datos del dataset.
    """
    print("\n***Ejercicio 1: Importación del dataset y EDA***\n")
    cyclists_df = load_dataset('data/dataset.csv')  # Renombrado a cyclists_df
    print("5 primeros registros:")
    print(cyclists_df.head())
    print(f"\nNúmero de ciclistas participantes: {cyclists_df['dorsal'].nunique()}")
    print(f"\nColumnas del dataframe: {cyclists_df.columns.tolist()}")
    return cyclists_df


def ejercicio_2(cyclists_df):
    """
    Anonimiza los ciclistas, elimina a los no participantes y limpia el dataset.
    Retorna el DataFrame limpio y anonimizado.
    """
    print("\n***Ejercicio 2: Anonimizar los ciclistas. Limpiar el dataset***\n")
    cyclists_df = name_surname(cyclists_df)
    print("5 primeros registros después de anonomizar:")
    print(cyclists_df.head())
    cyclists_df = remove_non_participants(cyclists_df)
    print("\n5 primeros registros después de eliminar los no participantes:")
    print(cyclists_df.head())
    print(f"\nNúmero de ciclistas tras limpiar: {cyclists_df['dorsal'].nunique()}")
    print("\nDatos del participante con dorsal 1000:")
    print(get_cyclist_by_dorsal(cyclists_df, 1000))
    return cyclists_df


def ejercicio_3(cyclists_df):
    """
    Agrupa los tiempos de los ciclistas en intervalos de 20 minutos y genera un histograma.
    Retorna el DataFrame con los tiempos agrupados y el DataFrame con los datos agrupados.
    """
    print("\n***Ejercicio 3: Agrupamiento de los minutos. Histograma***\n")
    cyclists_df['time_grouped'] = cyclists_df['time'].apply(minutes_002040)
    print("15 primeros registros después de crear la variable time_grouped:")
    print(cyclists_df.head(15))
    grouped_time_df = group_by_variable(cyclists_df, 'time_grouped')
    print("\nDatos agrupados por la variable time_grouped:")
    print(grouped_time_df)
    make_histogram(grouped_time_df, output_path='img/histograma.png')
    return cyclists_df, grouped_time_df


def ejercicio_4(cyclists_df):
    """
    Limpia la variable 'club' y agrupa los datos por club.
    Retorna el DataFrame con la variable 'club' limpia y el DataFrame agrupado por club.
    """
    print("\n***Ejercicio 4: Clubs ciclistas***\n")
    cyclists_df['club_clean'] = cyclists_df['club'].apply(clean_club)
    print("15 primeros registros después de la limpieza de la variable club:")
    print(cyclists_df.head(15))
    grouped_club_df = group_by_variable(cyclists_df, 'club_clean')
    print("\nDatos agrupados ordenados por participaciones:")
    print(grouped_club_df.sort_values(by='count', ascending=False))
    return cyclists_df, grouped_club_df


def ejercicio_5(cyclists_df):
    """
    Analiza el mejor ciclista de la UCSC, su posición y el porcentaje en el ranking general.
    Retorna el DataFrame de la UCSC, el mejor ciclista, su posición y el porcentaje.
    """
    print("\n***Ejercicio 5: Unió Ciclista Sant Cugat (UCSC)***\n")
    cyclists_df_by_time = cyclists_df.sort_values(by='time', ascending=True).reset_index(drop=True)
    cugat_df = select_club(cyclists_df_by_time, "Unió Ciclista Sant Cugat")
    mejor_ciclista = cugat_df.iloc[0]
    posicion_mejor_ciclista = (
        cyclists_df_by_time[cyclists_df_by_time['dorsal'] == mejor_ciclista['dorsal']]
        .index[0] + 1
    )
    total_ciclistas = len(cyclists_df_by_time)
    porcentaje = (posicion_mejor_ciclista / total_ciclistas) * 100
    print(f"El mejor ciclista de la UCSC es:\n{mejor_ciclista}")
    print(f"\nPosición en el ranking general: {posicion_mejor_ciclista}")
    print(f"\nPorcentaje del total: {porcentaje:.2f}%")
    return cugat_df, mejor_ciclista, posicion_mejor_ciclista, porcentaje


def main():
    parser = argparse.ArgumentParser(description="Ejecutar ejercicios de la PEC")
    parser.add_argument('--ejercicio', type=int, choices=range(1, 6),
                        help="Ejercicio a ejecutar (1-5)")
    args = parser.parse_args()

    if args.ejercicio is None:
        args.ejercicio = 5

    ejercicios_a_ejecutar = list(range(1, args.ejercicio + 1))

    cyclists_df = None

    for ejercicio_num in ejercicios_a_ejecutar:
        if ejercicio_num == 1:
            cyclists_df = ejercicio_1()
        elif ejercicio_num == 2:
            cyclists_df = ejercicio_2(cyclists_df)
        elif ejercicio_num == 3:
            cyclists_df, _ = ejercicio_3(cyclists_df)
        elif ejercicio_num == 4:
            cyclists_df, _ = ejercicio_4(cyclists_df)
        elif ejercicio_num == 5:
            ejercicio_5(cyclists_df)


if __name__ == "__main__":
    main()
