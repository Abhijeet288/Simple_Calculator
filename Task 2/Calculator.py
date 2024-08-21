print("Select any operation to perform")
print("1.  Addition")
print("2.  Subtraction")
print("3.  Multiplication")
print("4.  Division")


operation = int(input())
if operation == 1:
    # print("Enter two numbers to perform addition")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    print("Addition of two numbers is: "+ str(num1+num2))
elif operation == 2:
    # print("Enter two numbers to perform subtraction")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    print("Subtraction of two numbers is: "+ str(num1-num2))
elif operation == 3:
    # print("Enter two numbers to perform multiplication")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Multiplication of two numbers is: "+ str(num1*num2))
elif operation == 4:
    # print("Enter two numbers to perform division")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Division of two numbers is: "+ str(num1/num2))
else:
    print("Invalid Entry , Please run again ")