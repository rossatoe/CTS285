from calculator.M1HWfunctions_rossatoe import *

def Menu():
  opt = 0
  while(opt !=5):
    print("\n\t----------")
    print("\t   MENU")
    print("\t----------\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    while True:
      optStr = input("\nEnter the number of an option: ")
      if VerifyIntFunc(optStr):
        opt = int(optStr)
        break
      else:
        print("\nInvalid input. Please enter an integer.")
    print("")
    match opt:
      case 1:
        AddFunct()
      case 2:
        SubsFunct()
      case 3:
        DivFunct()
      case 4:
        MultFunct()
      case 5:
        print("Goodbye!")
      case _:
        print("Invalid Option, please try again.")
      
Menu()
