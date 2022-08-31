import sys

from typing import Dict, Union


from baza_de_date import AdministareBazaDeDate


baza_de_date = AdministareBazaDeDate("borderou_electronic.db")


class Comanda:
    def execute(self): pass


class ComandaCreareTabel(Comanda):
    def execute(self):
        baza_de_date.create_table(
            nume_tabel="borderou_electronic",
            coloane ={
                "id": "integer primary key autoincrement",
                "nume_complet": "text not null",
                "domiciliu": "text not null",
                "denumirea_speciei_culese": "text not null",
                "cantitate": "text not null",
                "pret": "text not null",
            }
        )

class ComandaInserareDate(Comanda):
    def execute(self, date: Dict[str, str]) -> str:
        baza_de_date.add(
            nume_tabel = "borderou_electronic", 
            date = date
        )
        return "Informatie adaugata!"


class ComandaListareInformatie(Comanda):
    def __init__(self, sortare_dupa: str = "nume_complet") -> None:
        self.sortare_dupa = sortare_dupa

    def execute(self):
        cursor = baza_de_date.select("borderou_electronic", sortare_dupa=self.sortare_dupa)
        rezultat = cursor.fetchall()
        return rezultat


class ComandaAfisareDate(Comanda):
    def execute(self, date: int):
        return baza_de_date.select(
            "borderou_electronic",
            {
                "id": date
            }
        ).fetchone()


class ComandaEditareInformatie(Comanda):
    def execute(self, date: Dict[str, str]):
        baza_de_date.update(
            "borderou_electronic",
            {
                "id": date["id"]
            },
            date["update"]
        )
        return "Informatie actualizata!"


class ComandaStergereInformatie(Comanda):
    def execute(self, date: str) -> str:
        baza_de_date.delete("borderou_electronic", {"id": date})
        return "Rand sters!"

class ComandaIesire(Comanda):
    def execute(self):
        sys.exit()