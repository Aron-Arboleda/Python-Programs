# Know your zodiac sign program

# Initiate variables to filter user input
Months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
Days = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"
,"16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

# Create Zodiac Indentifier Function
def Zodiac_Identifier(m, d):
    Signs = {
    "Sagittarius": "Sagittarius ♐︎ (The Archer)",
    "Capricorn": "Capricorn ♑︎ (The Goat)",
    "Aquarius": "Aquarius ♒︎ (The Water Bearer)",
    "Pisces": "Pisces ♓︎ (The Fishes)",
    "Aries": "Aries ♈︎ (The Ram)",
    "Taurus": "Taurus ♉︎ (The Bull)",
    "Gemini": "Gemini ♊︎ (The Twins)",
    "Cancer": "Cancer ♋︎ (The Crab)",
    "Leo": "Leo ♌︎ (The Lion)",
    "Virgo": "Virgo ♍︎ (The Virgin)",
    "Libra": "Libra ♎︎ (The Scales)",
    "Scorpio": "Scorpio ♏︎ (The Scorpion)"
    }

    if m == "december":
        if (d >= 1 and d <= 21):
            return Signs.get("Sagittarius")
        elif (d >= 22 and d <= 31):
            return Signs.get("Capricorn")
    elif m == "january":
        if (d >= 1 and d <= 19):
            return Signs.get("Capricorn")
        elif (d >= 20 and d <= 31):
            return Signs.get("Aquarius")
    elif (m == "february" and d <= 29):
        if (d >= 1 and d <= 18):
            return Signs.get("Aquarius")
        elif (d >= 19 and d <= 29):
            return Signs.get("Pisces")
    elif m == "march":
        if (d >= 1 and d <= 20):
            return Signs.get("Pisces")
        elif (d >= 21 and d <= 31):
            return Signs.get("Aries")
    elif (m == "april" and d <= 30):
        if (d >= 1 and d <= 19):
            return Signs.get("Aries")
        elif (d >= 20 and d <= 30):
            return Signs.get("Taurus")
    elif m == "may":
        if (d >= 1 and d <= 20):
            return Signs.get("Taurus")
        elif (d >= 21 and d <= 31):
            return Signs.get("Gemini")
    elif (m == "june" and d <= 30):
        if (d >= 1 and d <= 20):
            return Signs.get("Gemini")
        elif (d >= 21 and d <= 30):
            return Signs.get("Cancer")
    elif m == "july":
        if (d >= 1 and d <= 22):
            return Signs.get("Cancer")
        elif (d >= 23 and d <= 31):
            return Signs.get("Leo")
    elif m == "august":
        if (d >= 1 and d <= 22):
            return Signs.get("Leo")
        elif (d >= 23 and d <= 31):
            return Signs.get("Virgo")
    elif (m == "september" and d <= 30):
        if (d >= 1 and d <= 22):
            return Signs.get("Virgo")
        elif (d >= 23 and d <= 30):
            return Signs.get("Libra")
    elif m == "october":
        if (d >= 1 and d <= 22):
            return Signs.get("Libra")
        elif (d >= 23 and d <= 31):
            return Signs.get("Scorpio")
    elif (m == "november" and d <= 30):
        if (d >= 1 and d <= 21):
            return Signs.get("Scorpio")
        elif (d >= 22 and d <= 30):
            return Signs.get("Sagittarius")
    else:
        print("(Error: The processed birthdate doesn't exist.)")

# Extra filter function for user input
def Filter(x, m, values):
    x_var = x
    while x_var not in values:
        print("Invalid input.")
        x_var = input(f"\n{m}")
    return x_var

# START
print("\nHelloooo, this is a zodiac sign identifier program.")

# Loop the program
while True:
    # Get user input
    print("\nPlease enter your birth date below: ")
    print("(Example. Month: March, Day: 13)")
    MESSAGE = "Month: "
    Month = Filter(input(MESSAGE).casefold(), MESSAGE, Months) # Get month input, turn all characters into small letters, and filter it
    MESSAGE = "Day: "
    Day = int(Filter(input(MESSAGE), MESSAGE, Days)) # Get day input, and filter it
    ZODIAC = Zodiac_Identifier(Month, Day) # Use Zodiac Indentifier Function
    print(f"Zodiac Sign: {ZODIAC}\n") # Output classified zodiac sign
    
    # Ask if the user want to identify zodiac sign again, this will determine if you will break the loop or continue it
    MESSAGE = "Would you like to try again?(y/n): "
    ans = Filter(input(MESSAGE), MESSAGE, ["y", "n"])
    if ans == "y":
        continue
    else:
        print("ok bye.")
        break
# END
