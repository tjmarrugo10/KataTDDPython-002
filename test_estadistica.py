from unittest import TestCase

from Estadistica import Estadistica


class TestEstadistica(TestCase):
    def test_stats(self):
        self.assertEqual(Estadistica().stats(""), [0, 0, 0, 0], "Cadena vacia")

    def test_stats_unacadena(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1, 1, 1], "Un numero")

    def test_stats_dosnumeros(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1, 2, 1.5], "Dos numeros")

    def test_stats_nnumeros(self):
        self.assertEqual(Estadistica().stats("1,2,3,4"), [4, 1, 4, 2.5], "Multiples numeros")

    def test_stats_cadenavacia_minimo(self):
        self.assertEqual(Estadistica().stats(""), [0, 0, 0, 0], "Cadena vacia y minimo")

    def test_stats_unacadena_minimo(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1, 1, 1], "Un numero y minimo")

    def test_stats_dosnumeros_minimo(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1, 2, 1.5], "Dos numeros y minimo")

    def test_stats_cadenavacia_minimo_maximo(self):
        self.assertEqual(Estadistica().stats(""), [0, 0, 0, 0], "Cadena vacia, minimo,maximo")

    def test_stats_unnumero_minimo_maximo(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1, 1, 1], "Un numero, minimo, maximo")

    def test_stats_dosnumeros_minimo_maximo(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1, 2, 1.5], "Dos numeros,minimo,maximo")

    def test_stats_cadenavacia_promedio(self):
        self.assertEqual(Estadistica().stats(""), [0, 0, 0, 0], "Cadena vacia y promedio")

    def test_stats_unnumero_promedio(self):
        self.assertEqual(Estadistica().stats("1"), [1, 1, 1, 1], "Un numero, minimo, maximo, promedio")

    def test_stats_dosnumeros_promedio(self):
        self.assertEqual(Estadistica().stats("1,2"), [2, 1, 2, 1.5], "Dos numeros, minimo, maximo y promedio")

