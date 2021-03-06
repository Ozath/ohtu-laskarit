from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmainen_siirto)
        return siirto
