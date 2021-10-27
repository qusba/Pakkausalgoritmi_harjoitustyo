import os 
import unittest
import LZW

class TestLZWPurku(unittest.TestCase):
    def setUp(self):
        pass

    def test_LZW_purku_toimii(self):
        alkuperainen = "/home/kasperka/testi.txt"
        pakattu = LZW.LZW_pakkaa(alkuperainen)
        purettu = LZW.LZW_purku(pakattu)

        self.assertEqual(os.path.getsize(alkuperainen),os.path.getsize(purettu))
