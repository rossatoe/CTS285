from functions import *

def mainFunct():
    dataManOn = True
    while dataManOn == True:
        try:
            printMenuFunct()
            opt = input("option: ")
        except:
            print()
        match opt:
            case 1:
                ansChecker()
            case 2:
                memBank()
        printAnsFunct()
        while True:
            rpt = input("play again: y/n")
            if rpt == "n":
                dataManOn = False
                break
            elif rpt == "y":
                print()
                break
            else:
                print()


if __name__ == '__main__':
    mainFunct()

