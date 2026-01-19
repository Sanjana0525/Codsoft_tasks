def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Error: Division by zero is not possible"
    else:
        return a/b
    
while True:
    print("\n ------ Simple Calculator ------")
    print("1: Addition(+)")
    print("2: Subtraction(-)")
    print("3: Multiplication(*)")
    print("4: Division(/)")
    print("5: Exit")

    choice = input("Choose an operation to perform: ")

    if choice == "5":
        print("Exiting!")
        break

    if choice in ["1","2","3","4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result of Addition = ",add(num1,num2))

        elif choice == "2":
            print("Result of Subtraction = ",sub(num1,num2))

        elif choice == "3":
            print("Result of Multiplication = ",mul(num1,num2))

        elif choice == "4":
            print("Result of Division = ",div(num1,num2))
    
    else:
        print("Invalid choice! Please try again")
