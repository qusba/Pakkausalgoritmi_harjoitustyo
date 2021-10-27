import os
import LZW
import Huffman

while True:
    print()
    print("Hei! Haluatko pakata vai purkaa tiedoston?")
    print("Pakkaus = 1, purku = 2, poistu = 3")
    valinta1 = int(input("Syötä valinta: "))

    if valinta1 == 1:
        print()
        print("Halautko käyttää Huffman vai LZW -menetelmää?")
        print("Huffman = 1, LZW = 2")
        valinta2 = int(input("Syötä valinta: "))
        if valinta2 == 1:
            print()
            tiedosto = input("Syötä tiedostopolku: ")
            alkuperainen_koko = os.path.getsize(tiedosto)
            pakattu = Huffman.huffman_pakkaa(tiedosto)
            pakattu_koko = os.path.getsize(pakattu)
            teho = 100*(1 - (pakattu_koko/alkuperainen_koko))
            teho = round(teho)
            print(f"Pakkaustehokkuus oli noin {teho}%.")
        
        elif valinta2 == 2:
            print()
            tiedosto = input("Syötä tiedostopolku: ")
            alkuperainen_koko = os.path.getsize(tiedosto)
            pakattu = LZW.LZW_pakkaa(tiedosto)
            pakattu_koko = os.path.getsize(pakattu)
            teho = 100*(1 - (pakattu_koko/alkuperainen_koko))
            teho = round(teho)
            print(f"Pakkaustehokkuus oli noin {teho}%.")
    
    elif valinta1 == 2:
        print()
        print("Halautko käyttää Huffman vai LZW -menetelmää?")
        print("Huffman = 1, LZW = 2")
        valinta2 = int(input("Syötä valinta: "))
        
        if valinta2 == 1:
            print()
            tiedosto = input("Syötä _Huffman.bin loppuinen tiedostopolku: ")
            Huffman.huffman_purku(tiedosto)
        
        elif valinta2 == 2:
            print()
            tiedosto = input("Syötä _LZW.bin loppuinen tiedostopolku ")
            LZW.LZW_purku(tiedosto)  

    elif valinta1 == 3:
        break




