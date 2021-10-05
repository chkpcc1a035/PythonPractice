array = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newarr = []

def main():
    StyleSelect = int(input("Please Select A Style: \n 1. List Number Smaller than 5 \n 2. Enter a Number To List out smaller numbers \n 3. Make a new list by number under 5"))
    if StyleSelect == 1:
        for element in array:
            if element < 5:
                print(element)
    elif StyleSelect == 2:
        num = int(input("Please Enter a Digi: "))
        for element in array:
            if element < num:
                print(element)
    else:
        for element in array:
            if element < 5:
                newarr.append(element)

        print(newarr)
main()
