# Testausdokumentti

## Huffman

Huffmannin koodauksen funktioiden yksikkötestaus on suoritettu "testi.txt" -tiedostolla, jonka sisältö on "AAAAAABCCCCCCDDEEEEE\n". Yksikkötestaus kattaa jokaisen huffman_koodaus, huffman_pakkaus ja huffman_purku tiedostojen funktiot.
Näiden testien tarkoitus on yksinkertaisen syötteen avulla varmentaa kaikkien funktioiden antavan oikean tuloksen pakkaamisen ja purun eri vaiheissa.

Alla kuva haarautuvuuskattavuudesta:
![huffman_testikattavuus](https://user-images.githubusercontent.com/81024277/135897029-0069cef3-6b78-4023-9d2b-5b7ad4c4e3f9.png)


## Lempel-Ziv-Welch

Lempel-Ziv-Welchin yksikkötestaus on teoteutettu samaan tapaan kuin Huffmannin yksikkötestaus, eli samalla "AAAAAABCCCCCCDDEEEEE\n" -merkkijonolla. Yksikkötestaus kattaa jokaisen LZW_koodaus, LZW_pakkaus ja LZW_purku tiedostojen funktiot. 

Alla kuva Haarautuvuuskattavuudesta:
![LZW_coverage](https://user-images.githubusercontent.com/81024277/137769379-9b0187a2-07b2-4d3c-9fde-14b28a852988.png)

Molempien menetelmien testit ajetaan terminaalissa komennolla "poetry run invoke testaa". Yhteisen haarautumakattavuuden voi tuottaa komennolla "poetry run invoke coverage-report".


