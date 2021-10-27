import unittest
import Huffman

class TestHuffmanPakkaus(unittest.TestCase):
    def setUp(self):
        self.olio = Huffman.HuffmanKoodaus()

    def test_huffman_pakkaa_toimii(self):
        pakattu = Huffman.huffman_pakkaa("/home/kasperka/testi.txt")
        self.assertEqual(pakattu,"/home/kasperka/testi_Huffman.bin")
        
