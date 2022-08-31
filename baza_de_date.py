import sqlite3

from typing import Dict, List, Tuple, Union


class AdministareBazaDeDate:
    
    def __init__(self, nume_baza_de_date: str) -> None:
        
        self.connection = sqlite3.connect(nume_baza_de_date)

    def _execute(self, afirmatie: str, valori: Union[List, Tuple, None] = None) -> sqlite3.Cursor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(afirmatie, valori or [])
            return cursor

    def create_table(self, nume_tabel: str, coloane: Dict[str, str]) -> None:
        continut_coloane = []
        for nume_coloana, continut_coloana in coloane.items():
            tipuri_de_date_in_coloane = f"{nume_coloana.upper()} {continut_coloana}"
            continut_coloane.append(tipuri_de_date_in_coloane)
        interogare = (
            f"CREATE TABLE IF NOT EXISTS {nume_tabel} "
            f"({', '.join(continut_coloane)});"
        )
        self._execute(interogare)

    def add(self, nume_tabel: str, date: Dict[str, Union[str, int]]) -> None:       
        valoare_inlocuitoare = ", ".join("?" * len(date))
        nume_coloana = ", ".join(date.keys())
        valoare_coloana = tuple(date.values())
        interogatie = (
            f"INSERT INTO {nume_tabel} "
                f"({nume_coloana}) "
            f"VALUES "
                f"({valoare_inlocuitoare});"
        )
        self._execute(interogatie, valoare_coloana)

    def delete(self, nume_tabel: str, element: Dict[str, str]) -> None:
        valoare_inlocuitoare = [f"{coloane} = ?" for coloane in element.keys()]
        element_de_sters = " AND ".join(valoare_inlocuitoare)
        valoare_element = tuple(element.values())
        interogatie = (
            f"DELETE FROM {nume_tabel} "
            f"WHERE {element_de_sters};"
        )
        self._execute(interogatie, valoare_element)

    def select(self, nume_tabel: str, element: Union[Dict[str, str], None] = None, sortare_dupa: Union[str, int, None] = None) -> sqlite3.Cursor:
        element = element or {}
        interogatie = f"SELECT * FROM {nume_tabel}"
        valoare_element = tuple(element.values())
        
        if element:
            valoare_inlocuitoare = [f"{coloane} = ?" for coloane in element.keys()]
            selectare_element = " AND ".join(valoare_inlocuitoare)
            interogatie += f" WHERE {selectare_element}"
        
        if sortare_dupa:
            interogatie += f" ORDER BY {sortare_dupa}"

        interogatie += ";"

        return self._execute(interogatie, valoare_element)

    def update(self,nume_tabel: str, element: Union[Dict[str, str], None] = {}, date: Union[Dict[str, str], None] = {}):
        valoare_inlocuitoare = [f"{coloane} = ?" for coloane in element.keys()]
        actualizare_element = " AND ".join(valoare_inlocuitoare)
        
        valoare_initiala = ", ".join(f"{key} = ?" for key in date.keys())
        valori = tuple(date.values()) + tuple(element.values())
        
        self._execute(
            (
                f"UPDATE {nume_tabel} "
                f"SET {valoare_initiala} "
                f"WHERE {actualizare_element};"
            ),
            valori
        )

    def drop_table(self, nume_tabel: str) -> None:
        interogare = f"DROP TABLE {nume_tabel};"
        self._execute(interogare)


    def __del__(self) -> None:
        
        self.connection.close()