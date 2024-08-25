

def VerifyIntFunc(input):
  try:
    int(input)
    return True
  except ValueError:
    return False
    

def AddFunct():
  ext = False
  rpt = ""
  while ext == False:
    print("You chose Addition")
    while True:
      num1Str = input("\nEnter a number: ")
      if VerifyIntFunc(num1Str):
        num1 = int(num1Str)
        break
      else:
        print("\nInvalid input. Please enter an integer.")
    while True:
      num2Str = input("\nEnter another number: ")
      if VerifyIntFunc(num2Str):
        num2 = int(num2Str)
        break
      else:
        print("Invalid input. Please enter an integer.")
    ans = num1 + num2
    print("\n", num1, " plus ", num2, "equals ", ans)
    while True:
      rpt = input("\nTry Again? (y/n): ")
      if rpt.lower() == 'y':
        break
      elif rpt.lower() == 'n':
        ext = True
        break
      else:
        print("\nInvalid Input, choose between 'y' or 'n'.")
    

def SubsFunct():
  ext = False
  rpt = ""
  while ext == False:
    print("You chose Addition")
    while True:
      num1Str = input("\nEnter a number: ")
      if VerifyIntFunc(num1Str):
        num1 = int(num1Str)
        break
      else:
        print("\nInvalid input. Please enter an integer.")
    while True:
      num2Str = input("\nEnter another number: ")
      if VerifyIntFunc(num2Str):
        num2 = int(num2Str)
        break
      else:
        print("Invalid input. Please enter an integer.")
    ans = num1 - num2
    print("\n", num1, " minus ", num2, "equals ", ans)
    while True:
      rpt = input("\nTry Again? (y/n): ")
      if rpt.lower() == 'y':
        break
      elif rpt.lower() == 'n':
        ext = True
        break
      else:
        print("\nInvalid Input, choose between 'y' or 'n'.")

def DivFunct():
  ext = False
  rpt = ""
  while ext == False:
    print("You chose Addition")
    while True:
      num1Str = input("\nEnter a number: ")
      if VerifyIntFunc(num1Str):
        num1 = int(num1Str)
        break
      else:
        print("\nInvalid input. Please enter an integer.")
    while True:
      num2Str = input("\nEnter another number: ")
      if VerifyIntFunc(num2Str):
        num2 = int(num2Str)
        break
      else:
        print("Invalid input. Please enter an integer.")
    ans = num1 / num2
    print("\n", num1, " divided by ", num2, "equals ", ans)
    while True:
      rpt = input("\nTry Again? (y/n): ")
      if rpt.lower() == 'y':
        break
      elif rpt.lower() == 'n':
        ext = True
        break
      else:
        print("\nInvalid Input, choose between 'y' or 'n'.")

def MultFunct():
  ext = False
  rpt = ""
  while ext == False:
    print("You chose Addition")
    while True:
      num1Str = input("\nEnter a number: ")
      if VerifyIntFunc(num1Str):
        num1 = int(num1Str)
        break
      else:
        print("\nInvalid input. Please enter an integer.")
    while True:
      num2Str = input("\nEnter another number: ")
      if VerifyIntFunc(num2Str):
        num2 = int(num2Str)
        break
      else:
        print("Invalid input. Please enter an integer.")
    ans = num1 * num2
    print("\n", num1, " multiplied by ", num2, "equals ", ans)
    while True:
      rpt = input("\nTry Again? (y/n): ")
      if rpt.lower() == 'y':
        break
      elif rpt.lower() == 'n':
        ext = True
        break
      else:
        print("\nInvalid Input, choose between 'y' or 'n'.")