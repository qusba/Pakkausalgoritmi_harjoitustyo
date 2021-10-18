import unittest
import os 
from LZW_pakkaus import LZW_pakkaa
from LZW_koodaus import LZWKoodaus

class TestLZWPakkaus(unittest.TestCase):
    def setUp(self):
        pass

    def test_LZW_pakkaa_toimii(self):
        pakattu = LZW_pakkaa("/home/kasperka/testi.txt")
        self.assertEqual(pakattu,"/home/kasperka/testi_LZW.bin")
        tiedostokoko = os.path.getsize(pakattu)
        self.assertNotEqual(tiedostokoko,0)
        
