from enum import Enum


class Komunikat(Enum):
    AUTODIAGNOSTYKA = 1
    BLAD_LACZA = 2
    BLAD_WKLADU = 3
    BRAK_PAMIECI = 4
    CHLODZENIE = 5
    DUZE_ZUZYCIE_BEBNA = 6
    MALO_TONERU = 7
    ROZLACZONE = 8
    SPRAWDZ_ORYGINAL = 9


class ElementDrukarki(Enum):
    NAGRZEWNICA = 1
    MODUL_KOMUNIKACYJNY = 2
    TONER = 3
    PAMIEC = 4
    JEDNOSTKA_BEBNA = 5
    PODAJNIK = 6