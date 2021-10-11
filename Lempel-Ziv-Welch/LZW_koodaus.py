import math


class LZWKoodaus():
    """Luokka, jossa on kaikki funktiot, joita tarvitaan tiedon pakkaamiseen ja purkamiseen Lempel-Ziv-Welch menetelmällä.

    """

    def __init__(self, inputpolku):
        """Luokan konstruktori.

        Parametrit:
            inputpolku: [Polku tiedostoon, joka halutaan pakata.]
        """
        self.input_polku = inputpolku

    def luo_tuloste_pakatessa(self, teksti):
        """Funktio, joka luo tulosteen, mikä koostuu kirjainten ja kirjainyhdistelmien kokonaislukuesityksistä.
        Hyödyntää pakkaussanakirjaa luodakseen kirjainyhdistelmille kokonaislukuarvoja, jotka ylittävät luvun 256.

        Parametrit:
            teksti: [Pakattavan tiedoston sisältämä teksti.]

        Palauttaa:
            tuloste: [Lista kokonaisluvuista, jotka muutetaan biteiksi.]
        """

        pakkaus_sanakirja = {}
        for merkki in teksti:
            if merkki not in pakkaus_sanakirja:
                pakkaus_sanakirja[merkki] = ord(merkki)

        uusi_arvo = 256
        nykyinen = teksti[0]
        uusi = ""
        i = 0
        tuloste = []

        while i < len(teksti):
            if i != len(teksti)-1:
                uusi += teksti[i+1]

            if nykyinen + uusi in pakkaus_sanakirja:
                nykyinen = nykyinen + uusi
                if i == len(teksti)-1:
                    tuloste.append(pakkaus_sanakirja[nykyinen])

            else:
                tuloste.append(pakkaus_sanakirja[nykyinen])
                pakkaus_sanakirja[nykyinen + uusi] = uusi_arvo
                uusi_arvo += 1
                nykyinen = uusi

            uusi = ""
            i += 1
        return tuloste

    def muuta_tuloste_biteiksi(self, tuloste):
        """Funktio laskee tuloste -listan isoimman kokonaisluvun perusteella kuinka monta bittiä tarvitaan lukujen esittämiseen.
        Tämän jälkeen tuloste -listan sisältö muutetaan lasketun x-bitin formaattiin ja kirjoitetaan bittikoodi nimiseen merkkijonoon.
        Tallentaa myös tiedon siitä, kuinka monessa bitissä kokonaisluvut ovat ilmoitettu kahdeksan bitin formaatissa ja lisää tiedon
        bittikoodin eteen.

        Parametrit:
            tuloste: [Lista kokonaisluvuista, jotka muutetaan biteiksi.]

        Palauttaa:
            bittikoodi: [Merkkijono, johon on kirjoitettu tuloste -listan sisältö x-bitin formaatissa.]
        """

        isoin_luku = max(tuloste)
        tarvittavat_bitit = math.ceil(math.log(isoin_luku, 2)+0.1)
        info_biteistä = "{0:08b}".format(tarvittavat_bitit)

        tarvittavat_bitit = "0"+str(tarvittavat_bitit)+"b"
        bittikoodi = ""
        for luku in tuloste:
            luku = format(luku, tarvittavat_bitit)
            bittikoodi += luku
        bittikoodi = info_biteistä + bittikoodi

        return bittikoodi

    def tayta_tavut(self, bittikoodi):
        """Funktio täyttää bittikoodin kahdeksalla jaolliseksi, jotta se voidaan tallentaa bytearray -muuttujaan.

        Parametrit:
            bittikoodi: [muuta_tuloste_biteiksi -funktion palauttama bittikoodi.]

        Palauttaa:
            bittikoodi: [Uusi bittikoodi, joka on nyt kahdeksalla jaollinen.]
        """

        taytto = 8 - (len(bittikoodi) % 8)
        taytto_info = "{0:08b}".format(taytto)
        for i in range(taytto):
            bittikoodi += "0"

        bittikoodi = taytto_info + bittikoodi
        return bittikoodi

    def muuta_bittikoodi_tavuiksi(self, bittikoodi):
        """Funktio muuttaa merkkijonon bittikoodi tavuiksi ja tallentaa ne bytearray -muuttujaan.

        Parametrit:
            bittikoodi: [tayta_tavut -funktion palauttama kahdeksalla jaollinen bittikoodi.]

        Palauttaa:
            tavut: [Bittikoodi -muuttuja tallennettuna oikeiksi tavuiksi. Valmis kirjoitettavaksi tiedostoon.]
        """

        tavut = bytearray()

        for i in range(0, len(bittikoodi), 8):
            tavu = bittikoodi[i:i+8]
            tavut.append(int(tavu, 2))
        return tavut

    def poista_taytto(self, bittikoodi):
        """Funktio poistaa luetun tiedoston pakkausprosessissa lisätyn täytön.

        Parametrit:
            bittikoodi: [Purettavan tiedoston sisältämä bitti-informaatio muutettuna merkkijonoksi.]

        Palauttaa:
            bittikoodi: [Merkkijono, josta on poistettu pakatessa lisätty täyttö.]
        """

        taytto_info = bittikoodi[:8]
        bittikoodi = bittikoodi[8:]
        taytto_info = int(taytto_info, 2)
        bittikoodi = bittikoodi[:-1*taytto_info]

        return bittikoodi

    def muuta_bitit_tulosteeksi(self, bittikoodi):
        """Funktio muuttaa merkkijonossa bittikoodi olevan informaation takaisin listaksi kokonaislukuja.

        Parametrit:
            bittikoodi: [poista_taytto -funktion palauttama merkkijono.]

        Palauttaa:
            tuloste: [Lista kokonaislukuja, sama muoto kuin pakatessa.]
        """

        x_bittisyys = bittikoodi[:8]
        x_bittisyys = int(x_bittisyys, 2)
        bittikoodi = bittikoodi[8:]
        tuloste = []

        for i in range(0, len(bittikoodi), x_bittisyys):
            luku = bittikoodi[i:i+x_bittisyys]
            luku = int(luku, 2)
            tuloste.append(luku)
        return tuloste

    def muuta_tuloste_tekstiksi(self, tuloste):
        """Funktio muuttaa listan kokonaislukuja takaisin tekstiksi. Luo samanlaisen sanakirjan kuin luo_tuloste_pakatessa -funktio,
        jonka avulla tuloste muutetaan takaisin tekstiksi. Käytännössä luo_tuloste_pakatessa -funktion käänteisfunktio.

        Parametrit:
            tuloste: [Lista kokonaislukuja.]

        Palauttaa:
            lopputulos: [Valmis merkkijono, joka voidaan kirjoittaa tiedostoon.]
        """

        sanakirja = {}
        for i in range(256):
            sanakirja[i] = chr(i)

        uusi_arvo = 256
        nykyinen = tuloste[0]
        teksti = sanakirja[nykyinen]
        lisays = teksti[0]

        for i in range(len(tuloste)-1):
            uusi = tuloste[i+1]
            if uusi not in sanakirja:
                teksti = sanakirja[nykyinen]
                teksti = teksti + lisays
            else:
                teksti = sanakirja[uusi]

            lisays = ""
            lisays = teksti[0]
            sanakirja[uusi_arvo] = sanakirja[nykyinen] + lisays
            uusi_arvo += 1
            nykyinen = uusi

        lopputulos = ""
        for arvo in tuloste:
            lopputulos += sanakirja[arvo]

        return lopputulos
