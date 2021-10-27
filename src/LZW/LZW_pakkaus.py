import os
import LZW


def LZW_pakkaa(input_polku):
    """Funktio, joka kutsuu LZWKoodaus -luokan funktioita pakatakseen tiedoston LZW-menetelmällä.

    Parametrit:
        input_polku: [Polku tiedostoon, joka halutaan pakata.]

    Returns:
        output_polku: [Polku pakattuun tiedostoon.]
    """

    tiedostonimi, tiedostotyyppi = os.path.splitext(input_polku)
    output_polku = tiedostonimi + "_LZW" ".bin"
    LZWKoodaus_olio = LZW.LZWKoodaus()
    print(input_polku)

    with open(input_polku, "r") as tiedosto, open(output_polku, "wb") as optiedosto:
        teksti = tiedosto.read()

        tuloste = LZWKoodaus_olio.luo_tuloste_pakatessa(teksti)
        bittikoodi = LZWKoodaus_olio.muuta_tuloste_biteiksi(tuloste)
        taytetty_bittikoodi = LZWKoodaus_olio.tayta_tavut(bittikoodi)
        tavut = LZWKoodaus_olio.muuta_bittikoodi_tavuiksi(taytetty_bittikoodi)

        optiedosto.write(bytes(tavut))
        print("Pakkaus valmis")
        return output_polku
