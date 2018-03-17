from unittest import TestCase

from Estadistica import Estadistica


class TestEstadistica(TestCase):
    def test_stats(self):
        self.assertEqual(Estadistica().stats(""), [0, 0,0], "Cadena vacia")

    def test_stats_unacadena(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1], "Un numero")

    def test_stats_dosnumeros(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1], "Dos numeros")

    def test_stats_nnumeros(self):
        self.assertEqual(Estadistica().stats("1,2,3,4"), [4, 1], "Multiples numeros")

    def test_stats_cadenavacia_minimo(self):
        self.assertEqual(Estadistica().stats(""), [0, 0,0], "Cadena vacia y minimo")

    def test_stats_unacadena_minimo(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1], "Un numero y minimo")

    def test_stats_dosnumeros_minimo(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1], "Dos numeros y minimo")

    def test_stats_cadenavacia_minimo_maximo(self):
        self.assertEqual(Estadistica().stats(""),[0,0,0],"Cadena vacia, minimo,maximo")