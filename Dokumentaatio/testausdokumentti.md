# Testausdokumentti

## Huffman

Huffmannin koodauksen funktioiden yksikkötestaus on suoritettu "testi.txt" -tiedostolla, jonka sisältö on "AAAAAABCCCCCCDDEEEEE\n". Yksikkötestaus kattaa jokaisen huffman_koodaus, huffman_pakkaus ja huffman_purku tiedostojen funktiot.
Näiden testien tarkoitus on yksinkertaisen syötteen avulla varmentaa kaikkien funktioiden antavan oikean tuloksen pakkaamisen ja purun eri vaiheissa.


## Lempel-Ziv-Welch

Lempel-Ziv-Welchin yksikkötestaus on teoteutettu samaan tapaan kuin Huffmannin yksikkötestaus, eli samalla "AAAAAABCCCCCCDDEEEEE\n" -merkkijonolla. Yksikkötestaus kattaa jokaisen LZW_koodaus, LZW_pakkaus ja LZW_purku tiedostojen funktiot. 

Molempien menetelmien testit ajetaan terminaalissa komennolla "poetry run invoke testaa". Yhteisen haarautumakattavuuden voi tuottaa komennolla "poetry run invoke coverage-report".

Alla kuva haarautumakattavuudesta:


![yhteinen_haarautumakattavuus](https://user-images.githubusercontent.com/81024277/139065406-8d9fe947-b11d-4dd6-8d57-f5b598da934c.png)

## Suorituskykytestaus

Molempien algoritmien pakkaustehoa testattiin seitsemällä eri tekstitiedostolla, joiden koot olivat noin 0.00002mb, 0.1mb, 0.2mb, 0,4mb, 0,6mb, 1mb, 2mb.
Tiedostoista kaikki paitsi ensimmäinen sisälsivät tietokoneen tuottamaa lorem ipsumia.

Alla graafinen esitys algoritmien suorituskyvystä:


![Figure_1](https://user-images.githubusercontent.com/81024277/139428709-f89afec1-3028-4a18-9aec-15d24ffb8c64.png)

Testauksen perusteella vaikuttaisi siltä, ettei Huffman algoritmini suorituskyky pääse 47% korkeammalle. Huffmannin teho on parhaimmillaan silloin kun joitain yksittäisiä merkkejä esiintyy huomattavasti enemmän kuin toisia. Tietokoneen tuottamassa lorem ipsumissa tulokset näyttäisivät olevan hyvin tasaisia.

LZW algoritmin suorituskyky näytti lorem ipsumin kanssa kasvavan tiedostokoon kasvaessa. Paras tulos saatiin 2mb kokoisella tiedostolla, jolloin pakkausteho oli jopa 90%. LZW algoritmi toimii parhaiten silloin kun tiedostossa on paljon toistoa. Vaikka käytetty lorem ipsum teksti oli tietokoneella "satunnaisesti" luotua, sisältää se varmasti paljon toistoa varsinkin isompia tiedostoja luodessa.

Molemmat algoritmit toimivat todella heikosti pienimmän tiedoston kanssa, jolloin pakkaustehot olivat vain 14% Huffmannilla ja 19% Lempel-Ziv-Welchillä. Algoritmeja ei ole suunniteltu pienille tiedostoille, eikä toisaalta pieneten tiedostojen pakkaaminen ole kovin mielekästä.

Molemmilla algortimeilla saavutettu suorituskyky vastasi määrittelydokumentissa toivottua 40-60% tasoa. Lorem ipsumin tapauksessa LZW-algoritmi jopa ylitti sen kirkkaasti.




