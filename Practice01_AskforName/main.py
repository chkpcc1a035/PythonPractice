# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Ans = 0


def main():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    QuestionSelect = int(input(
        "Please Enter a Number to Select Questions: \n 1. Checking Is a Number is multiple of Four or Not\n 2. Check Odd or Even\n 3. Input Two Number to check"))
    if QuestionSelect == 1:
        CheckMultipleofFour()
    elif QuestionSelect == 2:
        CheckOddorEven()
    else:
        PlayNumandCheck()


def CheckMultipleofFour():
    Ans = int(input("Please Enter A Number To check is Mutiple of 4 or NOT"))
    Ans = Ans % 4
    if Ans == 0:
        print("The number you've entered is;" + Ans + "\n it is a multiple of 4 !")
    else:
        print("NO IT IS NOT multiple of 4 !")


def CheckOddorEven():
    Ans = int(input("Please Enter A Numer to Check Its Odd or Even!"))
    Ans = Ans % 2
    if Ans == 1:
        print("It is Odd!")
    else:
        print("It is Even!")


def PlayNumandCheck():
    num = int(input("Please Enter First Mumber: "))
    check = int(input("Please Enter Checking Number: "))

    Ans = num % check
    if Ans == 0:
        print("Its is evenly divide!")
    else:
        print("Its is not evenly divide!")


main()
