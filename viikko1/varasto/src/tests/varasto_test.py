import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):

    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

# added tests

    def test_luoto_negatiivinen_varaston_tilavuus_nollataan(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_luoto_negatiivinen_varaston_saldo_nollataan(self):
        self.varasto = Varasto(10,alku_saldo = -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_negatiivista_saldoa_varastoon(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_saldoa_yli_tilavuuden_varastoon(self):
        self.varasto = Varasto(10)
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_varastosta(self):
        self.varasto = Varasto(10)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),10)

    def test_saldoa_isompi_otto_varastosta(self):
        self.varasto = Varasto(10,2)
        saatu_maara = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(saatu_maara, 2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_print_fuction(self):
        self.varasto = Varasto(10)
        self.assertAlmostEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')
