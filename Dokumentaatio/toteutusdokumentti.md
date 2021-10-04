# Toteutusdokumentti

## Huffman

Algoritmin lukee input tiedoston tekstimuodossa ja muodostaa sanakirjan, jonka sisältö koostuu tiedostossa esiintyvistä merkeistä ja niiden ilmaantuvuudesta. Esimerkiksi jos merkki "a" esiintyy tiedostossa 43 kertaa, palauttaa sanakirja["a"] luvun 43.
Sanakirjan perusteella luodaan puurakenne, jolla voidaan muodostaa jokaiselle merkille uusi bittiesitysmuoto. Sanakirjan sisältö käydään läpi ja jokaisesta merkki,ilmaantuvuus parista luodaan HuffmanSolmu olio. Oliolla on attribuutit merkki, ilmaantuvuus, vasen_lapsi ja oikea_lapsi. Kaikki oliot lisätään listaan ja lista järjestetään ilmaantuvuuden mukaan. Listasta otetaan kaksi pienintä solmu. Luodaan uusi solmu, jonka merkki on None ja ilmaantuvuus on kahden aikaisemmin määriteltyjen solmujen ilmaantuvuuden summa, vasen lapsi on ensimmäisenä irroitettu solmu ja oikea lapsi toisena irroitettu solmu. Uusi solmu lisätään listaan ja irroitetut solmut poistetaan listasta. Tämän jälkeen lista järjestetään taas uudelleen. Prosessia toistetaan niin kauan kunnes listassa on enää 1 solmu jäljellä, jolloin puu on valmis. Puun avulla voidaan muodostaa jokaiselle merkille uusi bittiesitysmuoto. Aloitetaan juuresta, kun puussa liikutaan vasemmalle lisätään koodiin "0", kun oikealle lisätään "1", lehtisolmuun päästyä tallennetaan siihen sen uusi bittiesitysmuoto. Nyt teksti voidaan kirjoittaa binäärinä tiedostoon, mukaan täytyy myös kirjoittaa itse puu binäärinä, jotta purku onnistuu jälkeenpäin. Purkaessa puu irroitetaan bittijonosta ja muodostetaan uudelleen, jonka jälkeen sitä käytetään tekstin uudelleenkirjoittamiseen.

Huffman koodauksessa puun muodostaminen vaatii O(nlogn) verran aikaa, sillä puun koko riippuu syötteen koosta ja muodostamisessa on käytettävä järjestämistä, joka toimii logaritmisessa ajassa. Purkamisen tulisi toimia O(n) ajassa, sillä puu muodostetaan purkaessa vain lukemalla bittejä järjestyksessä.


