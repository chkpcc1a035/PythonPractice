def FindDivisors():
    InputDigi = int(input("Enter a Digi: "))
    InputDigList = []
    AnsList = []

    InputDigList = range(1, InputDigi + 1)

    for elem in InputDigList:
        if InputDigi % elem == 0 :
            AnsList.append(elem)

    print(AnsList)
FindDivisors()


