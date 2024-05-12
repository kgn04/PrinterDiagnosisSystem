from experta import *
from enums import ElementDrukarki, Komunikat
from facts import FaktKomunikat, FaktElementDrukarki


class Problem(Fact):
    element = Field(ElementDrukarki)
    komunikat = Field(Komunikat)
    przyczyna = Field(str)
    dzialanie = Field(str)


class DiagnostykaDrukarki(KnowledgeEngine):

    @DefFacts()
    def connections(self):
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA),
            FaktKomunikat(Komunikat.AUTODIAGNOSTYKA),
            'Temperatura zespołu nagrzewnicy nie rośnie do prawidłowej wartości w określonym czasie.',
            'Wyłącz urządzenie, odczekaj kilka sekund i włącz je ponownie. '
            'Pozostaw urządzenie bezczynne i włączone na 15 minut.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA),
            FaktKomunikat(Komunikat.AUTODIAGNOSTYKA),
            'Zespół nagrzewnicy jest zbyt gorący.',
            'Wyłącz urządzenie, odczekaj kilka sekund i włącz je ponownie. '
            'Pozostaw urządzenie bezczynne i włączone na 15 minut.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.NAGRZEWNICA),
            FaktKomunikat(Komunikat.CHLODZENIE),
            'Wnętrze urządzenia jest bardzo gorące.',
            'Urządzenie przerwie swoje bieżące zadanie drukowania i przejdzie w tryb chłodzenia. '
            'Zaczekaj, aż urządzenie przejdzie w tryb gotowości.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.MODUL_KOMUNIKACYJNY),
            FaktKomunikat(Komunikat.BLAD_LACZA),
            'Niska jakość linii telefonicznej spowodowała błąd komunikacji.',
            'Spróbuj wysłać faks ponownie.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.MODUL_KOMUNIKACYJNY),
            FaktKomunikat(Komunikat.ROZLACZONE),
            'Inna osoba lub urządzenie faksowe innej osoby zatrzymało wzywanie.',
            'Spróbuj wysłać lub odebrać ponownie.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.TONER),
            FaktKomunikat(Komunikat.BLAD_WKLADU),
            'Kaseta tonera nie jest zainstalowana prawidłowo.',
            'Osadź kasetę z tonerem pewnie w zespole bębna i ponownie zamontuj całość w urządzeniu.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.TONER),
            FaktKomunikat(Komunikat.BLAD_WKLADU),
            'Upewnij się, że używasz oryginalnych kaset z tonerem marki Brother.',
            'Używaj wyłącznie oryginalnych zespołów bębna i kaset z tonerem marki Brother.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.TONER),
            FaktKomunikat(Komunikat.MALO_TONERU),
            'Wciąż można drukować, ale urządzenie informuje, że zbliża się koniec okresu eksploatacji tonera.',
            'Zamów nową kasetę z tonerem już teraz, aby była dostępna, '
            'gdy na wyświetlaczu pojawi się komunikat WYMIEŃ TONER lub KONIEC TONERU.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.PAMIEC),
            FaktKomunikat(Komunikat.BRAK_PAMIECI),
            'Pamięć urządzenia jest pełna.',
            'Naciśnij przycisk Stop/Zakończ. Urządzenie anuluje zadanie drukowania i usunie je z pamięci.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.JEDNOSTKA_BEBNA),
            FaktKomunikat(Komunikat.DUZE_ZUZYCIE_BEBNA),
            'Czas wymienić jednostkę bębna.',
            'Wymień zespół bębna.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.JEDNOSTKA_BEBNA),
            FaktKomunikat(Komunikat.DUZE_ZUZYCIE_BEBNA),
            'Licznik jednostki bębna nie został zresetowany po zainstalowaniu nowego bębna.',
            'Zresetuj licznik zespołu bębna.'
        )
        yield Problem(
            FaktElementDrukarki(ElementDrukarki.PODAJNIK),
            FaktKomunikat(Komunikat.SPRAWDZ_ORYGINAL),
            'Dokument nie został prawidłowo ułożony lub podany bądź dokument skanowany z podajnika był zbyt długi.',
            'Wyciągnij zaciągnięty papier z zespołu podajnika.'
        )

    @Rule(AS.komunikat << FaktKomunikat(W()))
    def problemy_z_komunikatu(self, komunikat):
        for problem in self.facts.values():
            if isinstance(problem, Problem) and list(problem.values())[1][0] == list(komunikat.values())[0]:
                print("Przyczyna:", list(problem.values())[2])
                print("Działanie:", list(problem.values())[3])
                print()

    @Rule(AS.element << FaktElementDrukarki(W()))
    def problemy_z_elementu(self, element):
        for problem in self.facts.values():
            if isinstance(problem, Problem) and list(problem.values())[0][0] == list(element.values())[0]:
                print("Przyczyna:", list(problem.values())[2])
                print("Działanie:", list(problem.values())[3])
                print()
