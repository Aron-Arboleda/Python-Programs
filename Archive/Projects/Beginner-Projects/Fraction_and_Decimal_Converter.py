# Convert Fractions and Decimals
from fractions import Fraction

# Create Fraction and Decimal Converter Functions
def Fraction_to_Decimal(frac):
    frac = frac.split("/")
    ans = int(frac[0]) / int(frac[1])
    return ans

def Decimal_to_Fraction(dec):
    dec = Fraction(dec)
    return dec

# Extra Functions
def Round_off2D(dec):
    dec = "{:.2f}".format(dec)
    return dec

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
print("\nHello welcome to fraction and decimal converter")

# Loop the program
while True:
    # Output context for the user
    print("a = Fraction to Decimal")
    print("b = Decimal to Fraction")

    # Let the user choose between the two options
    Message = "Choose between the two(a/b): "
    choice = Filter(input(Message), Message, ["a", "b"])
    # Create conditions
    if choice == "a":
        print("\nYou have chosen Fraction to Decimal Converter")
        Message = "Enter your fraction(e.g. 1/2): " # Scan fraction input from user
        frac = Filter(input(Message), Message, ["0","1","2","3","4","5","6","7","8","9","/"])
        ans = Fraction_to_Decimal(frac) # Convert to decimal
        round_off = Round_off2D(ans) # Round off the answer to two decimal places
        # Output both of the answers
        print(f"= {ans}")
        print(f"Round off to two decimal places: {round_off}\n")
    else:
        print("\nYou have chosen Decimal to Fraction Converter")
        Message = "Enter your Decimal(e.g. 0.5): " # Scan decimal input from user
        dec = Filter(input(Message), Message, ["0","1","2","3","4","5","6","7","8","9","."]) 
        dec_ans = Decimal_to_Fraction(dec) # Convert to fraction
        print(f"= {dec_ans}\n") # Output the answer
    
    # Ask if the user want to convert again, this will determine if you will break the loop or continue it
    Message = "Would you like to do another conversion?(yes/no): "
    choice = Filter(input(Message), Message, ["yes", "no"])
    if choice == "yes":
        continue
    else:
        print("ok bye.")
        break
# END
