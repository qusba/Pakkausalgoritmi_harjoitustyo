from huffman_solmu import Huffman_Solmu


def luo_puu(data: dict):
    """Funktio joka luo Huffmannin puun

    Parametrit:
        data (dict): [sanakirja joka sisältää pakattavan tiedoston kaikki merkit ja niiden ilmaantuvuuden]
    """
    solmut = []
    for solmu in data.items():
        solmut.append(Huffman_Solmu(solmu[0], solmu[1]))

    while len(solmut) > 1:
        solmut = sorted(solmut, key=lambda solmu: solmu.ilmaantuvuus)

        vasen_solmu = solmut[0]
        oikea_solmu = solmut[1]

        vasen_solmu.bittikoodi = "0"
        oikea_solmu.bittikoodi = "1"

        uusi_solmu = Huffman_Solmu(vasen_solmu.merkki + oikea_solmu.merkki,
                                   vasen_solmu.ilmaantuvuus+oikea_solmu.ilmaantuvuus, vasen_solmu, oikea_solmu)

        solmut.append(uusi_solmu)
        solmut.remove(vasen_solmu)
        solmut.remove(oikea_solmu)

    return solmut[0]


def tulosta_puu(solmu, bittiesitys=""):
    """funktio joka antaa tulosteena annetusta solmusta lähtevän puun rakenteen.
       Funktiolla voi todeta puun oikeellisuuden testaamista varten.
       Käy rekursiivisesti puun läpi ja printtaa merkit sekä niiden bittikoodit.

    Parametrit:
        solmu (Huffman_Solmu): [Huffman_Solmu olio]
        bittiesitys: [Käytännössä sama kuin {self.bittikoodi}, nimetty erilailla hämmennyksen välttämiseksi]
    """
    arvo = bittiesitys + solmu.bittikoodi
    if solmu.vasen_lapsi:
        tulosta_puu(solmu.vasen_lapsi, arvo)
    if solmu.oikea_lapsi:
        tulosta_puu(solmu.oikea_lapsi, arvo)
    if len(solmu.merkki) == 1:
        print((solmu.merkki, arvo))
