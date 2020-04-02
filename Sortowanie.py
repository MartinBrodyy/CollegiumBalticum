import random
import time

#Seed losowości
random.seed(time.time())

lRandomList = []
iVariable = 0

for i in range(10):
    iRandomNumber = random.randint(0, 500)
    lRandomList.append(iRandomNumber)

#Wyświetlenie nie posortowanej tablicy
print(lRandomList)
iLenList = len(lRandomList)

while True:
    iCounter = 0
    for i in range(iLenList-1):
        if (lRandomList[i+1] > lRandomList[i]):
            i += 1
        else:
            iVariable = lRandomList[i]
            lRandomList[i] = lRandomList[i+1]
            lRandomList[i+1] = iVariable
            i += 1
            iCounter += 1
    if (iCounter == 0):
        print(lRandomList)
        break