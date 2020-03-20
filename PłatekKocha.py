import turtle
import time

turtle.speed(10)

sLength = input("Podaj długość odcinka: ")
sOrder = input("Podaj głębokość: ")

iLength = int(sLength)
iOrder = int(sOrder)

def koch(iLength, iOrder):
    if iOrder == 0:
        turtle.forward(iLength)
        return
    iLength /= 3.0
    koch(iLength, iOrder-1)
    turtle.left(60)
    koch(iLength, iOrder-1)
    turtle.right(120)
    koch(iLength, iOrder-1)
    turtle.left(60)
    koch(iLength, iOrder-1)

koch(iLength, iOrder)

for i in range (2):
    turtle.right(120)
    koch(iLength, iOrder)

time.sleep(100)