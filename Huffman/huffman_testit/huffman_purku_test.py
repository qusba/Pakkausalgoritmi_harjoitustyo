import unittest
from huffman_koodaus import HuffmanKoodaus
from Huffman_pakkaus import huffman_pakkaa
from huffman_purku import huffman_purku
from huffman_purku import luo_puu_uudelleen
from huffman_purku import kaanna_teksti_puun_avulla

class TestHuffmanPurku(unittest.TestCase):
    def setUp(self):
        self.olio = HuffmanKoodaus()
        self.pakattu = huffman_pakkaa("/home/kasperka/testi.txt")

    def test_huffman_purku_toimii(self):
        purettu = huffman_purku(self.pakattu)
        self.assertEqual(purettu,"/home/kasperka/testi_Huffman_purettu.txt")