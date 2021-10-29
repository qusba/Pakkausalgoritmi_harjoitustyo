# Käyttöohje

## Komennot:

Ohjelman voi käynnistää projektin päärepositoriossa komennolla: "poetry run invoke start"<br/>
Ohjelman testit voidaan ajaa komennolla: "poetry run invoke testaa"<br/>
Testien haarautumakattavuuden voi tuottaa komennolla "poetry run invoke coverage-report"

## Ohjelma käynnistämisen jälkeen:

Käynnistettyäsi ohjelman terminaaliin ilmestyy:

_"Hei! Haluatko pakata vai purkaa tiedoston?<br/>
Pakkaus = 1, purku = 2, poistu = 3<br/>
Syötä valinta:"_

Valitse tiedoston pakkaus painamalla "1","enter" tai tiedoston purku painamalla "2","enter". Halutessasi voit poistua ohjelmasta painamalla "3","enter".


### Pakkaaminen:

Painettuasi "1","enter" terminaalin ilmestyy:

_"Haluatko käyttää Huffman vai LZW -menetelmää?<br/>
Huffman = 1, LZW = 2<br/>
Syötä valinta:"_

Painamalla "1","enter" valitaan pakkaamiseen Huffman menetelmä, painamalla "2","enter" valitaan LZW.



Valittuasi kumman tahansa menetelmän terminaaliin ilmestyy:

_"Syötä tiedostopolku:"_

Kirjoita terminaaliin polku siihen tiedostoon, jonka haluat pakata, esim. /home/kayttaja/ipsum.txt.



Jos pakkaus onnistui terminaaliin ilmestyy:

_"Pakkaus valmis<br/>
(polku pakattuun tiedostoon)<br/>
Pakkaustehokkuus oli noin xx%"_


### Purku:

Painettuasi "2","enter" terminaaliin ilmestyy:

_"Haluatko käyttää Huffman vai LZW -menetelmää?<br/>
Huffman = 1, LZW = 2<br/>
Syötä valinta:"_


Jos valitset "1","enter", terminaaliin ilmestyy:

_"Syötä _Huffman.bin loppuinen tiedostopolku:"_


Jos valitset "2","enter", terminaaliin ilmestyy:

_"Syötä _LZW.bin loppuinen tiedostopolku:"_


Kirjoita pyydetyssä muodossa oleva tiedostopolku ja paina "enter".


Terminaaliin ilmestyy:

_"Purku valmis<br/>
(polku purettuun tiedostoon)_








