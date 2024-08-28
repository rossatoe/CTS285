def VerifyIntFunc(input):
  try:
    int(input)
    return True
  except ValueError:
    return False

# prompt users to repeat function or end current selection
def secondaryMenuOption():
  """prompts user a question to repeat current math formula or end selection

  """
  while True:
    rpt = input("\nTry Again? (y/n): ")
    if rpt.lower() == 'y':
      return False
    elif rpt.lower() == 'n':
      return True
    else:
      print("\nInvalid Input, choose between 'y' or 'n'.")
    

def AddFunct():
  ext = False
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
    ext = secondaryMenuOption()
    

def SubsFunct():
  ext = False
  while ext == False:
    print("You chose Subtraction")
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
    ext = secondaryMenuOption()

def DivFunct():
  ext = False
  while ext == False:
    print("You chose Division")
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
    ext = secondaryMenuOption()

def MultFunct():
  ext = False
  while ext == False:
    print("You chose Multiply")
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
    ext = secondaryMenuOption()