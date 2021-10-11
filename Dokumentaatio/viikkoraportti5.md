# Viikkoraportti 5

## Mitä tehtiin?

Toteutettiin Lempel-Ziv-Welch pakkaaminen sekä purku, ja siihen kaikki docstring kommentointi. Päivitettiin toteutusdokumenttia. Tehtiin Huffmanniin muutamia parannuksia vertaisarvioinnin ehdotuksista.
## Ohjelman edistyminen:

Koko Lempel-Ziv-Welch algoritmin toteutus. Algoritmi toteutettiin ilman kiinteää bittikattoa, joka saattaisi rajoittaa isojen tiedostojen pakkausta. Algoritmi epäonnistuu vasta jos jokainen merkki tallennetaan yli 256 bittisenä.

## Mitä opin?

Tällä viikolla opittiin Lempel-Ziv menetelmistä ja etenkin LZW:stä. Myöskin saatiin taas kikkailla hieman bytearray -muuttujan kanssa. Löysin hyvän pseudon, joka oli C++ koodia, joten myös C++ tulkintaa opittiin hieman.

## Mitä teen seuraavaksi?

Lempel-Ziville kaikki yksikkötestit ja sitten jäljellä on enää dokumentaation täydennys, pienimuotoinen käyttöliittymä sekä suorituskykytestaus.

## Aika:

Aikaa käytettiin tällä viikolla noin 20h.
