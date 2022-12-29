from Kutya import Kutya

kutya1 = Kutya('Bodri', 'kan', 'Spániel', 40, 13)
kutya2 = Kutya('Maci', 'kan', 'Bishon H.', 40, 13)
kutya3 = Kutya('Dió', 'szuka', 'Tacskó', 40, 13)

kutyak = [kutya1, kutya2, kutya3]


def adatok():
    i = 0
    fejlec = "{:<15}{:<15}{:<15}{:<15}{:<15}"
    print(fejlec.format("név", "nem", "fajta", "magasság", "súly"))
    while i < len(kutyak):
        print(f"{kutyak[i].get_name():<15}"
              f"{kutyak[i].sex:<15}"
              f"{kutyak[i].breed:<15}"
              f"{kutyak[i].height:<15}"
              f"{kutyak[i].weight:<15}")
        i += 1


def mit_csinal():
    i = 0
    while i < len(kutyak):
        x = kutyak[i].tevekenyseg()
        if x == "ugat":
            print(f"{kutyak[i].get_name()}: harap")
        else:
            print(f"{kutyak[i].get_name()}: {x}")
        i += 1


adatok()
mit_csinal()
