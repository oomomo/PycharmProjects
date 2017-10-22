def add(num1, num2):
    """REturn num1 plus num2"""
    return num1 + num2

def sub(num1, num2):
    """REturn num1 minus num2"""
    return num1 - num2

def mul(num1, num2):
    """REturn num1 times num2"""
    return num1 * num2

def div(num1, num2):
    """REturn num1 divided by num2"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled div by zero, Returning zero. ")
        return 0

def runOperation(operation, num1, num2):
    """Determines the operation to run based on the operation argument
    which should be passed in as an int"""
    """Determine operation"""
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Substracting...")
        print(sub(num1, num2))
    elif (operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print('Dividing...')
        print(div(num1, num2))
    else   :
        print("I don't understand.")

def main():
    # Allow user to run basic calculator operations with two numbers
    user_continue = True
    while user_continue:
        validInput = False
        while not validInput:
            # Get user input
            try :
                num1 = int(input("What is number 1? "))
                num2 = int(input("What is number 2? "))
                operation = int(input("What do you want to do? 1. add, 2. substract, 3. multiply, "
                                      "or 4. divide. Enter number: "))
                validInput = True
            except ValueError:
                print("Invalid input. Try again.")
            except:
                print("Unknown Error")
            runOperation(operation, num1, num2)
            user_yn = input('Would you like to run another calculation? ("y" for yes or '
                            'any other value to exit)')
            if (user_yn != 'y'):
                user_continue = False
                break
            else:
                continue

if __name__ == "__main__":
    main()



