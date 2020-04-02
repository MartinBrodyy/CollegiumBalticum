import random
import time

#Seed losowości
random.seed(time.time())

lRandomList = []

for i in range(10):
    iRandomNumber = random.randint(0, 500)
    lRandomList.append(iRandomNumber)

#Wyświetlenie nie posortowanej tablicy
print("Lista nieposortowana:")
print(lRandomList)
iLenList = len(lRandomList)

#Szukana liczba
print("Podaj liczbę której szukasz.")
sSearched = input()
iSearched = int(sSearched)

for i in range(iLenList):
    if(iSearched == lRandomList[i]):
        print("Szukana przez Ciebie liczba znajduje się w ",i," indeksie tablicy.")
        break
    else:
        if(i == iLenList-1):
            print("W tablicy nie ma twojej liczby.")
