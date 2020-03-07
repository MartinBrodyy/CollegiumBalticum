import turtle
import time

turtle.speed(10)

wiersze = input("Podaj ilość wierszy: ")
wiersze = int(wiersze)
kolumny = input("Podaj ilość kolumn: ")
kolumny = int(kolumny)
wielkosc = input("Podaj wielkosc kwadratu: ")
wielkosc= int(wielkosc)

def kwadrat():
    for i in range(4):
        turtle.forward(wielkosc)
        turtle.right(90)

for i in range(wiersze):
    for j in range(kolumny):
        turtle.penup()
        turtle.goto(j * wielkosc, i * wielkosc)
        turtle.pendown()
        if(i%2==0):
            if(j%2==0):
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")
        else:
            if (j%2 == 0):
                turtle.fillcolor("white")
            else:
                turtle.fillcolor("black")
        turtle.begin_fill()
        kwadrat()
        turtle.end_fill()

time.sleep(10)

# 1. Proszę pamiętać że programujemy po angielsku :)
# 2. Fajnie że nazwy zmiennych są czytelne. Proszę tylko zastosować język angielski i pewną konwencję, np.
# camelCase: czyliNazwaJestPisanaWTenSposób
# zmienne_oddzielone_dolnymi_spacjami
# sNameOfUser
# iNumberOfColumn
# to już jest idealne nazwenictwo: Po angielsku, czytelne, oraz pokazuje jakiego typu jest zmienna.
# 3. Mega zwięźle napisane, chyba najkrótszy kod do tej pory jaki widziałem ;)
# 4. Gdyby się uprzeć, można sparametryzować także kolory. Zamiast black/white, można stworzyć listę kolorów i używać ich jako param:
# lColorList = ["black", "white"]
# następnie posługując sie lColorList[j%2==0] wybierze sam odpowiedni kolor ;)