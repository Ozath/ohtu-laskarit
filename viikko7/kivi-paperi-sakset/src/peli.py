from komentotehdas import Komentotehdas

class Peli:

    def __init__(self, io):
        self.io = io
        self.komentotehdas = Komentotehdas(io)

    def suorita(self):
        while True:
            self.io.kirjoita("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
            )
            pelimoodi = self.komentotehdas.hae(self.io.lue())
            if pelimoodi:
                self.io.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
                pelimoodi.pelaa()
            else:
                break