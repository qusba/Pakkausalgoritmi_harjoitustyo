import os
from huffman_koodaus import HuffmanKoodaus  # pylint: disable W0611
from Huffman_pakkaus import huffman_pakkaa
from huffman_solmu import HuffmanSolmu


def huffman_purku(huffmankoodaus_olio, binääritiedosto_polku):
    """Funktio, joka muutamaa apufunktiota käyttäen hoitaa Huffman pakatun tiedoston purkamisen.

    Parametrit:
        huffmankoodaus_olio: [HuffmanKoodaus luokan olio, tarvitaan luokan sisältämien funktioiden käyttöön.]
        binääritiedosto_polku: [Polku binääritiedostoon, joka halutaan purkaa.]

    Palauttaa:
        output_polku: [Polku purettuun tiedostoon.]
    """
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
        global puun_koodi
        puun_koodi = eritelty_teksti[0]
        global indeksi
        indeksi = 0
        uusi_puu = luo_puu_uudelleen(puun_koodi[indeksi])
        global puu
        puu = uusi_puu
        lopputulos = kaanna_teksti_puun_avulla(eritelty_teksti[1], uusi_puu)
        optiedosto.write(lopputulos)

    print("Purku valmis")
    print(output_polku)
    return output_polku


def luo_puu_uudelleen(bitti):
    """Funktio, joka luo uudelleen Huffmannin puun tiedostosta löytyvän informaation avulla.

    Käyttää hyväkseen globaaleja muuttujia puun_koodi, sekä indeksi, jotka on alustettu huffman_purku() funktiossa.

    Lukee puun_koodi muuttujassa sijaitsevasta merkkijonosta yhden merkin kerrallaan indeksi muuttujan avulla.

    Parametrit:
        bitti: [puun koodista yksi merkki]

    Palauttaa:
        HuffmanSolmu: [Valmis Huffmannin puu]
    """

    global puun_koodi
    global indeksi

    if bitti == "1":
        merkki = chr(int(puun_koodi[indeksi+1:indeksi+9], 2))
        indeksi = indeksi + 9
        return HuffmanSolmu(merkki, 0)

    else:
        if indeksi < len(puun_koodi)-1:
            indeksi += 1
        vasen_lapsi = luo_puu_uudelleen(puun_koodi[indeksi])
        oikea_lapsi = luo_puu_uudelleen(puun_koodi[indeksi])
        return HuffmanSolmu(None, 0, vasen_lapsi, oikea_lapsi)


def kaanna_teksti_puun_avulla(bittiteksti, solmu):
    """ Funktio, joka käyttää Huffmannin puuta bittitekstin kääntämiseen takaisin merkeiksi.

    Args:
        bittiteksti: [Käännettävän binääritiedoston eroteltu tekstiosa]
        solmu: [Huffmannin puun juurisolmu]

    Returns:
        kaannettu_teksti: [Valmis teksti, joka voidaan kirjottaa uuteen tiedostoon.]
    """
    global puu
    kaannettu_teksti = ""
    for bitti in bittiteksti:
        if bitti == "0" and solmu.vasen_lapsi is not None:
            solmu = solmu.vasen_lapsi
            if solmu.vasen_lapsi is None:
                kaannettu_teksti += solmu.merkki
                solmu = puu

        if bitti == "1" and solmu.oikea_lapsi is not None:
            solmu = solmu.oikea_lapsi
            if solmu.oikea_lapsi is None:
                kaannettu_teksti += solmu.merkki
                solmu = puu

    return kaannettu_teksti
