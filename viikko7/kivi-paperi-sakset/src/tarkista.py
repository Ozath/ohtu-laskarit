class Tarkista:

    def tasapeli(self, eka, toka):
        if eka == toka:
            return True
        return False
   
    def eka_voittaa(self, eka, toka):
        if eka == "k" and toka == "s":
            return True
        elif eka == "s" and toka == "p":
            return True
        elif eka == "p" and toka == "k":
            return True
        return False