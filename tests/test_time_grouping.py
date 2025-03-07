"""
Archivo de pruebas unitarias para las funciones de agrupamiento de tiempos
en el módulo src.time_grouping.
"""

import os
import unittest
import pandas as pd
import matplotlib.pyplot as plt
from src.time_grouping import minutes_002040, group_by_variable, make_histogram


class TestTimeGrouping(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones de agrupamiento de tiempos
    en el módulo src.time_grouping.
    """
    def test_minutes_002040(self):
        """
        Prueba la función minutes_002040 para asegurarse de que agrupa los
        minutos de la cadena de tiempo correctamente en intervalos de 20 minutos.
        """
        test_data = [
            ("00:05:00", "00:00"),
            ("00:25:00", "00:20"),
            ("00:35:00", "00:20"),
            ("00:55:00", "00:40"),
            ("01:05:00", "01:00")
        ]

        for time_str, expected in test_data:
            self.assertEqual(minutes_002040(time_str), expected)

    def test_group_by_variable(self):
        """
        Prueba la función group_by_variable para asegurarse de que agrupa
        correctamente un DataFrame por una variable específica.
        """
        data = {'time_grouped': ['00:00', '00:20', '00:20', '00:40',
                                 '01:00', '00:00'],
                'dorsal': [1, 2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        grouped_df = group_by_variable(df, 'time_grouped')
        expected_data = {'time_grouped': ['00:00', '00:20', '00:40', '01:00'],
                         'count': [2, 2, 1, 1]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(grouped_df, expected_df)

    def test_make_histogram(self):
        """
        Prueba la función make_histogram para asegurarse de que genera y guarda
        un histograma correctamente a partir de un DataFrame de tiempos agrupados.
        """
        data = {'time_grouped': ['00:00', '00:20', '00:20', '00:40',
                                 '01:00', '00:00'],
                'count': [2, 2, 1, 1, 1, 2]}
        grouped_df = pd.DataFrame(data)
        output_path = 'test_histograma.png'
        make_histogram(grouped_df, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)


if __name__ == '__main__':
    unittest.main()
