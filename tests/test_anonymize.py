"""
Archivo de pruebas unitarias para las funciones de anonimización en el módulo src.anonymize.
"""

import unittest
import pandas as pd
from faker import Faker
from src.anonymize import name_surname, remove_non_participants, get_cyclist_by_dorsal


class TestFunctions(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones de anonimización.
    """
    def setUp(self):
        """
        Configura los datos de prueba antes de cada prueba.
        """
        data = {
            'dorsal': [1001, 1002, 1003],
            'biker': ['Juan Pérez', 'Ana García', 'Luis Rodríguez'],
            'time': ['01:02:30', '00:00:00', '02:15:40'],
            'club': ['Club A', 'Club B', 'Club A']
        }
        self.df = pd.DataFrame(data)

    def test_name_surname(self):
        """
        Prueba la función name_surname para verificar que los nombres de los ciclistas
        se anonimicen correctamente.
        """
        df_result = name_surname(self.df)
        self.assertNotEqual(df_result['biker'][0], 'Juan Pérez')
        self.assertNotEqual(df_result['biker'][1], 'Ana García')
        self.assertNotEqual(df_result['biker'][2], 'Luis Rodríguez')
        self.assertTrue(all(isinstance(name, str) for name
                            in df_result['biker']))

    def test_remove_non_participants(self):
        """
        Prueba la función remove_non_participants para verificar que los ciclistas que
        no participaron se eliminen correctamente.
        """
        df_result = remove_non_participants(self.df)
        self.assertFalse((df_result['time'] == '00:00:00').any())
        self.assertEqual(len(df_result), 2)

    def test_get_cyclist_by_dorsal(self):
        """
        Prueba la función get_cyclist_by_dorsal para verificar que se obtienen los ciclistas
        correctos según su dorsal.
        """
        df_result = get_cyclist_by_dorsal(self.df, 1001)
        self.assertEqual(df_result['dorsal'].iloc[0], 1001)
        self.assertEqual(df_result['biker'].iloc[0], 'Juan Pérez')
        self.assertEqual(df_result['time'].iloc[0], '01:02:30')


if __name__ == "__main__":
    unittest.main()
