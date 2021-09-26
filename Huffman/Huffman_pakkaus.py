import os
from huffman_koodaus import HuffmanKoodaus


def huffman_pakkaa(huffmankoodaus_olio):
    """Funktio luo uuden pakatun tiedoston.

    Parametrit:
        huffmankoodaus_olio: [HuffmanKoodaus luokan luoma olio.]

    Palauttaa:
        output_polku: [Uuden pakatun tiedoston tiedostopolku.]
    """
    tiedostonimi, tiedostotyyppi = os.path.splitext(
        huffmankoodaus_olio.input_polku)
    output_polku = tiedostonimi + ".bin"

    with open(huffmankoodaus_olio.input_polku, "r") as tiedosto, open(output_polku, "wb") as optiedosto:
        teksti = tiedosto.read()
        teksti = teksti.rstrip()

        ilmaantuvuus = huffmankoodaus_olio.luo_ilmaantuvuus_sanakirja(teksti)
        huffmannin_puu = huffmankoodaus_olio.luo_puu(ilmaantuvuus)
        huffmannin_puu_bitteinä = huffmankoodaus_olio.muuta_puu_biteiksi(
            huffmannin_puu)
        uudet_bittikoodit = huffmankoodaus_olio.tallenna_koodit(huffmannin_puu)

        koodattu_teksti = huffmankoodaus_olio.muuta_teksti_biteiksi(teksti)
        taytetty_koodattu_teksti = huffmankoodaus_olio.tayta_tavut(
            koodattu_teksti)

        lopputulos = huffmankoodaus_olio.muuta_teksti_tavuiksi(
            taytetty_koodattu_teksti)
        optiedosto.write(bytes(lopputulos))

        print("Pakkaus valmis")
        print(output_polku)
        return output_polku
