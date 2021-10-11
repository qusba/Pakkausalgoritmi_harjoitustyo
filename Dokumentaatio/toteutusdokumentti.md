# Toteutusdokumentti

## Huffman

Algoritmin lukee input tiedoston tekstimuodossa ja muodostaa sanakirjan, jonka sisältö koostuu tiedostossa esiintyvistä merkeistä ja niiden ilmaantuvuudesta. Esimerkiksi jos merkki "a" esiintyy tiedostossa 43 kertaa, palauttaa sanakirja["a"] luvun 43. <br/>

Sanakirjan perusteella luodaan puurakenne, jolla voidaan muodostaa jokaiselle merkille uusi bittiesitysmuoto. Sanakirjan sisältö käydään läpi ja jokaisesta merkki,ilmaantuvuus parista luodaan HuffmanSolmu olio. Oliolla on attribuutit merkki, ilmaantuvuus, vasen_lapsi ja oikea_lapsi.<br/>

Kaikki oliot lisätään listaan ja lista järjestetään ilmaantuvuuden mukaan. Listasta otetaan kaksi pienintä solmua, joiden perusteella luodaan uusi solmu, jonka merkki on None ja ilmaantuvuus on kahden aikaisemmin määriteltyjen solmujen ilmaantuvuuden summa, vasen lapsi on ensimmäisenä irroitettu solmu ja oikea lapsi toisena irroitettu solmu. Uusi solmu lisätään listaan ja irroitetut solmut poistetaan listasta. Tämän jälkeen lista järjestetään taas uudelleen. Prosessia toistetaan niin kauan kunnes listassa on enää 1 solmu jäljellä, jolloin puu on valmis.<br/>

Puun avulla voidaan muodostaa jokaiselle merkille uusi bittiesitysmuoto. Aloitetaan juuresta, kun puussa liikutaan vasemmalle lisätään koodiin "0", kun oikealle lisätään "1", lehtisolmuun päästyä tallennetaan siihen sen uusi bittiesitysmuoto.<br/>

Nyt teksti voidaan kirjoittaa binäärinä tiedostoon. Mukaan täytyy myös kirjoittaa itse puu binäärinä, jotta purku onnistuu jälkeenpäin. Purkaessa puu irroitetaan bittijonosta ja muodostetaan uudelleen, jonka jälkeen sitä käytetään tekstin uudelleenkirjoittamiseen.

### Aikavaativuudesta

Huffman koodauksessa puun muodostaminen vaatii O(nlogn) verran aikaa, sillä puun koko riippuu syötteen koosta ja muodostamisessa on käytettävä järjestämistä, joka toimii logaritmisessa ajassa. Purkamisen tulisi toimia O(n) ajassa, sillä puu muodostetaan purkaessa vain lukemalla bittejä järjestyksessä.

## Lempel-Ziv-Welch

Algoritmi aloittaa luomalla sanakirjan, jonka sisältö koostuu kaikista input tiedoston merkeistä, jotka toimivat avaimina, sekä merkkejä vastaavista kokonaislukuesityksistä, jotka toimivat arvoina. Tämän jälkeen syötettä käydään läpi ja sanakirjaan aletaan tallentaa vastaan tulevia uusia monen merkin yhdisteitä, joille luodaan oma uusi kokonaislukuesitysmuoto, joka myöskin tallennetaan sankirjaan. Esimerkiksi jos tiedoston alussa esiintyisin merkkijono "aaa", toiminta on seuraavanlainen: 

Katsotaan indeksissä 0 ja 1 olevia kirjaimia, todetaan että niiden yhdiste ei ole sanakirjassa, joten lisätään se sanakirjaan arvolla 256. Arvo 256 on valittu siitä syystä että Pythonissa olemassa oleva merkistö käyttää arvot 0-255. Koska yhdiste ei ollut sanakirjassa pusketaan outputtina tulevaan tulosteeseen indeksissä 0 sijainnut arvo ja aloittava indeksi kasvaa nyt yhdellä. Seuraavaksi katsotaan indeksejä 1 ja 2, todetaan että "aa" löytyy sanakirjasta, joten tulosteeseen pusketaan "aa":n kohdalta löytyvä 256.

Algoritmin käydessä läpi tiedostoa sanakirjaan saadaan tallennettua uusia merkkiyhdisteitä, joita edustaa yksi kokonaisluku. Aikaisemmin tiedostossa yhtä merkkiä edusti aina yksi luku, mutta pakkaamisen jälkeen yksi luku voi edustaa montaa merkkiä ja näin saadaan pakkausta aikaiseksi. Algoritmi toimii paremmin, mitä enemmän tiedostossa on samankaltaisuutta.

Yksi algoritmin eduista on, että pakkaamiseen käytettyä sanakirjaa ei tarvitse tallentaa bittitiedostoon mukaan, vaan se voidaan luoda uudestaan lukiessa pelkän syötteen perusteella. Mukaan täytyy tallentaa vain, kuinka monessa bitissä luvut on ilmoitettu. 

### Aikavaativuudesta

LZW-algoritmin aikavaativuus on luokkaa O(n). Monessa kohtaa algoritmin kulkua vaaditaan n verran askelia, mutta yhtäkään sisäkkäistä silmukkaa ei tarvita. Algoritmi ei myöskään tarvitse järjestämistä, kuten Huffman. Purkaessa sankirjan muodostaminen vaatii vähintään 256 + n askelta, mikä on hieman enemmän kuin pakatessa, mutta isoilla syötteillä merkitys on olematon.


 
