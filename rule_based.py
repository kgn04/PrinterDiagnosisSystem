from experta import *
from enums import ElementDrukarki, Komunikat
from facts import FaktKomunikat, FaktElementDrukarki


class DiagnostykaDrukarki(KnowledgeEngine):

    @Rule(OR(FaktKomunikat(Komunikat.AUTODIAGNOSTYKA), FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA)))
    def autodiagnostyka1(self):
        print('\nPrzyczyna: Temperatura zespołu nagrzewnicy nie rośnie do prawidłowej wartości w określonym czasie.')
        print('Działanie: Wyłącz urządzenie, odczekaj kilka sekund i włącz je ponownie. '
              'Pozostaw urządzenie bezczynne i włączone na 15 minut.')

    @Rule(OR(FaktKomunikat(Komunikat.AUTODIAGNOSTYKA), FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA)))
    def autodiagnostyka2(self):
        print('\nPrzyczyna: Zespół nagrzewnicy jest zbyt gorący.')
        print('Działanie: Wyłącz urządzenie, odczekaj kilka sekund i włącz je ponownie. '
              'Pozostaw urządzenie bezczynne i włączone na 15 minut.')

    @Rule(OR(FaktKomunikat(Komunikat.CHLODZENIE), FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA)))
    def chlodzenie(self):
        print('\nPrzyczyna: Wnętrze urządzenia jest bardzo gorące.')
        print('Działanie: Urządzenie przerwie swoje bieżące zadanie drukowania i przejdzie w tryb chłodzenia. '
              'Zaczekaj, aż urządzenie przejdzie w tryb gotowości.')

    @Rule(OR(FaktKomunikat(Komunikat.BLAD_LACZA), FaktElementDrukarki(ElementDrukarki.MODUL_KOMUNIKACYJNY)))
    def blad_lacza(self):
        print('\nPrzyczyna: Niska jakość linii telefonicznej spowodowała błąd komunikacji.')
        print('Działanie: Spróbuj wysłać faks ponownie.')

    @Rule(OR(FaktKomunikat(Komunikat.ROZLACZONE), FaktElementDrukarki(ElementDrukarki.MODUL_KOMUNIKACYJNY)))
    def rozlaczone(self):
        print('Przyczyna: Inna osoba lub urządzenie faksowe innej osoby zatrzymało wzywanie.')
        print('Działanie: Spróbuj wysłać lub odebrać ponownie.')

    @Rule(OR(FaktKomunikat(Komunikat.BLAD_WKLADU), FaktElementDrukarki(ElementDrukarki.TONER)))
    def blad_wkladu1(self):
        print('\nPrzyczyna: Kaseta tonera nie jest zainstalowana prawidłowo.')
        print('Działanie: Osadź kasetę z tonerem pewnie w zespole bębna i ponownie zamontuj całość w urządzeniu.')

    @Rule(OR(FaktKomunikat(Komunikat.BLAD_WKLADU), FaktElementDrukarki(ElementDrukarki.TONER)))
    def blad_wkladu2(self):
        print('\nPrzyczyna: Upewnij się, że używasz oryginalnych kaset z tonerem marki Brother.')
        print('Działanie: Używaj wyłącznie oryginalnych zespołów bębna i kaset z tonerem marki Brother.')

    @Rule(OR(FaktKomunikat(Komunikat.MALO_TONERU), FaktElementDrukarki(ElementDrukarki.TONER)))
    def malo_toneru(self):
        print('\nPrzyczyna: Wciąż można drukować, ale urządzenie informuje, '
              'że zbliża się koniec okresu eksploatacji tonera.')
        print('Działanie: Zamów nową kasetę z tonerem już teraz, aby była dostępna, '
              'gdy na wyświetlaczu pojawi się komunikat WYMIEŃ TONER lub KONIEC TONERU.')

    @Rule(OR(FaktKomunikat(Komunikat.BRAK_PAMIECI), FaktElementDrukarki(ElementDrukarki.PAMIEC)))
    def brak_pamieci(self):
        print('\nPrzyczyna: Pamięć urządzenia jest pełna.')
        print('Działanie: Naciśnij przycisk Stop/Zakończ. Urządzenie anuluje zadanie drukowania i usunie je z pamięci.')

    @Rule(OR(FaktKomunikat(Komunikat.DUZE_ZUZYCIE_BEBNA), FaktElementDrukarki(ElementDrukarki.JEDNOSTKA_BEBNA)))
    def duze_zuzycie_bebna1(self):
        print('\nPrzyczyna: Czas wymienić jednostkę bębna.')
        print('Działanie: Wymień zespół bębna.')

    @Rule(OR(FaktKomunikat(Komunikat.DUZE_ZUZYCIE_BEBNA), FaktElementDrukarki(ElementDrukarki.JEDNOSTKA_BEBNA)))
    def duze_zuzycie_bebna2(self):
        print('\nPrzyczyna: Licznik jednostki bębna nie został zresetowany po zainstalowaniu nowego bębna.')
        print('Działanie: Zresetuj licznik zespołu bębna.')

    @Rule(OR(FaktKomunikat(Komunikat.SPRAWDZ_ORYGINAL), FaktElementDrukarki(ElementDrukarki.PODAJNIK)))
    def sprawdz_oryginal(self):
        print('\nPrzyczyna: Dokument nie został prawidłowo ułożony '
              'lub podany bądź dokument skanowany z podajnika był zbyt długi.')
        print('Działanie: Wyciągnij zaciągnięty papier z zespołu podajnika.')
