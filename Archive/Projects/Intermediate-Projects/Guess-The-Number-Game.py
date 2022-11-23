# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name, duplicate-key,

# import random library to generate random values
import random

# Create filter function for user input.
def Filter(x, m, values):
    x_var = x
    if values[0] in "0123456789":
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
print("\n\033[0;30;47m --------- GUESS THE NUMBER! --------- \033[0m")

# Initiate a variable for score to be used for points system
score = 0

# Loop the program
while True:
    number_list = list(range(1001)) # Make a list of all possible values that the computer can generate you can generate a number upto N number, in this case it will generate upto 1000.
    number = random.choice(number_list) # Apply random function to generate a number from the list
    attempts = 10 # Initiate a variable for user attempts to limit number guesses.

    # Output context for the user
    print("\n\033[1;33;40mOur almighty COMPUTER have generated a number between \033[1;37;40m0 \033[1;33;40mand \033[1;37;40m1000, \033[1;31;40m(You have 10 attemps!)\033[0m")
    Text = "\033[1;37;40mEnter your guess: " 
    guess = int(Filter(input(Text), Text, "0123456789")) # Get user guessed number input
    
    # Apply the logic with conditions
    if guess == number:
        print(f"\033[1;37;42m YOU WON! the generated number is {number} \033[0m")
        score += 100
        print(f"\033[1;37;40mScore: {score} \033[1;32;40m(+100 pts)\n")
        Text = "\033[1;33;40mPlay Again?(y/n): "
        ans = Filter(input(Text), Text, ["y", "n"])
        if ans == "y":
            continue
        else:
            print("\033[0mok bye.\n") 
            break
    elif (guess > number or guess < number):
        attempts -= 1 # subtract 1 from attempt for the input earlier
        # Create another loop that will continue to get user guesses until it matches the generated number or when the user ran out of attempts.
        while (guess != number and attempts != 0): 
            if guess > number:
                attempts -= 1
                Text = "\033[1;37;40mLOWER!: "
                guess = int(Filter(input(Text), Text, "0123456789"))
                continue
            elif guess < number:
                attempts -= 1
                Text = "\033[1;37;40mHIGHER!: "
                guess = int(Filter(input(Text), Text, "0123456789"))
                continue
            else:
                print("\033[1;31;40mInvalid input.")
                break
        # If the guess of the user is right, add points to his/her score based on the number of attempts that is left. more attempts = more score. Lastly output context message.
        if guess == number:
            if attempts >= 3:
                print(f"\033[1;37;42m YOU WON! the generated number is {number}. \033[0m")
                score += 40
                print(f"\033[1;37;40mScore: {score} \033[1;32;40m(+40 pts)\n")
            else:
                print(f"\033[1;37;42m YOU WON! the generated number is {number}. \033[0m")
                score += 20
                print(f"\033[1;37;40mScore: {score} \033[1;32;40m(+20 pts)\n")
        # If the user ran out of attempts, subtract points to his/her score and output context message.
        elif attempts == 0:
            print(f"\033[0;37;41m You LOSE! You've ran out of attempts. The generated number is \033[1;37;41m{number}\033[0;37;41m. \033[0m")
            score -= 5
            print(f"\033[1;37;40mScore: {score} \033[1;31;40m(-5 pts)\n")
        # Ask if the user wants to play again. This will determine if you'll break the loop or continue it
        Text = "\033[1;33;40mPlay Again?(y/n): "
        ans = Filter(input(Text), Text, ["y", "n"])
        if ans == "y":
            continue
        elif ans == "n":
            print("\033[0mok bye.\n") 
            break
    else: 
        print("\033[0;31;40mInvalid input.")
# END
