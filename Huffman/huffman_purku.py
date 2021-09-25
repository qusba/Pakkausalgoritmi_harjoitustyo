import os 
from huffman_koodaus import HuffmanKoodaus
from Huffman_pakkaus import huffman_pakkaa

def huffman_purku(huffmankoodaus_olio,binääritiedosto_polku):
    tiedostonimi, tiedostotyyppi = os.path.splitext(binääritiedosto_polku)
    output_polku = tiedostonimi + "(purettu)" + ".txt"

    with open(binääritiedosto_polku,"rb") as tiedosto, open(output_polku, "w") as optiedosto:
        bittiteksti = ""

        tavu = tiedosto.read(1)
        while len(tavu) > 0:
            tavu = ord(tavu)
            bitit = bin(tavu)[2:].rjust(8,"0")
            bittiteksti += bitit
            tavu = tiedosto.read(1)
        
        koodattu_teksti = huffmankoodaus_olio.poista_taytto(bittiteksti)
        purettu_teksti = huffmankoodaus_olio.muuta_tavut_tekstiksi(koodattu_teksti)

        optiedosto.write(purettu_teksti)
    print("Purku valmis")
    print(output_polku)
    return output_polku

alkuperainen = HuffmanKoodaus("/home/kasperka/unicafe.txt")
pakattu = huffman_pakkaa(alkuperainen)
purettu = huffman_purku(alkuperainen,pakattu)
