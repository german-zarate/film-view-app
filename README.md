# Elokuva-arvostelusovellus

Sovelluksessa listataan tietoa elokuvista, joille käyttäjät voivat kirjoittaa arvosteluita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä. Ylläpitäjällä on oikeus hallinnoida käyttäjätilejä ja elokuvia sekä niiden tietoja.

## Testaaminen

Sovellusta voi testata osoitteessa https://tsoha-elokuvasovellus.herokuapp.com/  
Toistaiseksi sovelluksessa on vain rekisteröitymis- ja kirjautumistoiminnallisuus. Sovelluksessa on yksi pääkäyttäjä, jonka tunnus on *admin* ja salasana *password*. Vain tälle käyttäjälle on näkyvissä painike, jolla voidaan lisätä uusi elokuva sovellukseen. Tämä toiminnallisuus ei ole kuitenkaan vielä valmiina eikä linkin tulekaan vielä toimia.

## Ominaisuudet

- Sivustolla listataan tietokannasta löytyvät elokuvat ja elokuvan nimeä klikkaamalla saadaan näkyviin lisää tietoa elokuvasta:
  - Nimi
  - Kuvaus
  - Lajityyppi (genre)
  - Julkaisuvuosi
  - Julkaisumaa
  - Kieli
  - Ohjaaja
  - Käsikirjoittaja
  - Mahdollisesti muita oleellisia tietoja
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä voi antaa arvion elokuvasta ja lukea muiden antamia arvioita
  - Numeroarvosana esim. 1-10
    - Numeroarvosanoista lasketaan keskiarvo, joka on elokuvan "arvosana" sivustolla
  - Sanallinen arvostelu
- Käyttäjä voi hakea elokuvia elokuvan nimen, kuvauksen tai lajityypin perusteella
- Elokuvalistaus on mahdollista ladata aakkosjärjestyksessä tai arvosanan perusteella parhaimmasta huonoimpaan
- Ylläpitäjä voi lisätä ja poistaa elokuvia
- Ylläpitäjä voi muokata käyttäjän tai elokuvan tietoja
- Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion
