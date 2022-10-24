from abc import ABC, abstractmethod


class Czlowiek:
    imie = ""
    wiek = None
    plec = ""

    def powitanie(self):
        print("Cześć, mam na imię", self.imie)

    def spacer(self):
        if self.plec == 'k':
            print("Ruszyłam na spacer")
        else:
            print("Ruszyłem na spacer")


class Czlowiek2(ABC):
    '''
    Klasa człowiek, która tworzy instancje kolejnych kopii Człowieka.
    @:author TK
    @:param imie, __wiek, plec
    '''

    def __init__(self, imie: str, wiek=0, plec="k"):
        self.imie = imie
        self.__wiek = wiek
        self.plec = plec

    def powitanie(self):
        print("Cześć, mam na imię", self.imie)
        self.__dodaj_lata()

    def spacer(self):
        if self.plec == 'k':
            print("Ruszyłam na spacer")
        else:
            print("Ruszyłem na spacer")

    def __dodaj_lata(self):
        for i in range(5):
            self.__wiek += i
        print(self.__wiek)

    @abstractmethod
    def numSeryjny(self):
        pass


class Android(Czlowiek2):

    def __init__(self, imie):
        super().__init__(imie, wiek=0, plec='n')

    def lasery(self):
        print(f"Tu {self.imie}, będę strzelał laserem!")

    def numSeryjny(self):
        print("78534289ruynrh54353")
