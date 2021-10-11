import unittest
from huffman_koodaus import HuffmanKoodaus
from huffman_pakkaus import huffman_pakkaa

class TestHuffmanPakkaus(unittest.TestCase):
    def setUp(self):
        self.olio = HuffmanKoodaus()

    def test_huffman_pakkaa_toimii(self):
        pakattu = huffman_pakkaa("/home/kasperka/testi.txt")
        self.assertEqual(pakattu,"/home/kasperka/testi_Huffman.bin")
        