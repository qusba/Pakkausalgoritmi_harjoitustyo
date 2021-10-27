import unittest
import Huffman

class TestHuffmanPurku(unittest.TestCase):
    def setUp(self):
        self.olio = Huffman.HuffmanKoodaus()
        self.pakattu = Huffman.huffman_pakkaa("/home/kasperka/testi.txt")

    def test_huffman_purku_toimii(self):
        purettu = Huffman.huffman_purku(self.pakattu)
        self.assertEqual(purettu,"/home/kasperka/testi_Huffman_purettu.txt")
