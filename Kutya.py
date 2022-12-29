# Kutyákról szeretnénk tárolni a nevüket, nemüket, fajukat, marmagass
# águkat, súlyukat.
#
# Hozz létre egy kutya osztályt! Az osztály adattagjait a fenti feladatspecifikáció
# alapján határozd meg.
#
# A konstruktor állítsa be az adattagok értékét!
#
# Hozz létre egy __str__ metódust, mely kiírja az adott kutya legfontosabb adatait!
#
# Példányosítsd az osztályodat, legalább 3 kutyapédányt hozz létre!
#
# Készíts egy listát, melyben eltárolod ezeket a kutya példányokat.
#
# ++ Készíts egy osztálymetódust (tagfüggvényt) tevekenyseg néven.
# A függvény írja ki, hogy a kutya  éppen ugat, alszik, vagy játszik.
# Az aktuális tevékenységet egy véletlen szám alapján döntse el!
#
# ++ Készíts egy osztálymetódust harap néven! A kutya akkor harap, ha a
# paraméterében megadott kutya éppen ugat!
import random


class Kutya:
    def __init__(self, name, sex, breed, height, weight):  # osztály konstruktora
        self.__name = name    # az osztály saját változói / adattagok
        self.sex = sex
        self.breed = breed
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.__name}{self.sex, self.breed, self.height, self.weight}"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def tevekenyseg(self):
        tev = ["ugat", "alszik", "játszik"]
        return random.choice(tev)

    def harap(self):
        harape = Kutya.tevekenyseg(self)
        if harape == "ugat":
            x = "Megharapott"
        else:
            x = "Nem harapott meg"
        return x
