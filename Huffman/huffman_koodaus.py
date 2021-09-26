from huffman_solmu import HuffmanSolmu


class HuffmanKoodaus:
    """Luokka, jossa kaikki funktiot, joita tarvitaan tiedoston pakkaamiseen ja purkamiseen Huffman-menetelmällä.

    """

    def __init__(self, inputpolku):
        """ Luokan konstruktori.

        Parametrit:
        input_polku: Polku tiedostoon joka halutaan pakata ilmaistuna stringinä.
        bittiesitykset: Sanakirja, jota tarvitaan Huffmannin puun mukaisten merkkien uusien bittiesitysten tallentamiseen.
        puun_bittikoodi: Merkkijono, johon tallennetaan Huffmannin puu bitteinä.
        """
        self.input_polku = inputpolku
        self.bittiesitykset = {}
        self.puun_bittikoodi = ""

    def luo_ilmaantuvuus_sanakirja(self, teksti):
        """ Funktio joka laskee tiedoston merkit ja niiden ilmaantuvuuden ja luo tiedoista sanakirjan.

        Parametrit:
            teksti: [Teksti, joka halutaan pakata]

        Palauttaa:
            Sanakirja: [Valmis dict muuttuja]
        """
        sanakirja = {}
        for merkki in teksti:
            if merkki not in sanakirja:
                sanakirja[merkki] = 0
            sanakirja[merkki] += 1
        return sanakirja

    def luo_puu(self, data: dict):
        """Funktio joka luo Huffmannin puun

        Parametrit:
        data (dict): [sanakirja joka sisältää pakattavan tiedoston kaikki merkit ja niiden ilmaantuvuuden]

        Palauttaa:
            Solmut[0]  [Valmiin Huffmannin puun juurisolmu]"""

        solmut = []
        for solmu in data.items():
            solmut.append(HuffmanSolmu(solmu[0], solmu[1]))

        while len(solmut) > 1:
            solmut = sorted(solmut, key=lambda solmu: solmu.ilmaantuvuus)

            vasen_solmu = solmut[0]
            oikea_solmu = solmut[1]
            uusi_solmu = HuffmanSolmu(None,
                                      vasen_solmu.ilmaantuvuus+oikea_solmu.ilmaantuvuus, vasen_solmu, oikea_solmu)

            solmut.append(uusi_solmu)
            solmut.remove(vasen_solmu)
            solmut.remove(oikea_solmu)

        return solmut[0]

    def muuta_puu_biteiksi(self, solmu):
        """Funktio, joka muuttaa Huffmannin puun biteiksi, jotta se voidaan tallentaa pakatun tekstin kanssa.

        Parametrit:
            solmu: [Huffmannin puun juurisolmu.]

        Palauttaa:
            puun_bittikoodi: [Valmis merkkijono, jossa on koodattuna Huffmannin puun sisältö ja sen rakenne.]
        """

        if solmu.vasen_lapsi is None and solmu.oikea_lapsi is None:
            self.puun_bittikoodi += "1" + "{0:08b}".format(ord(solmu.merkki))

        else:
            self.puun_bittikoodi += "0"
            self.muuta_puu_biteiksi(solmu.vasen_lapsi)
            self.muuta_puu_biteiksi(solmu.oikea_lapsi)
        return self.puun_bittikoodi

    def tallenna_koodit(self, solmu, bittiesitys=""):
        """Funktio, joka tallentaa konstruktorin luomaan self.bittiesitykset sanakirjaan Huffmannin puun mukaiset merkkien uudet bittiesitykset.


        Parametrit:
            solmu ([type]): [Huffmannin puun juurisomu, saadaan funktiolta "luo_puu"]
            bittiesitys: [Tyhjä merkkijono, johon rakentuvat uudet bittiesitykset rekursion edetessä]. Oletuksena "".
        """
        if solmu == None:
            return
        if solmu.merkki != None:
            self.bittiesitykset[solmu.merkki] = bittiesitys
            self.kaanteiset_bittiesitykset[bittiesitys] = solmu.merkki

        self.tallenna_koodit(solmu.vasen_lapsi, bittiesitys + "0")
        self.tallenna_koodit(solmu.oikea_lapsi, bittiesitys + "1")

    def muuta_teksti_biteiksi(self, teksti):
        """Funktio luo merkkijonon, joka vastaa tekstiä bitteinä uusien bittiesitysten mukaan.


        Parametrit:
            teksti: [Teksti jota tulkitaan.]

        Palauttaa:
            bittireksti: [Uusi luotu merkkijono.]
        """
        bittiteksti = ""
        for merkki in teksti:
            bittiteksti += self.bittiesitykset[merkki]
        return bittiteksti

    def tayta_tavut(self, koodattu_teksti):
        """Funktio varmistaa, että "muuta_biteiksi" funktiossa luotu merkkijono on oikean mittainen, jotta se voidaan muuttaa tavuiksi.
        Funktio lisää tarvittavat ylimääräiset bitit merkkijonoon, sekä tiedon siitä, mitä on lisätty. Tässä vaiheessa myös biteiksi muutettu
        Huffmannin puu lisätään koodattuun tekstiin.

        Parametrit:
            koodattu_teksti: ["muuta_biteiksi" funktion palauttama merkkijono.]

        Returns:
            Koodattu_teksti: [Valmiiksi hiottu bittimerkkijono.]
        """
        puun_pituus = len(self.puun_bittikoodi)
        puun_pituus_info = "{0:08b}".format(puun_pituus)
        koodattu_teksti = self.puun_bittikoodi + koodattu_teksti
        koodattu_teksti = puun_pituus_info + koodattu_teksti
        ylijaamabitit = 8 - (len(koodattu_teksti) % 8)
        for i in range(ylijaamabitit):
            koodattu_teksti += "0"

        tayttoinfo = "{0:08b}".format(ylijaamabitit)
        koodattu_teksti = tayttoinfo + koodattu_teksti
        return koodattu_teksti

    def muuta_teksti_tavuiksi(self, taytetty_koodattu_teksti):
        """Funktio joka "tayta_tavut" funktion valmiiksi käsittelemän merkkijonon tavuiksi.

        Args:
            taytetty_koodattu_teksti: ["tayta_tavut" funktion valmistelema merkkijono.]

        Returns:
            tavut: [Valmis tavuiksi muutettu teksti]
        """
        tavut = bytearray()
        for i in range(0, len(taytetty_koodattu_teksti), 8):
            tavu = taytetty_koodattu_teksti[i:i+8]
            tavut.append(int(tavu, 2))
        return tavut

    def poista_taytto(self, bittimerkkijono):
        """Funktio, joka poistaa tayta_tavut() funktion lisäämät ylimääräiset bitit.

        Parametrit:
            bittimerkkijono: ["Bitti" muodossa oleva merkkijono, joka on pakattu huffman_pakkaa() funktiolla]

        Palauttaa:
            koodattu_teksti: [Merkkijono, josta on poistettu ylimääräiset bitit lopusta, sekä informaatio niiden määrästä alusta.]
        """
        tayttoinfo = bittimerkkijono[:8]
        ylijaamabitit = int(tayttoinfo, 2)
        bittimerkkijono = bittimerkkijono[8:]
        koodattu_teksti = bittimerkkijono[:-1*ylijaamabitit]

        return koodattu_teksti

    def irroita_puu(self, bittimerkkijono):
        """Funktio, joka erottaa toisistaan merkkijonosta käsittelyä varten Huffmannin puun ja itse tekstiosan.

        Parametrit:
            bittimerkkijono ([type]): [Poista_taytto() funktion palauttama merkkijono]

        Palauttaa:
            [puu, teksti]: [Lista, jossa on kaksi alkiota: Huffmannin puu indeksissä 0, sekä koodattu teksti indeksissä 1]
        """
        puun_info = bittimerkkijono[:8]
        puun_pituus = int(puun_info, 2)
        bittimerkkijono = bittimerkkijono[8:]
        puu = bittimerkkijono[:puun_pituus]
        teksti = bittimerkkijono[puun_pituus:]
        return [puu, teksti]
