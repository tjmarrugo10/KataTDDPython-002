from unittest import TestCase

from Estadistica import Estadistica


class TestEstadistica(TestCase):
    def test_stats(self):
        self.assertEqual(Estadistica().stats(""), [0], "Cadena vacia")

    def test_stats_unacadena(self):
        self.assertEqual(Estadistica().stats("1"), [1], "Un numero")

    def test_stats_dosnumeros(self):
        self.assertEqual(Estadistica().stats("1,2"), [2], "Dos numeros")