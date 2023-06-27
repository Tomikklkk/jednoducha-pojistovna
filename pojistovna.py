from zakaznik import Zakaznik

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
                
