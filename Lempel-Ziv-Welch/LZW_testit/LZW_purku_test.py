import os 
import unittest
from LZW_purku import LZW_purku
from LZW_koodaus import LZWKoodaus
from LZW_pakkaus import LZW_pakkaa

class TestLZWPurku(unittest.TestCase):
    def setUp(self):
        pass

    def test_LZW_purku_toimii(self):
        alkuperainen = "/home/kasperka/testi.txt"
        pakattu = LZW_pakkaa(alkuperainen)
        purettu = LZW_purku(pakattu)

        self.assertEqual(os.path.getsize(alkuperainen),os.path.getsize(purettu))
