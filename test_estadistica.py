from unittest import TestCase

from Estadistica import Estadistica


class TestEstadistica(TestCase):
    def test_stats(self):
        self.assertEqual(Estadistica().stats(""), [0], "Cadena vacía")
