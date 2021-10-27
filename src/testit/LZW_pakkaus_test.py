import unittest
import os 
import LZW

class TestLZWPakkaus(unittest.TestCase):
    def setUp(self):
        pass

    def test_LZW_pakkaa_toimii(self):
        pakattu = LZW.LZW_pakkaa("/home/kasperka/testi.txt")
        self.assertEqual(pakattu,"/home/kasperka/testi_LZW.bin")
        tiedostokoko = os.path.getsize(pakattu)
        self.assertNotEqual(tiedostokoko,0)
        
