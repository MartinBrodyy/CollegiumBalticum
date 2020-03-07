import turtle
import time

turtle.speed(10)

sNumberOfRows = input("Enter the number of rows: ")
iNumberOfRows = int(sNumberOfRows)
sNumberOfColumn = input("Enter the number of columns: ")
iNumberOfColumn = int(sNumberOfColumn)
sSizeOfSquare = input("Enter the size of the squares: ")
iSizeOfSquare= int(sSizeOfSquare)

lColorList = ["black", "white"]

def square():
    for i in range(4):
        turtle.forward(iSizeOfSquare)
        turtle.right(90)

for i in range(iNumberOfRows):
    for j in range(iNumberOfColumn):
        turtle.penup()
        turtle.goto(j * iSizeOfSquare, i * iSizeOfSquare)
        turtle.pendown()
        if(i%2==0):
            turtle.fillcolor(lColorList[j%2==0])
        else:
            turtle.fillcolor(lColorList[j%2!=0])
        turtle.begin_fill()
        square()
        turtle.end_fill()

time.sleep(10)
