class Zakaznik:
    def __init__(self, jmeno, prijmeni, telefon, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

class Pojistovna:
    def __init__(self):
        self.zakaznici = []

    def pridej_zakaznika(self, jmeno, prijmeni, telefon, vek):
        zakaznik = Zakaznik(jmeno, prijmeni, telefon, vek)
        self.zakaznici.append(zakaznik)
        print("----------------------")
        print("Nový zákazník byl přidán.")

    def vypis_vsechny_zakazniky(self):
        if len(self.zakaznici) == 0:
            print("----------------------")
            print("Pojišťovna nemá žádného zákazníka.")
        else:
            print("----------------------")
            print("Seznam všech zákazníků:")
            for zakaznik in self.zakaznici:
                print("Jméno:", zakaznik.jmeno)
                print("Příjmení:", zakaznik.prijmeni)
                print("Telefon:", zakaznik.telefon)
                print("Věk:", zakaznik.vek)
                print("----------------------")
                
    def vyhledej_zakaznika(self, jmeno, prijmeni):
        nalezeny_zakaznik = []
        for zakaznik in self.zakaznici:
            if zakaznik.jmeno == jmeno and zakaznik.prijmeni == prijmeni:
                nalezeny_zakaznik.append(zakaznik)
        
        if len(nalezeny_zakaznik) == 0:
            print("----------------------")
            print("Zákazník s tímto jménem a příjmením nebyl nalezen.")
        else:
            print("----------------------")
            print("Nalezený zákazník:")
            for zakaznik in nalezeny_zakaznik:
                print("Jméno:", zakaznik.jmeno)
                print("Příjmení:", zakaznik.prijmeni)
                print("Telefon:", zakaznik.telefon)
                print("Věk:", zakaznik.vek)
                
pojistovna = Pojistovna()

while True:
    print("-----------------------")
    print("Evidence pojištěných")
    print("-----------------------")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = input("Vyberte si akci:\n")

    if volba == "1":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        telefon = input("Zadejte telefoní číslo:\n")
        vek = int(input("Zadjete věk:\n"))
        pojistovna.pridej_zakaznika(jmeno, prijmeni, telefon, vek)

    elif volba == "2":
        pojistovna.vypis_vsechny_zakazniky()

    elif volba == "3":
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        pojistovna.vyhledej_zakaznika(jmeno, prijmeni)

    elif volba == "4":
        break

    else:
        print("Neplatná volba. Zadejte číslo 1-4.")