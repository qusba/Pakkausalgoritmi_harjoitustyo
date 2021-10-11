import unittest
from huffman_koodaus import HuffmanKoodaus


class TestHuffmanKoodaus(unittest.TestCase):
    def setUp(self):
        self.teksti = "AAAAAABCCCCCCDDEEEEE\n"
        self.olio = HuffmanKoodaus()
        self.sanakirja = self.olio.luo_ilmaantuvuus_sanakirja(self.teksti)
        self.puu = self.olio.luo_puu(self.sanakirja)
        self.olio.tallenna_koodit(self.puu)
        self.puu_bitteina = self.olio.muuta_puu_biteiksi(self.puu)
        self.bittiteksti = self.olio.muuta_teksti_biteiksi(self.teksti)
        self.taytetty_bittiteksti = self.olio.tayta_tavut(self.bittiteksti)
        self.tavut = self.olio.muuta_teksti_tavuiksi(self.taytetty_bittiteksti)
        
    def test_luo_ilmaantuvuus_sanakirja_toimii(self):
        self.assertEqual(self.sanakirja["A"], 6)
        self.assertEqual(self.sanakirja["B"], 1)
        self.assertEqual(self.sanakirja["C"], 6)
        self.assertEqual(self.sanakirja["D"], 2)
        self.assertEqual(self.sanakirja["E"], 5)
        self.assertEqual(self.sanakirja["\n"],1)

    def test_luo_puu_toimii(self):
        self.assertEqual(self.puu.ilmaantuvuus, 21)
        self.assertEqual(self.puu.vasen_lapsi.oikea_lapsi.merkki, "E")
        self.assertEqual(self.puu.vasen_lapsi.vasen_lapsi.vasen_lapsi.merkki, "D")
        self.assertEqual(self.puu.vasen_lapsi.vasen_lapsi.oikea_lapsi.vasen_lapsi.merkki,"B")
        self.assertEqual(self.puu.vasen_lapsi.vasen_lapsi.oikea_lapsi.oikea_lapsi.merkki,"\n")

    def test_muuta_puu_biteiksi_toimii(self):
        self.assertEqual(self.puu_bitteina,"00010100010001010000101000010101010001010101000001101000011")

    def test_tallenna_koodit_toimii(self):
        self.assertEqual(self.olio.bittiesitykset["A"],"10")
        self.assertEqual(self.olio.bittiesitykset["B"],"0010")
        self.assertEqual(self.olio.bittiesitykset["C"],"11")
        self.assertEqual(self.olio.bittiesitykset["D"],"000")
        self.assertEqual(self.olio.bittiesitykset["E"],"01")
        self.assertEqual(self.olio.bittiesitykset["\n"],"0011")

    def test_muuta_teksti_biteiksi_toimii(self):
        self.assertEqual(self.bittiteksti,"101010101010001011111111111100000001010101010011")
    
    def test_tayta_tavut_toimii(self):  
        self.assertEqual(self.taytetty_bittiteksti,"000000010000010100000111100000000000000101000100010100001010000101010100010101010000011010000111010101010100010111111111111000000010101010100110")
        
    def test_muuta_teksti_tavuiksi(self):   
        self.assertEqual(self.tavut,bytearray(b'\x01\x05\x07\x80\x01DP\xa1TU\x06\x87UE\xff\xe0*\xa6'))

    def test_poista_taytto_toimii(self):
        bittiteksti = self.olio.poista_taytto(self.taytetty_bittiteksti)
        self.assertEqual(bittiteksti,"000001010000011110000000000000010100010001010000101000010101010001010101000001101000011101010101010001011111111111100000001010101010011")

    def test_irroita_puu_toimii(self):  
        bittiteksti = self.olio.poista_taytto(self.taytetty_bittiteksti)
        eroteltu = self.olio.irroita_puu(bittiteksti)
        self.assertEqual(eroteltu[0],"00010100010001010000101000010101010001010101000001101000011")
        self.assertEqual(eroteltu[1],"101010101010001011111111111100000001010101010011")

