from fact_based import DiagnostykaDrukarki as DiagnostykaFakty
from rule_based import DiagnostykaDrukarki as DiagnostykaZasady
from enums import Komunikat, ElementDrukarki
from facts import FaktKomunikat, FaktElementDrukarki


# engine = DiagnostykaFakty()
engine = DiagnostykaZasady()
running = True
while running:
    choice = input("\nW czym mogę pomóc?\n[1] Zdiagnozuj problemy związane z częścią\n"
                   "[2] Zdiagnozuj problemy na bazie komunikatu\n\n"
                   "[0] Zakończ\n\n")
    if choice == '0':
        running = False
    else:
        my_enum = ElementDrukarki if choice == '1' else Komunikat
        my_fact = FaktElementDrukarki if choice == '1' else FaktKomunikat
        for i, element in enumerate(my_enum):
            print(f'[{i + 1}] {element.name}')
        choice = input("\nWprowadź numer części/komunikatu:\n")
        engine.reset()
        engine.declare(my_fact(my_enum(int(choice))))
        engine.run()
