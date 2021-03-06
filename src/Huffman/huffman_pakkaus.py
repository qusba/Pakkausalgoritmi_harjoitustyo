import os
import Huffman


def huffman_pakkaa(input_polku):
    """Funktio luo uuden pakatun tiedoston.

    Parametrit:
        input_polku: [Polku tiedostoon, joka halutaan pakata.]

    Palauttaa:
        output_polku: [Uuden pakatun tiedoston tiedostopolku.]
    """
    huffmankoodaus_olio = Huffman.HuffmanKoodaus()
    tiedostonimi, tiedostotyyppi = os.path.splitext(input_polku)
    output_polku = tiedostonimi + "_Huffman"+".bin"

    with open(input_polku, "r") as tiedosto, open(output_polku, "wb") as optiedosto:
        teksti = tiedosto.read()

        ilmaantuvuus = huffmankoodaus_olio.luo_ilmaantuvuus_sanakirja(teksti)
        huffmannin_puu = huffmankoodaus_olio.luo_puu(ilmaantuvuus)
        huffmankoodaus_olio.muuta_puu_biteiksi(
            huffmannin_puu)
        huffmankoodaus_olio.tallenna_koodit(huffmannin_puu)

        koodattu_teksti = huffmankoodaus_olio.muuta_teksti_biteiksi(teksti)
        taytetty_koodattu_teksti = huffmankoodaus_olio.tayta_tavut(
            koodattu_teksti)

        lopputulos = huffmankoodaus_olio.muuta_teksti_tavuiksi(
            taytetty_koodattu_teksti)
        optiedosto.write(bytes(lopputulos))

        print("Pakkaus valmis")
        print(output_polku)
        return output_polku
