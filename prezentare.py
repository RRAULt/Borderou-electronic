import os

from typing import Callable, Dict, Union

import comenzi


class Obtiuni:
    def __init__(self, nume: str, comanda: comenzi.Comanda, prep_call: Callable = None):
        self.nume = nume
        self.comanda = comanda
        self.prep_call = prep_call

    def _handle_message(self, mesaj: Union[str, list]):
        if isinstance(mesaj, list):
            for intrare in mesaj:
                print(intrare)
        else:
            print(mesaj)

    def choose(self):
        date = self.prep_call() if self.prep_call else None
        mesaj = self.comanda.execute(date) if date else self.comanda.execute()
        self._handle_message(mesaj)

    def __str__(self):
        return self.nume


def printare_obtiuni(obtiuni: Dict[str, Obtiuni]):
    for litera_corespunzatoare, obtiune in obtiuni.items():
        print(f" {litera_corespunzatoare}) {obtiune}")
    print()


def validare_obtiune_aleasa(obtiune_aleasa: str, obtiuni: Dict[str, Obtiuni]) -> bool:
    return obtiune_aleasa in obtiuni or obtiune_aleasa.upper() in obtiuni


def alege_optiune_disponibila(obtiuni: Dict[str, Obtiuni]) -> Obtiuni:
    obtiune_aleasa = input("Alege o obtiune: ")
    while not validare_obtiune_aleasa(obtiune_aleasa, obtiuni):
        print("Alegere gresita!\nAlege o obtiune valida!")
        obtiune_aleasa = input("Alege o obtiune: ")
    return obtiuni[obtiune_aleasa.upper()]


def obtine_input_utilizator(eticheta:Union[str, int], obligativitate_completare: bool = True) -> Union[str, None]:
    informatie_inserata = input(f"{eticheta}: ") or None
    while obligativitate_completare and not informatie_inserata:
        informatie_inserata = input(f"{eticheta}: ") or None
    return informatie_inserata.title()


def obtine_informatie_noua() -> dict:
    return {
        "nume_complet": obtine_input_utilizator("Nume si prenume"),
        "domiciliu": obtine_input_utilizator("Domiciliu"),
        "denumirea_speciei_culese": obtine_input_utilizator("Denumirea speciei culese din flora salbatica"),
        "cantitate": obtine_input_utilizator("Cantitate(kg)"),         
        "pret": obtine_input_utilizator("Pret")
    }


def obtine_actualizare_borderou() -> dict:
    numar_coloana = int(obtine_input_utilizator("Introduceti id-ul randului pe care doriti sa il modificati"))
    camp = obtine_input_utilizator("Alege valoarea pe care doresti sa o modifici(nume_complet,domiciliu, denumirea_speciei_culese, cantitate, pret)")
    valoare_noua = obtine_input_utilizator(f"Introduceti noua valoare {camp}")
    return {
        "id": numar_coloana,
        "update": {
            camp: valoare_noua
        }
    }


def ecran_curat():
    clear_command = "cls" if os.name == "nt" else "clear"
    os.system(clear_command)


def obtine_id():
    return int(obtine_input_utilizator("Introduceti id-ul aferent informatiei pe care doriti sa o vedeti"))