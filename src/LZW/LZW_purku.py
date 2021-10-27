import os
import LZW

def LZW_purku(binääritiedosto_polku):
    """Funktio purkaa LZW-menetelmällä pakatun tiedoston kutsumalla LZWKoodaus -luokan funktioita.

    Parametrit:
        binääritiedosto_polku: [Polku purettavaan binääritiedostoon.]

    Palauttaa:
        output_polku: [Polku purettuun tiedostoon.]
    """

    tiedostonimi, tiedostotyyppi = os.path.splitext(binääritiedosto_polku)
    output_polku = tiedostonimi + "_purettu" + ".txt"
    LZWKoodaus_olio = LZW.LZWKoodaus()

    with open(binääritiedosto_polku, "rb") as tiedosto, open(output_polku, "w") as optiedosto:

        bittikoodi = ""
        tavu = tiedosto.read(1)

        while len(tavu) > 0:
            tavu = ord(tavu)
            bitit = bin(tavu)[2:].rjust(8, "0")
            bittikoodi += bitit
            tavu = tiedosto.read(1)

        bittikoodi = LZWKoodaus_olio.poista_taytto(bittikoodi)
        tuloste = LZWKoodaus_olio.muuta_bitit_tulosteeksi(bittikoodi)
        lopputulos = LZWKoodaus_olio.muuta_tuloste_tekstiksi(tuloste)
        optiedosto.write(lopputulos)
        print("Purku valmis")
        print(output_polku)
        return output_polku
