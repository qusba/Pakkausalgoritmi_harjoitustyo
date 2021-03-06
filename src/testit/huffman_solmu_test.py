import unittest
import Huffman
class TestHuffmanSolmu(unittest.TestCase):
    def setUp(self):
        pass


    def test_solmu_luodaan_oikein(self):
        solmu = Huffman.HuffmanSolmu("f",30)
        self.assertEqual(solmu.merkki,"f")
        self.assertEqual(solmu.ilmaantuvuus,30)
        self.assertEqual(solmu.vasen_lapsi,None)
        self.assertEqual(solmu.oikea_lapsi,None)
        self.assertEqual(solmu.bittikoodi,"")

    def test_solmulle_voidaan_osoittaa_vanhemmat(self):
        solmu1 = Huffman.HuffmanSolmu("f",30)
        solmu2 = Huffman.HuffmanSolmu("d",50)
        solmu3 = Huffman.HuffmanSolmu(None,solmu1.ilmaantuvuus+solmu2.ilmaantuvuus,solmu1,solmu2)

        self.assertEqual(solmu3.vasen_lapsi,solmu1)
        self.assertEqual(solmu3.oikea_lapsi,solmu2)
