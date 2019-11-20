import math
import threading

plik = open("listaNazwILiczb2.txt", "r")


def funkcja(strNazwa, intLiczba):
    #Wersja zapisu dla mnie
    gdzie_zapisac = "/Users/martinbrody/Desktop/1 Studia/Programowanie/Zadanie2/wyniki/" + strNazwa
    zapis = open(gdzie_zapisac, "w")
    #Zapis dzialajacy na kazdym komputerze
    #zapis = open(strNazwa, "w")

    licznik = 0
    x = intLiczba
    while licznik < 1500:
        x = x + math.sin(x) * math.cos(x) * math.tan(x) * 1.000000000087 * math.pi
        print(x)
        wynik = str(x)
        zapis.write(wynik + "\n")
        licznik += 1
    zapis.close()

#Sprawdzenie jak duzo linii przechowuje plik
dlugosc_pliku = plik.readlines()
dlugosc = len(dlugosc_pliku)
plik.seek(0)

for i in range(dlugosc):
    lista_z_pliku = plik.readline()
    nazwa, liczba = lista_z_pliku.split(";")
    intLiczba = int(liczba)
    strNazwa = nazwa + ".txt"
    print(strNazwa, "   ", intLiczba)
    t = threading.Thread(target=funkcja, daemon=False, args=(strNazwa, intLiczba))
    t.start()
    #funkcja(strNazwa, intLiczba)


plik.close()
