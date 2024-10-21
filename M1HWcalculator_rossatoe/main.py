from functions import *

def mainFunct():
    mathList = ["Add", "Subtract", "Divide", "Multiply",
                "+", "-", "/", "x"]
    opt = 1
    while opt != 5:
        menuFunct()
        opt = verifyOptFunct(input("Select an option: "))
        if 1 <= opt <= 4:
            rpt = 1
            while rpt != 2:
                print("\n", mathList[opt-1])
                num1 = verifyFltFunct(input("Enter the first value: "))
                num2 = verifyFltFunct(input("Enter the second value: "))
                ans = calcFunct(opt, num1, num2)
                rsltsFunct(num1, num2, opt, mathList, ans)
                rpt = verifyRptFunct(input("Select an option: "))
    print("\nGoodbye!")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainFunct()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
