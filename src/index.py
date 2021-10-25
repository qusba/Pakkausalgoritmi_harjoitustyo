import os
from LZW.LZW_koodaus import LZWKoodaus
from LZW.LZW_purku import LZW_purku
from LZW.LZW_pakkaus import LZW_pakkaa
from Huffman.huffman_koodaus import HuffmanKoodaus
from Huffman.huffman_pakkaus import huffman_pakkaa
from Huffman.huffman_purku import huffman_purku

while True:
    print("Hei! Haluatko pakata vai purkaa tiedoston?")
    print("Pakkaus = 1, purku = 2, poistu = 3")
    valinta1 = int(input("Syötä valinta"))

    if valinta1 == 1:
        print("Halautko käyttää Huffman vai LZW -menetelmää?")
        print("Huffman = 1, LZW = 2")
        valinta2 = int(input("Syötä valinta"))
        if valinta2 == 1:
            tiedosto = input("Syötä tiedostopolku")
            alkuperainen_koko = os.path.getsize(tiedosto)
            pakattu = huffman_pakkaa(tiedosto)
            pakattu_koko = os.path.getsize(pakattu)
            teho = 100*(1 - (pakattu_koko/alkuperainen_koko))
            teho = round(teho)
            print(f"Pakkaustehokkuus oli {teho} prosenttia.")



