# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name, duplicate-key, unspecified-encoding, bad-indentation

# Table of Contents
# 1. Dictionaries
# 2. Dictionary Functions
# 3. Tuples
# 4. Tuple Unpacking
# 5. Sets
# 6. Line Functions 
# 7. Letter Counter (practice)
# 8. Lambda
# 9. Map
# 10. Generators
# 11. Decorators
# 12. Recursion
# 13. *args
# 14. **kwargs
# 15. Spelling Backwards (practice)
# 16. Classes
# 17. Inheritance
# 18. Operator Overloading, Magic Methods
# 19. Data Hiding
# 20. Static Methods
# 21. Properties
# 22. Inheritance
# 23. Exception Handling (try and except)
# 24. Exception Handling (finally)
# 25. Exception Handling (else)
# 26. Raising Exceptions
# 27. Registration System (practice)
# 28. Reading Files
# 29. Writing Files
# 30. Working with Files
# 31. Title Encoder (practice)
# 32. Assertions

"""
1. Dictionaries
You are working at a car dealership and store the car data in a dictionary: Your program needs to take the key as input
and output the corresponding value.
Sample Input:
year
Sample Output:
2018 
"""
print("\n1.") # (To organize the output, kindly ignore)

car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

key = str(input())
print(car[key])


"""
2. Dictionary Functions
You are working on data that represents the economic freedom rank by country. Each country name and rank are stored in a dictionary,
with the key being the country name. Complete the program to take the country name as input and output its corresponding economic 
freedom rank. In case the provided country name is not present in the daya, output "Not found".
"""
print("\n2.") # (To organize the output, kindly ignore)

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

country_name = str(input())
print(data.get(country_name, "Not found"))

"""
3. Tuples
You are given a lists of contacts, where each contact in represented by a tuple, with the name and age of the contact.  
Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact 
in the format presented below:
Sample Input:
John
Sample Output:
John is 31
"""
print("\n3.") # (To organize the output, kindly ignore)

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18),
]

name = str(input())
for x in contacts:
    if x[0] == name:
        print(name + " is " + str(x[1]))    
        break
    if x[0] != name:
        continue
else:
    print("Not Found")

"""
4. Tuple Unpacking
Tuple can be used to output multiple values from a function. You need to make a function called calc(), that will take the side length
of a square as its argument and return the perimeter and area using a tuple. The perimeter is the sum of all sides, while the area 
is the square of the side length.
Sample Input:
3
Sample Output:
Perimeter: 12
Area: 9
"""
print("\n4.") # (To organize the output, kindly ignore)

def calc(x):
    return x * 4, x ** 2

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))


"""
5. Sets
YOu are working on a recruitment platform, which should march the aailable jobs and the candidates based on their skills. 
The skills required for the job, and the candidate's skills are stored in sets. Complete te program to output the matched
"""
print("\n5.") # (To organize the output, kindly ignore)

skills = {'Python', 'HTML', 'Sql', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(list(skills & job_skills)[0])

"""
6. Line Functions 
Given a word as input, output a list, containing only the letters of the word that are not vowels. The vowels are a, e, i, o, u.
Sample Input:
awesome
Sample Output:
['w', 's', 'm']
"""
print("\n6.") # (To organize the output, kindly ignore)

word = set(input())
consonants = [i for i in word if i not in ('a', 'e', 'i', 'o', 'u')]
print(consonants)

"""
7. Letter Counter (practice)
Given a string as input, you need to output how many times each letter appeats in the string. 
You decide to store the daya in a dictionary, with the letters as the keys, and the corresponding countrs as the values. 
Create a program to take a string as input and output a dictionary, which represents the letter count. 
Sample Input:
awesome
Sample Output:
['w', 's', 'm']
"""
print("\n7.") # (To organize the output, kindly ignore)

text = input()
dicta = {}
for i in text:
    dicta[i] = text.count(i)

print(dicta)


"""
8. Lambda
You are given code that should calculate the corresponding percentage of a price. Somebody wrote a lambda function to accomplish that, 
however the lambda is wrong. Fix the code to output the given percentage of the price.
Sample Input:
50
10
Sample Output:
5.0
"""
print("\n8.") # (To organize the output, kindly ignore)

price = int(input())
perc = int(input())

res = (lambda x, y: x*(y/100))(price, perc)
print(res)

"""
9. Map
You work on a payroll program. Given a list of salaries, 
you need to take the bonus everybody is getting as input and increase all the salaries by that amount. 
Output the resulting list. You can use the map() function to increase all the values of teh list.
"""
print("\n9.") # (To organize the output, kindly ignore)

def add_bonus(x):
	return x + bonus

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
result = list(map(add_bonus, salaries))
print(result)

"""
10. Generators
Finding prime numbers is a common coding interview task. The given code defines a function isPrime(x), which returns Trie if x is prime. 
You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the isPrime() function to 
output the prime numbers in the given range(between the two arguments).
Sample Input:
10
20
Sample Output:
[11, 13, 17, 19]
• The given code takes the two arguments as input and passes them to the generator function, outputting the result as a list.
"""
print("\n10.") # (To organize the output, kindly ignore)

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

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

"""
11. Decorators
You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
***
INVOICE #42
***
END OF PAGE
"""

print("\n11.") # (To organize the output, kindly ignore)

def decor(func):
	def wrap(x):
		print("***")
		func(x)
		print("***")
		print("END OF PAGE")
	return wrap

@decor
def invoice(num):
	print("INVOICE #" + num)

invoice(input())

"""
12. Recursion
The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary. 
However, the code has an error. Fix the code by adding the base case for the recursion, 
then take a number from user input and call the convert() function, to output the result.
Sample Input:
8
Sample Output:
1000
"""

print("\n12.") # (To organize the output, kindly ignore)

def convert(num):
	if num == 0:
		return 0
	else:
		print(num)
		return (num % 2 + 10 * convert(num//2))

print(convert(int(input())))

"""
13. *args
The given code defined a function called my_in(), which takes two arguments and returns the smaller one. 
You need to improve the function, so that it can take any number of variables, so that the function call works.
• Remember, *args can be accessed inside the function as a tuple.
"""

print("\n13.") # (To organize the output, kindly ignore)

def my_min(*args):
	return min(args)

print(my_min(8, 13, 4, 42, 120, 7))

"""
14. **kwargs
"""

print("\n14.") # (To organize the output, kindly ignore)

def my_func(x, y = 7, *args, **kwargs):
	print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

"""
15. Spelling Backwards (practice)
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.
Sample Input:
HELLO
Sample Output:
O
L
L
E
H
• Complete the recursive spell() function to produce the expected result.
"""

print("\n15.") # (To organize the output, kindly ignore)

def spell(txt):
	#your code goes here
	if len(txt) == 1:
		print(txt)
	else:
		print(txt[-1])
		txt = txt[:-1]
		spell(txt)

txt = input()
spell(txt)

"""
16. Classes
You are making a video game! The given code declares a Player class, with its attributes and an intro() method.
Complete the code to take the name and level from user input, create a Player object with the corresponding values and 
call the intro() method of that object.

Sample Input
Tony
12

Sample Output
Tony (Level 12)
• Complete the recursive spell() function to produce the expected result.
"""

print("\n16.") # (To organize the output, kindly ignore)

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

user = Player(input(), input())
user.intro()

"""
17. Inheritance
You are making a drawing application, which has a Shape base class.
The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods. 

Do the following to complete the program:
1. Inherit the Rectangle class from Shape.
2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle.
• The perimeter is equal to 2*(width+height)
"""

print("\n17.") # (To organize the output, kindly ignore)

class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    #your code goes here
    def perimeter(self):
        print(2*(self.width + self.height))

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()

"""
18. Operator Overloading, Magic Methods
We are improving our drawing application.
Our application needs to support adding and comparing two Shape objects. 
Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.

The addition should return a new object with the sum of the widths and heights of the operands, 
while the comparison should return the result of comparing the areas of the objects.
• The given code created two Shape objects from user input, outputs the area() of their addition and compares them.
"""

print("\n18.") # (To organize the output, kindly ignore)

class Shape2: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        return self.width*self.height

    def __add__(self, other):
        return Shape2(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape2(w1, h1)
s2 = Shape2(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)


"""
19. Data Hiding
We are working on a game. Our Player class has name and private _lives attributes.
The hit() method should decrease the lives of the player by 1. In case the lives equal to 0, it should output "Game Over".
Complete the hit() method to make the program work as expected.
• The code creates a Player object and calls its hit() method multiple times.
"""

print("\n19.") # (To organize the output, kindly ignore)

class Player2:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")

p = Player2("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()

"""
20. Static Methods
The given code takes 2 numbers as input and calls the static area() method of the Shape class, to output the area of the shape, 
which is equal to the height multiplied by the width. To make the code work, you need to define the Shape class, 
and the static area() method, which should return the multiplication of its two arguments.
• Use the @staticmethod decorator to define a static method.
"""
print("\n20.") # (To organize the output, kindly ignore)

class Shape3:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(w, h):
        return w * h

w = int(input())
h = int(input())

print(Shape3.area(w, h))

"""
21. Properties
We are improving our game and need to add an isAlive property, which returns True if the lives count is greater than 0.
Complete the code by adding the isAlive property.
• The code uses a while loop to hit the Player, until its lives count becomes 0, using the isAlive property to make the condition.
"""
print("\n21.") # (To organize the output, kindly ignore)

class Player5:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    #your code goes here
    @property
    def isAlive(self):
        if self._lives > 0:
            return True
        else:
            return False

p = Player5("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break

"""
22. Inheritance
We are improving our game and need to add an isAlive property, which returns True if the lives count is greater than 0.
Complete the code by adding the isAlive property.
• The code uses a while loop to hit the Player, until its lives count becomes 0, using the isAlive property to make the condition.
"""
print("\n22.") # (To organize the output, kindly ignore)

class Enemy:
    name = ""
    lives = 0
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster', 3)

class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == "laser":
        a.hit()
    elif x == "gun":
        m.hit()
    elif x == 'exit':
        break

"""
23. Exception Handling (try and except)
An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
In case the input is not a number, the machine should output "Please enter a number".
Use exception handling to take a number as input, call the withdraw() method with the input as its argument, and output "Please enter a number", in case the input is not a number.
• A ValueError is raised when you try to convert a non-integer to an integer using int().
"""
print("\n23.") # (To organize the output, kindly ignore)

def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   money = int(input())
   withdraw(money)
except ValueError:
    print("Please enter a number")

"""
24. Exception Handling (finally)
"""
print("\n24.") # (To organize the output, kindly ignore)

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

"""
25. Exception Handling (else)
You are making a digital menu to order food. The menu is stored as a list of items.
Your program needs to take the index of the item as input and output the item name.
In case the index is not valid, you should output "Item not found".
In case the index is valid and the item name is output successfully, you should output "Thanks for your order".
Sample Input:
    2
Sample Output:
    Cheeseburger
    Thanks for your order
• Handle the cases when the input is out of range, as well as when it is not a number.
"""
print("\n25.") # (To organize the output, kindly ignore)

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
try:
    order = menu[int(input())]
    print(order)
except (ValueError, IndexError):
    print("Item not found")
else:
    print("Thanks for your order")

"""
26. Raising Exceptions
You are making a program to post tweets. Each tweet must not exceed 42 characters.
Complete the program to raise an exception, in case the length of the tweet is more than 42 characters.
• You can use the len() function to calculate the length of the string.
"""
print("\n26.") # (To organize the output, kindly ignore)

tweet = input()

try:
    #your code goes here
    if len(tweet) > 42:
        raise SyntaxError
    
except:
    print("Error")
else:
    print("Posted")

"""
27. Registration System (practice)
You are making a registration form for a website.
The form has a name field, which should be more than 3 characters long.
Any name that has less than 4 characters is invalid.
Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". Output "Account Created" if the name is valid.
Sample Input
    abc
Sample Output
    Invalid Name
• Use try/raise/except statements.
"""
print("\n27.") # (To organize the output, kindly ignore)

try:
    name = input()
    #your code goes here
    if len(name) < 4:
        raise SyntaxError
except:
    print("Invalid Name")
else:
    print("Account Created")

"""
28. Reading Files
You need to make a program to read the given number of characters of a file.
Take a number N as input and output the first N characters of the books.txt file.
• The given code opens the books.txt file. Use the file object to read the content of the file.
"""
print("\n28.") # (To organize the output, kindly ignore)

file = open("btch.txt")
#your code goes here
char = int(input())
print(file.read(char))
file.close()

"""
29. Writing Files
Take a number N as input and write the numbers 1 to N to the file "numbers.txt", each number on a separate line.
Sample Input
    4
Sample Output
    1
    2
    3
    4
The given code reads the content of the file and outputs it.
• You can use \n to make line breaks. Do not forget to close the file after writing to it.
"""
print("\n29.") # (To organize the output, kindly ignore)

n = int(input())

file = open("btch.txt", "w+")
#your code goes here
for i in range(1, n + 1):
    file.write(f"{i}\n")
file.close()

f = open("btch.txt", "r")
print(f.read())
f.close()

"""
30. Working with Files
You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words
...

Make sure to match the above mentioned format in the output.
To count the number of words in a given string, you can use the split() function, or, 
alternatively, count the number of spaces (for example, if a string contains 2 spaces, then it contains 3 words).
"""
print("\n30.") # (To organize the output, kindly ignore)

with open("btch.txt") as f:
    #your code goes here
    y = 1
    for i in f.readlines():
        x = i.count(" ") + 1
        print(f"Line {y}: {x} words")
        y += 1

"""
31. Title Encoder
You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions, each on a new line.
• You can use the .split() method to get a list of words in a string.
"""
print("\n31.") # (To organize the output, kindly ignore)

file = open("btch.txt")

x = file.readlines()
for i in x:
    lists = []
    y = i.split(" ")
    for a in y:
        b = lists.append(a[0])
    print("".join(lists))
file.close()

"""
32. Assertions

"""
print("\n32.") # (To organize the output, kindly ignore)

print(1)
assert 2 + 2 == 4
print(2)
temp = -10
assert (temp >= 0), "Colder than absolute zero!"
print(3)