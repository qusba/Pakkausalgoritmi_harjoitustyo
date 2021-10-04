import math
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
        if solmu is None:
            return
        if solmu.merkki is not None:
            self.bittiesitykset[solmu.merkki] = bittiesitys

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

        # täytetään puun bittikoodi 8 jaolliseksi
        self.puun_bittikoodi = (8-puun_pituus % 8)*"0" + self.puun_bittikoodi
        puun_taytto_info = 8-puun_pituus % 8

        # tallennetaan info siitä, kuinka monta bittiä on täytetty
        puun_taytto_info = "{0:08b}".format(puun_taytto_info)
        puun_pituus = len(self.puun_bittikoodi)

        # laskee kuinka monta bittiä tarvitaan puun pituuden ilmoittavan kokonaisluvun tallentamiseen
        puuhun_tarvittavat_bitit = (math.log(puun_pituus, 2)) + 0.1
        puuhun_tarvittavat_bitit = math.ceil(puuhun_tarvittavat_bitit)

        # muuttaa lasketun luvun 8-bittiseksi
        info_biteista = "{0:08b}".format(puuhun_tarvittavat_bitit)

        puuhun_tarvittavat_bitit = "0"+str(puuhun_tarvittavat_bitit)+"b"

        # formatoidaan puun pituus x-bittiseksi
        puun_pituus_info = format(puun_pituus, puuhun_tarvittavat_bitit)

        # lisätään merkkijonoon puu ja erinäiset infobitit
        koodattu_teksti = puun_taytto_info + info_biteista + \
            puun_pituus_info + self.puun_bittikoodi + \
            koodattu_teksti

        ylijaamabitit = 8 - (len(koodattu_teksti) % 8)
        for i in range(ylijaamabitit): #pylint: disable W0612
            koodattu_teksti += "0"
        tayttoinfo = "{0:08b}".format(ylijaamabitit)

        # täydennetään kokonaisuus 8 jaolliseksi, lisätään info täytöstä
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
        print(tavut)
        return tavut

    def poista_taytto(self, bittimerkkijono):
        """Funktio, joka poistaa tayta_tavut() funktion lisäämät ylimääräiset bitit merkkijonon lopusta.

        Parametrit:
            bittimerkkijono: ["Bitti" muodossa oleva merkkijono, joka on pakattu huffman_pakkaa() funktiolla]

        Palauttaa:
            koodattu_teksti: [Merkkijono, josta on poistettu ylimääräiset bitit lopusta, sekä informaatio niiden määrästä alusta.]
        """
        # erottelee informaation loppuun lisätyistä biteistä
        tayttoinfo = bittimerkkijono[:8]
        ylijaamabitit = int(tayttoinfo, 2)
        bittimerkkijono = bittimerkkijono[8:]
        # poistaa lopusta lisätyt bitit
        koodattu_teksti = bittimerkkijono[:-1*ylijaamabitit]

        return koodattu_teksti

    def irroita_puu(self, bittimerkkijono):
        """Funktio, joka erottaa toisistaan merkkijonosta käsittelyä varten Huffmannin puun ja itse tekstiosan.

        Parametrit:
            bittimerkkijono ([type]): [Poista_taytto() funktion palauttama merkkijono]

        Palauttaa:
            [puu, teksti]: [Lista, jossa on kaksi alkiota: Huffmannin puu indeksissä 0, sekä koodattu teksti indeksissä 1]
        """
        # erotellaan informaatio puuhun täytetyistä biteistä
        puun_taytto_info = bittimerkkijono[:8]
        puun_taytto_info = int(puun_taytto_info, 2)
        # poistetaan täyttöinfo merkkijonosta
        bittimerkkijono = bittimerkkijono[8:]

        # erotellaan informaatio siitä, kuinka monessa bitissä puun pituus on ilmoitettu
        info_biteista = bittimerkkijono[:8]
        info_biteista = int(info_biteista, 2)
        # poistetaan täyttöinfo merkkijonosta
        bittimerkkijono = bittimerkkijono[8:]

        # erotellaan puun pituuden kertovat bitit merkkijonosta
        puun_pituus_info = bittimerkkijono[:info_biteista]
        puun_pituus_info = int(puun_pituus_info, 2)
        # poistetaan täyttöinfo
        bittimerkkijono = bittimerkkijono[info_biteista:]

        # erotellaan puu merkkijonosta
        puu = bittimerkkijono[:puun_pituus_info]
        puu = puu[puun_taytto_info:]  # poistetaan puusta täytetyt bitit
        # erotellaan teksti merkkijonosta
        teksti = bittimerkkijono[puun_pituus_info:]
        
        return [puu, teksti]
