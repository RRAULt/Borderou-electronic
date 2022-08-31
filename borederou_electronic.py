from collections import OrderedDict

import comenzi

from prezentare import ( Obtiuni,
    printare_obtiuni,
    alege_optiune_disponibila,
    ecran_curat,
    obtine_informatie_noua,
    obtine_actualizare_borderou,
    obtine_id,
)



def loop():
    options = OrderedDict(
        {
            "A": Obtiuni("Adauga date in tabel", comenzi.ComandaInserareDate(), prep_call = obtine_informatie_noua),
            "B": Obtiuni("Afisare date din borderou", comenzi.ComandaAfisareDate(), prep_call= obtine_id),
            "C": Obtiuni("Listare informatie din borderou in ordine alfabetica dupa nume", comenzi.ComandaListareInformatie()),
            "D": Obtiuni("Listare informatie din borderou dupa kg", comenzi.ComandaListareInformatie(sortare_dupa ="cantitate")),
            "E": Obtiuni("Edicare borderou", comenzi.ComandaEditareInformatie(), prep_call= obtine_actualizare_borderou),
            "F": Obtiuni("Stergere element din borderou", comenzi.ComandaStergereInformatie(), prep_call= obtine_id),
            "Q": Obtiuni("Exit aplicatie", comenzi.ComandaIesire())
        }
    )

    ecran_curat()
    printare_obtiuni(options)
    optiune_aleasa = alege_optiune_disponibila(options)
    ecran_curat()
    optiune_aleasa.choose()
    _ = input("\nPentru a reveni la meniu apasa pe 'ENTER'")

if __name__ == "__main__":
    print("Bine ati venit in aplicatia Borderoul electronic!")
    comenzi.ComandaCreareTabel().execute()
    
    while True:
        loop()