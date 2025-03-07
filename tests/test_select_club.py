"""
Archivo de pruebas unitarias para la función select_club en el módulo src.select_club.
"""

import unittest
import pandas as pd
from src.select_club import select_club


class TestSelectClub(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función select_club.
    """
    def test_select_club(self):
        """
        Prueba la función select_club para asegurarse de que filtra correctamente
        los ciclistas por el club especificado.
        """
        df = pd.DataFrame({
            'dorsal': [1, 2, 3, 4],
            'biker': ['Carlos', 'Luis', 'Ana', 'Juan'],
            'time': ['01:20:00', '01:15:00', '01:10:00', '01:25:00'],
            'club_clean': ['UCSC', 'SARIÑENA', 'UCSC', 'OSCENSE']
        })

        result = select_club(df, 'UCSC')

        expected = pd.DataFrame({
            'dorsal': [1, 3],
            'biker': ['Carlos', 'Ana'],
            'time': ['01:20:00', '01:10:00'],
            'club_clean': ['UCSC', 'UCSC']
        })

        result_reset = result.reset_index(drop=True)
        expected_reset = expected.reset_index(drop=True)

        pd.testing.assert_frame_equal(result_reset, expected_reset)


if __name__ == '__main__':
    unittest.main()
