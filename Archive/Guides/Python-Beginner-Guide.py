# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name

# Table of Contents
# 1. Simple Calculation.
# 2. Some Math 
# 3. Exponentiation 
# 4. Flight Time (Project)
# 5. Strings 1
# 6. Strings 2
# 7. String Operations
# 8. Working with Variables
# 9. Input
# 10. Working with input
# 11. Tip Calculator (Project)
# 12. if Statements
# 13. else Statements
# 14. Boolean Logic
# 15. while Loops
# 16. continue
# 17. BMI Calculator (Project)
# 18. Lists
# 19. List Operation
# 20. for Loops
# 21. Ranges
# 22. List Slices
# 23. Sum of Consecutive Numbers (Project)
# 24. List Functions
# 25. String Functions
# 26. def Function
# 27. Arguments
# 28. Return
# 29. Search Engine (Project)


"""
1. Simple Calculation.
Calculating points earned by a soccer team. The team won 18 games and ended 7 games as a draw.
A win brings 3 point, while a draw brings 1. 
"""
print("1.") # (To organize the output, kindly ignore)
print((18 * 3) + (7 * 1))



"""
2. Some Math 
Write a program that will multiply the sum of 5 and 6 by 57.3 and output the result. 
"""
print("\n2.") # (To organize the output, kindly ignore)
print((5 + 6) * 57.3)



"""
3. Exponentiation 
Write code to output 4 raised to the 5th power. 
"""
print("\n3.") # (To organize the output, kindly ignore)
print(4 ** 5)



"""
4. Flight Time 
You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, 
covering a distance of 7425 miles, the place flies at an average speed of 550 miles an hour. 
calculate and output the total flight time in hours. (Hint) The result sshould be a float.
"""
print("\n4.") # (To organize the output, kindly ignore)
print(7425 / 550)



"""
5. Strings 1
You are given a code that should output a string with quotes. However, it contains errors.
Add backlash commands to fix the given code.
"""
print("\n5.") # (To organize the output, kindly ignore)
print('I\'m learning Python. It\'s easy.')



"""
6. Strings 2
Write a program to output the letters A B C D, each on a separate line.
"""
print("\n6.") # (To organize the output, kindly ignore)
print("""A
B
C
D""")


"""
7. String Operations
Create a program to output "hi" 5 times, without any separators, on the same line.
"""
print("\n7.") # (To organize the output, kindly ignore)

print("hi" * 5)

"""
8. Working with Variables
The provided code stores the value 7 in a variable, and outputs it. 
Change the code to output the value of the variable raised to the power of 3.
"""
print("\n8.") # (To organize the output, kindly ignore)

num = 7
print(num ** 3)

"""
9. Input
Create a code that takes a string input from the user and multiply it by 10.
"""
print("\n9.") # (To organize the output, kindly ignore)

x = input()
print(x * 10)

"""
10. Working with input
Write a program to take x and y as input and output the string x, repeated y times. 
Sample Input: 
hi
3
Sample Output:
hihihi
"""
print("\n10.") # (To organize the output, kindly ignore)

x = str(input())
y = int(input())
print(x * y)

"""
11. Tip Calculator
Write a program to tip with 20% of the bill amount. Your program needs to take the bill amount as input and output the tip as a float.
Sample Input: 
50
Sample Output:
10.0
"""
print("\n11.") # (To organize the output, kindly ignore)

bill = int(input())
print(float(bill * 0.20))

"""
12. if Statements
Write a program that chechs if the water is boiling. Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.
Sample Input:
105
Sample Output:
Boiling 
"""
print("\n12.") # (To organize the output, kindly ignore)

temp = int(input())
if temp >= 100:
    print("Boiling")


"""
13. else Statements
Write a program that controls he entrance to a club. Only people who are 18 or older are allowed to enter the club. 
Your program takes the age of the person who tries to enter, and outputs "Allowed" if they are allowed and "Sorry" if they are too young.
Sample Input: 
24
Sample Output:
Allowed
"""
print("\n13.") # (To organize the output, kindly ignore)

age = int(input())
if age >= 18:
    print("Allowed")
else:
    print("Sorry")

"""
14. Boolean Logic
Given the age of a person as an input, output their age group. Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64
Sample Input:
42
Sample Output:
Adult
"""
print("\n14.") # (To organize the output, kindly ignore)

age = int(input("Enter your age: "))
if (age >= 0 and age <= 11):
    print("Child")
elif (age >= 12 and age <= 17):
    print("Teen")
elif (age >= 18 and age <= 64):
    print("Adult")

"""
15. while Loops
You are given a program that outputs all the numbers from 0 to 10. Change the code to make it output only the even numbers.
Note: Any integer that can be dividede exactly by 2 is an even number.
"""
print("\n15.") # (To organize the output, kindly ignore)

x = 0
while x <= 10:
    print(x)
    x += 2
    
"""
16. continue
You are making a ticketing system. The price of a single ticket is $100. For children under 3 years of age, the ticket is free. Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
Sample Input:
18
24
2
5
42
Sample Output:
400
"""
print("\n16.") # (To organize the output, kindly ignore)

total = 0
passengers = 5

while passengers > 0:
    x = int(input("Age: "))
    passengers -= 1
    if x > 3:
        total += 100
    
print("Total fee:", total)

"""
17. BMI Calculator
formula: weight/height^2
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30.
Obesity = 30 or more
Sample Input:
85
1.9
Sample Output:
Normal
"""
print("\n17.") # (To organize the output, kindly ignore)

weight = float(input())
height = float(input())
BMI = weight/height**2
if BMI < 18.5:
    print("Underweight")
elif (BMI >= 18.5 and BMI < 25):
    print("Normal")
elif (BMI >= 25 and BMI < 30):
    print("Overweight")
else:
    print("Obesity")

"""
18. Lists
Write a program that takes an input string and outputs the 3rd character of the string.
"""
print("\n18.") # (To organize the output, kindly ignore)

x = str(input())
print(x[2])

"""
19. List Operation
Given a list of numbers, output "bingo" if it contains the unput number.
"""
print("\n19.") # (To organize the output, kindly ignore)

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())
if num in x:
    print("bingo")

"""
20. for Loops
for loops allow you to easily iterate thorugh lists. Given a list of numbers, calculate their sum using a for loop.
"""
print("\n20.") # (To organize the output, kindly ignore)

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

total_sum = 0
for i in x:
    total_sum += i

print(total_sum)

"""
21. Ranges
Take two inputs, one for start and one for the end of year. Use range function to complete the program.
Print the output as a list.
"""
print("\n21.") # (To organize the output, kindly ignore)

x = int(input())
y = int(input())
print(list(range(x, y)))

"""
22. List Slices
Write a program that takes an input string and outputs the last character of that string.
"""
print("\n22.") # (To organize the output, kindly ignore)

x = str(input())
print(x[-1])

"""
23. Sum of Consecutive Numbers
Take a number N as input and output the sum of all number from 1 to N (including N).
Sample input:
100
Sample Output:
5050
Explanation: The sum of all numbers from 1 to 100 equal to 5050.
"""
print("\n23.") # (To organize the output, kindly ignore)

N = int(input())
x = list(range(N+1))

total = 0
for i in x:
    total += i

print(total)


"""
24. List Functions
Write a program that takes an input, add it to the end of the queue, and output the resulting list.
"""
print("\n24.") # (To organize the output, kindly ignore)

queue = ['John', 'Amy', 'Bob', 'Adam']
x = input()
queue.append(x)
print(queue)


"""
25. String Functions
Replace all of the characters in the given input with spaces and output the result.
"""
print("\n25.") # (To organize the output, kindly ignore)

msg = "hatdog#ham#cheesestick"
print(msg.replace("#", " "))

"""
26. def Function
Replace all of the characters in the given input with spaces and output the result.
"""
print("\n26.") # (To organize the output, kindly ignore)

user = input()

def welcome():
    print("Welcome, " + user)

welcome()

"""
27. Arguments
You need to take the user input and call the printBill() function by passing the input as its argument.
"""
print("\n27.") # (To organize the output, kindly ignore)

text2 = input()

def printBill(text2):
    print("======")
    print(text2)
    print("======")

printBill(text2)

"""
28. Return
Take the width and length as input and output the area of the rectangle. Complete the area function, 
which takes the length and width as arguments, to calculate and return the area. Then call the function for the given inputs.
"""
print("\n28.") # (To organize the output, kindly ignore)

def area(x, y):
    return x*y

w = int(input())
h = int(input())

print(area(w, h))

"""
29. Search Engine
The given code takes a text and a word as input and passes them to a function called search(). The search() function should return "Word found" if the word is present in the text, or "Word not found", if it isn't.
Sample Input:
"This is awesome"
"awesome"
Sample Output:
Word found
"""
print("\n29.") # (To organize the output, kindly ignore)

text = input()
word = input()
def search(x, y):
    if y in x:
        return "Word found"
    else:
        return "Word not found"

print(search(text, word))