print("Calculator")
print("==========\n")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def exponent(a,b):
    return a**b

Entered = False
while Entered == False:
    try:
        print("Would you like to:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n5) Exponentiate")
        Operator = int(input())
        Entered = True
    except ValueError:
        print("Please enter a valid input")

Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
Answer = 0

if Operator == 1:
    Answer = add(Num1,Num2)
    print(f"{Num1} + {Num2} = {Answer}")
elif Operator == 2:
    Answer = subtract(Num1,Num2)
    print(f"{Num1} - {Num2} = {Answer}")
elif Operator == 3:
    Answer = multiply(Num1,Num2)
    print(f"{Num1} * {Num2} = {Answer}")
elif Operator == 4:
    Answer = divide(Num1,Num2)
    print(f"{Num1} / {Num2} = {Answer}")
elif Operator == 5:
    Answer = exponent(Num1,Num2)
    print(f"{Num1} to the power of {Num2} = {Answer}")