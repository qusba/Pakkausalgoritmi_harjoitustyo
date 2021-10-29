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

Molempien algoritmien pakkaustehoa testattiin seitemällä eri tekstitiedostolla, joiden koot olivat noin 0.00002mb, 0.1mb, 0.2mb, 0,4mb, 0,6mb, 1mb, 2mb.
Tiedostoista kaikki paitsi ensimmäinen sisälsivät tietokoneen tuottamaa lorem ipsumia.

Alla graafinen esitys algoritmien suorituskyvystä:


![Figure_1](https://user-images.githubusercontent.com/81024277/139428709-f89afec1-3028-4a18-9aec-15d24ffb8c64.png)




