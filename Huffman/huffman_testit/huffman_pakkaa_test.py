import unittest
from huffman_koodaus import HuffmanKoodaus
from Huffman_pakkaus import huffman_pakkaa

class TestHuffmanPakkaus(unittest.TestCase):
    def setUp(self):
        self.olio = HuffmanKoodaus("/home/kasperka/testi.txt")

    def test_huffman_pakkaa_toimii(self):
        pakattu = huffman_pakkaa(self.olio)
        self.assertEqual(pakattu,"/home/kasperka/testi.bin")
        