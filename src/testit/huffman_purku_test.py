import unittest
from huffmankoodaus import HuffmanKoodaus
from huffmanpakkaus import huffman_pakkaa
from huffmanpurku import huffman_purku

class TestHuffmanPurku(unittest.TestCase):
    def setUp(self):
        self.olio = HuffmanKoodaus()
        self.pakattu = huffman_pakkaa("/home/kasperka/testi.txt")

    def test_huffman_purku_toimii(self):
        purettu = huffman_purku(self.pakattu)
        self.assertEqual(purettu,"/home/kasperka/testi_Huffman_purettu.txt")