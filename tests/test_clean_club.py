"""
Archivo de pruebas unitarias para la función clean_club en el módulo src.clean_club.
"""

import unittest
from src.clean_club import clean_club


class TestCleanClub(unittest.TestCase):
    """
    Clase de pruebas unitarias para la función clean_club.
    """
    def test_clean_club(self):
        """
        Prueba la función clean_club con varios casos de prueba para verificar
        que limpia correctamente los nombres de los clubes ciclistas.
        """
        test_cases = [
            ("PEÑA CICLISTA HUESCA", "HUESCA"),
            ("C.C. HUESCA", "HUESCA"),
            ("C.C HUESCA", "HUESCA"),
            ("UCSC T.T.", "UCSC"),
            ("A.D. SARIÑENA", "SARIÑENA"),
            (" CLUB CICLISTA OSCENSE ", "OSCENSE"),
            ("PENYA CICLISTA BARBASTRO", "BARBASTRO"),
            ("UCSC", "UCSC"),
            ("", ""),
        ]

        for input_club, expected_output in test_cases:
            with self.subTest(input_club=input_club):
                self.assertEqual(clean_club(input_club), expected_output)


if __name__ == "__main__":
    unittest.main()
