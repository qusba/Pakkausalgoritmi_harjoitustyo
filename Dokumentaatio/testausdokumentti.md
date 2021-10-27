# Testausdokumentti

## Huffman

Huffmannin koodauksen funktioiden yksikkötestaus on suoritettu "testi.txt" -tiedostolla, jonka sisältö on "AAAAAABCCCCCCDDEEEEE\n". Yksikkötestaus kattaa jokaisen huffman_koodaus, huffman_pakkaus ja huffman_purku tiedostojen funktiot.
Näiden testien tarkoitus on yksinkertaisen syötteen avulla varmentaa kaikkien funktioiden antavan oikean tuloksen pakkaamisen ja purun eri vaiheissa.


## Lempel-Ziv-Welch

Lempel-Ziv-Welchin yksikkötestaus on teoteutettu samaan tapaan kuin Huffmannin yksikkötestaus, eli samalla "AAAAAABCCCCCCDDEEEEE\n" -merkkijonolla. Yksikkötestaus kattaa jokaisen LZW_koodaus, LZW_pakkaus ja LZW_purku tiedostojen funktiot. 

Molempien menetelmien testit ajetaan terminaalissa komennolla "poetry run invoke testaa". Yhteisen haarautumakattavuuden voi tuottaa komennolla "poetry run invoke coverage-report".

Alla kuva haarautumakattavuudesta:


![yhteinen_haarautumakattavuus](https://user-images.githubusercontent.com/81024277/139065406-8d9fe947-b11d-4dd6-8d57-f5b598da934c.png)


