"""
Módulo que contiene funciones para limpiar los nombres de los clubes ciclistas,
eliminando abreviaturas y cadenas específicas que no son relevantes.
"""

import re


def clean_club(club: str) -> str:
    """
    Limpia el nombre del club ciclista eliminando cadenas específicas y
    abreviaturas comunes.

    Esta función transforma el nombre del club a mayúsculas y elimina cadenas
    como "PEÑA CICLISTA", "AGRUPACIÓN CICLISTA", "CLUB", y otras
    abreviaturas relacionadas con clubes ciclistas.

    Args:
        club (str): El nombre del club ciclista a limpiar.

    Returns:
        str: El nombre del club ciclista limpio, sin abreviaturas ni
        cadenas adicionales.
    """
    club = club.upper()

    replace_values = ['PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
                      'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ',
                      'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB ']
    for value in replace_values:
        club = club.replace(value, '')

    club = re.sub(
        r'^('
        r'C\.C\. |C\.C |CC |'
        r'C\.D\. |C\.D |CD |'
        r'A\.C\. |A\.C |AC |'
        r'A\.D\. |A\.D |AD |'
        r'A\.E\. |A\.E |AE |'
        r'E\.C\. |E\.C |EC |'
        r'S\.C\. |S\.C |SC |'
        r'S\.D\. |S\.D |SD '
        r')', '', club
    )

    club = re.sub(
        r'('
        r' T\.T\.| T\.T| TT| '
        r'T\.E\.| T\.E| TE| '
        r'C\.C\.| C\.C| CC| '
        r'C\.D\.| C\.D| CD| '
        r'A\.D\.| A\.D| AD| '
        r'A\.C\.| A\.C| AC'
        r')$', '', club
    )

    club = club.strip()

    return club
