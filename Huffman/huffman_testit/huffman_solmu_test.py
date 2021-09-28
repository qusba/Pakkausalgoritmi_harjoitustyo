import unittest
from huffman_solmu import HuffmanSolmu

class TestHuffmanSolmu(unittest.TestCase):
    def setUp(self):
        pass


def test_solmu_luodaan_oikein(self):
    solmu = HuffmanSolmu("f",30)
    self.assertEqual(solmu.merkki,"f")
    self.assertEqual(solmu.ilmaantuvuus,30)
    self.assertEqual(solmu.vasen_lapsi,None)
    self.assertEqual(solmu.oikea_lapsi,None)