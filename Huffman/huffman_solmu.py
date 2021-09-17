
class Huffman_Solmu:
    def __init__(self, merkki, ilmaantuvuus, vasen_lapsi=None, oikea_lapsi=None):
        """Luokka joka on vastuussa solmujen luonnista Huffmanin puuta varten.

        Parametrit:
            merkki: [tekstissä esiintyvä merkki]
            ilmaantuvuus: [kuinka usein merkki esiintyy tekstissä]
            vasen_lapsi: [solmun vasen lapsi, oletus none].
            oikea_lapsi: [solmun oikea lapsi, oletus none].
            bittikoodi: [käsittelyn aikana muodostuva bittisekvenssi kyseiselle merkille] 
        """
        self.merkki = merkki
        self.ilmaantuvuus = ilmaantuvuus
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi
        self.bittikoodi = ""
