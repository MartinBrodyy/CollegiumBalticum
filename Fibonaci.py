iNumberOne = 0
iNumberTwo = 1

sLength = input("Podaj ile liczb ciągu chcesz zobaczyć.")
iLength = int(sLength)

def fibonacci(iNumberOne, iNumberTwo, iLength):
    print(iNumberOne,"|",iNumberTwo)
    iNumberOne = iNumberOne + iNumberTwo
    iNumberTwo = iNumberOne + iNumberTwo
    if (iLength > 0):
        iLength -= 1
        return fibonacci(iNumberOne, iNumberTwo, iLength)
    else:
        return

fibonacci(iNumberOne, iNumberTwo, iLength)