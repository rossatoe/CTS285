def verifyOptFunct(inpt):
    while True:
        try:
            inpt = int(inpt)
            if 1 <= inpt <= 5:
                return inpt
            else:
                inpt = input("Invalid option, please select an option between 1-5:")
        except ValueError:
            inpt = input("Invalid input, please select an option as an integer: ")

def verifyFltFunct(val): #Verificar los numeros
    while True:
        try:
            val = float(val)
            return val

        except ValueError:
            val = input("Invalid input, please type a number: ")

def verifyRptFunct(rpt):
    while True:
        try:
            rpt = int(rpt)
            if 1 <= rpt <= 2:
                return rpt
            else:
                rpt = input("Invalid option, please select an option between 1-2:")
        except ValueError:
            rpt = input("Invalid input, please select an option as an integer: ")


def menuFunct(): #Menu textual
    print("\n\t------------------",
          "CALCULATOR",
          "MENU",
          "------------------",
          "\n1. Add",
          "\n2. Subtract",
          "\n3. Divide",
          "\n4. Multiply",
          "\n5. Exit"
          )

def calcFunct(opt, num1, num2): #Opciones y calculo
    match opt:
        case 1: #devuelve suma
            return num1 + num2
        case 2:  # devuelve substraccion
            return num1 - num2
        case 3:  # devuelve division
            return num1 / num2
        case 4:  # devuelve multiplicacion
            return num1 * num2

def rsltsFunct(num1, num2, opt, mathList, ans):
    print(num1, mathList[opt+3], num2, " = ", ans)
    print("\n1. Repeat",
          "\n2. Main Menu")