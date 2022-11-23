# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name, duplicate-key, global-statement

# import random library to generate random values
import random

# variables initialize arrays/lists of values for the user and computer
choices = {"1": "rock", "2": "paper", "3": "scissors"}
comp_choices = ["1", "2", "3"]

# variable to get user name
user_name = input("\n\033[1;37;40mWhat's your name?: ")

# Filter function for user input.
def Filter(x, m, values):
    x_var = x
    if values == "0123456789":
        value = False
        while value is False:
            for i in x_var:
                if i not in values:
                    print("\033[0;31;40mInvalid input.\033[0m")
                    value = False
                    x_var = input(f"\n{m}")
                    break
                else:
                    value = True
        return x_var
    else:
        while x_var not in values:
            print("\033[0;31;40mInvalid input.\033[0m")
            x_var = input(f"\n{m}")
        return x_var

# START
print(f"\033[0;30;47m Hi {user_name}! Let's play rock-paper-scissors! It's You vs the Computer! \033[0m\n")

# Loop the program
while True:
    # Initialize user and computer score
    user_score = 0
    computer_score = 0 
    Text = "\033[1;37;40mEnter maximum points: "
    maxp = int(Filter(input(Text), Text, "0123456789")) # Get maximum points from the user
    print("\033[0;30;47m\n---GAME START!---\033[0m")
    Text = "\033[1;37;40mEnter your choice 🤛 rock(1), 🖐 paper(2), ✌ scissors(3):"
    user = Filter(input(Text), Text, ["1", "2", "3"]) # Let the user choose if rock, paper, or scissors
    comp = random.choice(comp_choices) # Generate computer choice from lists of choices
    
    # Functions when user will lose or win
    def lose():
        global computer_score
        computer_score += 1
        print(f"\033[1;37;40m---SCORE:--- (First to {maxp} points)")
        print(f"\033[1;37;40m{user_name}: " + str(user_score))
        print("\033[1;37;40mComputer: " + "\033[1;37;40m" + str(computer_score) + "\033[1;33;40m (+1 point)\n")

    def win():
        global user_score
        user_score += 1
        print(f"\033[1;37;40m---SCORE:--- (First to {maxp} points)")
        print(f"\033[1;37;40m{user_name}: " + str(user_score) + "\033[1;33;40m (+1 point)")
        print("\033[1;37;40mComputer: " + "\033[1;37;40m" + str(computer_score) + "\n")

    # Create another loop to repeatedly evaluate user choice and computer choice until one of them reaches the maximum points
    while (user_score != maxp and computer_score != maxp):
        # Apply game logic with conditions
        if user == comp:
            print(f"\033[1;34;40mBoth players selected {choices.get(user)}. It's a TIE!")
            print(f"\033[1;37;40m---SCORE:--- (First to {maxp} points)")
            print(f"\033[1;37;40m{user_name}: " + str(user_score) + "\033[1;33;40m")
            print("\033[1;37;40mComputer: " + "\033[1;37;40m" + str(computer_score) + "\n")
        elif user == "1":
            if comp == "2":
                print("\033[1;31;40mYou LOSE! Computer chose 🖐 (paper). \033[0m")
                lose()
            elif comp == "3":
                print("\033[1;32;40mYou WON! Computer chose ✌ (scissors). \033[0m")
                win()
        elif user == "2":
            if comp == "1":
                print("\033[1;32;40mYou WON! Computer chose 🤛 (rock). \033[0m")
                win()
            elif comp == "3":
                print("\033[1;31;40mYou LOSE! Computer chose ✌ (scissors). \033[0m")
                lose()
        else:
            if comp == "1":
                print("\033[1;31;40mYou LOSE! Computer chose 🤛 (rock). \033[0m")
                lose()
            elif comp == "2":
                print("\033[1;32;40mYou WON! Computer chose 🖐 (paper). \033[0m")
                win()
        if (user_score != maxp and computer_score != maxp):
            Text = "\033[1;37;40mEnter your choice 🤛 rock(1), 🖐 paper(2), ✌ scissors(3):"
            user = Filter(input(Text), Text, ["1", "2", "3"])
            comp = random.choice(comp_choices)
    # Output win or lose message based on the points of both the user and computer
    if user_score == maxp:
        print(f"\033[1;37;42m  ------ YEY! YOU WON THE GAME! You scored {user_score} points ------ \033[0m\n")
    else: 
        print(f"\033[1;37;41m  ------ GAME OVER! YOU LOST THE GAME! Computer scored {computer_score} points ------ \033[0m\n")
    # Ask if user wants to play again. This will determine if you'll break the loop or continue it
    Text = "\033[1;33;40mPlay Again?(y/n): \033[0m"
    ans = Filter(input(Text), Text, ["y", "n"])
    if ans == "n":
        print("ok bye.") 
        break
