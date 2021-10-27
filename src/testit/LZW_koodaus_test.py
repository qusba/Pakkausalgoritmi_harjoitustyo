import unittest
import LZW
class TestLZWKoodaus(unittest.TestCase):
    def setUp(self):
        self.olio = LZW.LZWKoodaus()
        self.teksti = "AAAAAABCCCCCCDDEEEEE\n"
        self.tuloste = self.olio.luo_tuloste_pakatessa(self.teksti)
        self.tuloste_bittimerkkijonona = self.olio.muuta_tuloste_biteiksi(self.tuloste)
        self.taytetty_bittimerkkijono = self.olio.tayta_tavut(self.tuloste_bittimerkkijonona)
        self.bittikoodi_tavuina = self.olio.muuta_bittikoodi_tavuiksi(self.taytetty_bittimerkkijono)

    
    def test_luo_tuloste_pakatessa_toimii(self):
       
        self.assertEqual(self.tuloste,[65, 256, 257, 66, 67, 260, 261, 68, 68, 69, 265, 265, 10])
    
    def test_muuta_tuloste_biteiksi_toimii(self):
        
        self.assertEqual(self.tuloste_bittimerkkijonona, "00001001001000001100000000100000001001000010001000011100000100100000101001000100001000100001000101100001001100001001000001010")

    def test_tayta_tavut_toimii(self):

        self.assertEqual(self.taytetty_bittimerkkijono, "0000001100001001001000001100000000100000001001000010001000011100000100100000101001000100001000100001000101100001001100001001000001010000")

    def test_muuta_bittikoodi_tavuiksi_toimii(self):

        self.assertEqual(type(self.bittikoodi_tavuina),bytearray)
        self.assertEqual(self.bittikoodi_tavuina,bytearray(b'\x03\t \xc0 $"\x1c\x12\nD"\x11a0\x90P'))
    
    def test_poista_taytto_toimii(self):
        bittikoodi = self.olio.poista_taytto(self.taytetty_bittimerkkijono)
        self.assertEqual(bittikoodi,self.tuloste_bittimerkkijonona)
    
    def test_muuta_bitit_tulosteeksi_toimii(self):
        tuloste = self.olio.muuta_bitit_tulosteeksi(self.tuloste_bittimerkkijonona)
        self.assertEqual(tuloste,self.tuloste)

    def test_muuta_tuloste_tekstiksi_toimii(self):
        teksti = self.olio.muuta_tuloste_tekstiksi(self.tuloste)
        self.assertEqual(teksti,self.teksti)
