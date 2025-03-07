"""
Archivo de pruebas unitarias para la función load_dataset en el módulo src.data_loader.
"""

import unittest
import pandas as pd
from src.data_loader import load_dataset


class TestDataLoader(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función load_dataset.
    """
    def test_load_dataset(self):
        """
        Prueba la función load_dataset para asegurarse de que carga correctamente
        un archivo CSV en un DataFrame de pandas.
        """
        df = load_dataset('data/dataset.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()
