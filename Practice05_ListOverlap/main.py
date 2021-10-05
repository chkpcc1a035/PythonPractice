import random

ranList01 = []
ranList02 = []


def ListOverLap():
    ranList01 = range(1, random.randint(1, 50))
    ranList02 = range(1, random.randint(1, 50))

    print("Total length of List 01 :" + str(ranList01))
    print("Total length of List 02 :" + str(ranList02))
    for elem in ranList01:
        if elem in ranList02:
            print(elem)
    print(elem + 1)  # since the last digi will be n-1, need to fill back 1 digi


ListOverLap()
