import os
import Huffman


class PuunTiedot:
    """Apuluokka Huffmannin puun uudelleenrakennusta varten.

    """

    def __init__(self, puun_koodi, indeksi, puu):
        """Luokan konstruktori.

        Args:
            puun_koodi: [Huffmannin puu merkkijonona]
            indeksi: [Apumuttuja indeksointiin]
            puu: [Muuttuja, johon valmis puu tallennetaan. Hyödynnetään kääntäessä.]
        """
        self.puun_koodi = puun_koodi
        self.indeksi = indeksi
        self.puu = puu


def huffman_purku(binääritiedosto_polku):
    """Funktio, joka muutamaa apufunktiota käyttäen hoitaa Huffman pakatun tiedoston purkamisen.

    Parametrit:
        binääritiedosto_polku: [Polku binääritiedostoon, joka halutaan purkaa.]

    Palauttaa:
        output_polku: [Polku purettuun tiedostoon.]
    """
    huffmankoodaus_olio = Huffman.HuffmanKoodaus()
    tiedostonimi, tiedostotyyppi = os.path.splitext(binääritiedosto_polku)
    output_polku = tiedostonimi + "_purettu" + ".txt"

    with open(binääritiedosto_polku, "rb") as tiedosto, open(output_polku, "w") as optiedosto:
        bittiteksti = ""

        tavu = tiedosto.read(1)
        while len(tavu) > 0:
            tavu = ord(tavu)
            bitit = bin(tavu)[2:].rjust(8, "0")
            bittiteksti += bitit
            tavu = tiedosto.read(1)

        koodattu_teksti = huffmankoodaus_olio.poista_taytto(bittiteksti)
        eritelty_teksti = huffmankoodaus_olio.irroita_puu(koodattu_teksti)
        puun_tiedot_olio = PuunTiedot(eritelty_teksti[0], 0, None)
        uusi_puu = luo_puu_uudelleen(
            puun_tiedot_olio.puun_koodi[puun_tiedot_olio.indeksi], puun_tiedot_olio)
        puun_tiedot_olio.puu = uusi_puu
        lopputulos = kaanna_teksti_puun_avulla(
            eritelty_teksti[1], uusi_puu, puun_tiedot_olio)
        optiedosto.write(lopputulos)

    print("Purku valmis")
    print(output_polku)
    return output_polku


def luo_puu_uudelleen(bitti, puun_tiedot_olio):
    """Funktio, joka luo uudelleen Huffmannin puun tiedostosta löytyvän informaation avulla.

    Käyttää hyväkseen globaaleja muuttujia puun_koodi, sekä indeksi, jotka on alustettu huffman_purku() funktiossa.

    Lukee puun_koodi muuttujassa sijaitsevasta merkkijonosta yhden merkin kerrallaan indeksi muuttujan avulla.

    Parametrit:
        bitti: [puun koodista yksi merkki]
        puun_tiedot_olio: [huffman_purku -funktiossa luotu puun_tiedot_olio, tarvitaan funktion ulkopuolisten muuttujien käyttöön.]

    Palauttaa:
        HuffmanSolmu: [Valmis Huffmannin puu]
    """

    if bitti == "1":
        merkki = chr(int(
            puun_tiedot_olio.puun_koodi[puun_tiedot_olio.indeksi+1:puun_tiedot_olio.indeksi+9], 2))
        puun_tiedot_olio.indeksi = puun_tiedot_olio.indeksi + 9
        return Huffman.HuffmanSolmu(merkki, 0)

    else:
        if puun_tiedot_olio.indeksi < len(puun_tiedot_olio.puun_koodi)-1:
            puun_tiedot_olio.indeksi += 1
        vasen_lapsi = luo_puu_uudelleen(
            puun_tiedot_olio.puun_koodi[puun_tiedot_olio.indeksi], puun_tiedot_olio)
        oikea_lapsi = luo_puu_uudelleen(
            puun_tiedot_olio.puun_koodi[puun_tiedot_olio.indeksi], puun_tiedot_olio)
        return Huffman.HuffmanSolmu(None, 0, vasen_lapsi, oikea_lapsi)


def kaanna_teksti_puun_avulla(bittiteksti, solmu, puun_tiedot_olio):
    """ Funktio, joka käyttää Huffmannin puuta bittitekstin kääntämiseen takaisin merkeiksi.

    Parametrit:
        bittiteksti: [Käännettävän binääritiedoston eroteltu tekstiosa]
        solmu: [Huffmannin puun juurisolmu]
        puun_tiedot_olio: [huffman_purku -funktiossa luotu puun_tiedot_olio, tarvitaan funktion ulkopuolisten muuttujien käyttöön.]
]

    Palauttaa:
        kaannettu_teksti: [Valmis teksti, joka voidaan kirjottaa uuteen tiedostoon.]
    """

    kaannettu_teksti = ""
    for bitti in bittiteksti:
        if bitti == "0" and solmu.vasen_lapsi is not None:
            solmu = solmu.vasen_lapsi
            if solmu.vasen_lapsi is None:
                kaannettu_teksti += solmu.merkki
                solmu = puun_tiedot_olio.puu

        if bitti == "1" and solmu.oikea_lapsi is not None:
            solmu = solmu.oikea_lapsi
            if solmu.oikea_lapsi is None:
                kaannettu_teksti += solmu.merkki
                solmu = puun_tiedot_olio.puu

    return kaannettu_teksti
    
