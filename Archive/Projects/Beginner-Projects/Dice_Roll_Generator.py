import random

# Function to Filter User Input.
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

#  List of Possible Values
dots = (1, 2, 3, 4, 5, 6)

# START
print("ROLL A DICE! \n")

# Ask to roll the dice or not
Message = "Would you like to roll a dice?(y/n) >> "

# Filter input and assign to a variable
choice = Filter(input(Message), Message, ["y", "n"])

# Add conditons
if choice == "y":
    # Loop the program
    while True:
        # Ask dice roll quantity
        Message = "How many times would you like to roll the dice?(enter a number) >> "
        count = int(Filter(input(Message), Message, "0123456789"))

        # Initialize a list variable for Dice Roll Results.
        values_list = []

        # Iterate with count variable
        for i in range(count):
            # Generate random choice from "dots" variable using random library function.
            roll = random.choice(dots)
            # every iteration add the result to list variable to store generated values.
            values_list.append(roll)

            # Add conditions based on the generated value.
            if roll == 1:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
            elif roll == 2:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
            elif roll == 3:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
            elif roll == 4:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
            elif roll == 5:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
            else:
                print("""\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️""")
        # output the results
        print(f"\nResults: {values_list}\n")

        # Ask if the user want to roll the dice again, this will determine if you will break the loop or continue it
        Message = "Roll again?(y/n) >> "
        loop = Filter(input(Message), Message, ["y", "n"])
        if loop == "y":
            continue
        else:
            print("ok bye.")
            break
else:
    print("ok bye.")

# END
