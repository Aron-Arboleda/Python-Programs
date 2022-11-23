# Prime and Composite Numbers Generator

# Create Validator and Generator Functions for both composite and prime numbers.
def isComposite(x):
    if x < 4:
        return False
    elif x == 4:
        return True
    for n in range(2, x):
        if x % n == 0:
            return True

def compositeGenerator(a, b):
    for i in range(a, b):
        if isComposite(i):
            yield i

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeGenerator(a, b):
    for i in range(a, b):
        if isPrime(i):
            yield i

# Extra Filter Function
def Filter(x, m, values):
    x_var = x
    if values[0] in "0123456789":
        value = False
        while value is False:
            for i in x_var:
                if i not in values:
                    print("Invalid input.")
                    value = False
                    x_var = input(f"\n{m}")
                    break
                else:
                    value = True
        return x_var
    else:
        while x_var not in values:
            print("Invalid input.")
            x_var = input(f"\n{m}")
        return x_var

# START
print("\nHello welcome to Prime and Composite Numbers Generator")

# Loop the program
while True:
    print("\na = Composite Numbers") # Provide context for the user and get user input
    print("b = Prime Numbers")
    Message = "Choose what numbers you want to generate(a/b): "
    choice = Filter(input(Message), Message, ["a", "b"])
    
    # Create conditions
    if choice == "a":
        print("\nYou have chosen to generate Composite Numbers.") 
        start_point = 0
        Message = "Generate Composite Numbers upto what number: " 
        end_point = int(Filter(input(Message), Message, "0123456789")) # Ask the endpoint number to generate composite numbers
        print(list(compositeGenerator(start_point, end_point))) # Output the generated numbers
    else:
        print("\nYou have chosen to generate Prime numbers.")
        start_point2 = 0
        Message = "Generate Prime Numbers upto what number: "
        end_point2 = int(Filter(input(Message), Message, "0123456789")) # Ask the endpoint number to generate prime numbers
        print(list(primeGenerator(start_point2, end_point2))) # Output the generated numbers
    
    # Ask if the user want to generate again, this will determine if you will break the loop or continue it
    Message = "Would you like to generate again?(y/n): "
    ans = Filter(input(Message), Message, ["y", "n"])
    if ans == "y":
        continue
    else:
        print("ok bye.")
        break
# END
