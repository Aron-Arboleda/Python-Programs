# Welcome text
print("Hello this is a calculator limited to perform calculations for two numbers only. ")
print("Proceed to calculate below.")

# symbols variable for filtering user input.
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`-=,./;'[]\<>?:\"{|} "

while True:
    # get first number input
    num1 = input("Enter your first number: ")
    # filter user input using symbols variable then convert string input into float number
    while num1[0] in symbols:
        print("Invalid input.")
        num1 = input("Enter your first number: ")
    num1 = float(num1)

    # get second number input
    num2 = input("Enter your second number: ")
    # filter user input using symbols variable then convert string input into float number
    while num2[0] in symbols:
        print("Invalid input.")
        num2 = input("Enter your second number: ")
    num2 = float(num2)

    # let user choose operation
    operation = input("Choose your operation by entering a number [add(1), subtract(2), multiply(3), divide(4)]: ")

    # filter user input and convert string input into integer
    while operation not in ["1", "2", "3", "4"]:
        print("Invalid input.")
        operation = input("Choose your operation by entering a number [add(1), subtract(2), multiply(3), divide(4)]: ")
    operation = int(operation)

    # add conditions and print outputs
    if operation == 1:
        print(num1, "+", num2, "=", (num1 + num2))
    elif operation == 2:
        print(num1, "-", num2, "=", (num1 - num2))
    elif operation == 3:
        print(num1, "×", num2, "=", (num1 * num2))
    elif operation == 4:
        print(num1, "÷", num2, "=", (num1 / num2))

    # ask if user would like to calculate again
    ans = input("\nWould you like to do another calculation?(yes/no): ")
    # filter user input
    while ans not in ["yes","no"]:
        print("Invalid input.")
        ans = input("\nWould you like to do another calculation?(yes/no): ")
    if ans == "yes":
        continue
    else:
        print("ok bye.") 
        break