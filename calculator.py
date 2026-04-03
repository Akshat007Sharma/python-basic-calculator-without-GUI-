#building a basic calculator
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
while True:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        print("the total is:",add(num1,num2))
    elif choice == 2:
        print("the difference is:",subtract(num1,num2))
    elif choice == 3:
        print("the product is:",multiply(num1,num2))
    elif choice == 4:
        print("the division is:",divide(num1,num2))
    else:
        print("Invalid choice!")
        break