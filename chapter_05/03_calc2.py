on = True

def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)

def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)

def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)
# enclose selection into while loop
while on:
    operation = input("Please type +, -, *, /, or q: ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        calc_on = False
    else:
        print("That operation is not available.  ")