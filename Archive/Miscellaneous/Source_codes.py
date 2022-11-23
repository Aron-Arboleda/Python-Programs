# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name, duplicate-key, unspecified-encoding, bad-indentation

# decorator
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


# -------------------------------------------------------

# Recursion
def factorial(x):
	if x == 1:
		return 1
	else: 
		return x * factorial(x-1)

print(factorial(5))


def is_even(x):
	if x == 0:
		return True
	else:
		print(x)
		return is_odd(x-1)

def is_odd(x):
	print(x)
	return not is_even(x)

print(is_odd(17))
print(is_even(22))

def convert(num):
	if num == 0:
		return 0
	else:
		print(num)
		return (num % 2 + 10 * convert(num//2))

print(convert(int(input())))

# -------------------------------------------------------

# kwargs and args
def function(named_arg, *args):
	print(named_arg)
	print(args)

function(1, 2, 3, 4, 5)

def my_func(x, y = 7, *args, **kwargs):
	print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


def my_min(*args):
	return min(args)

print(my_min(8, 13, 4, 42, 120, 7))


# -------------------------------------------------------

# Object-Oriented-Programming

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

user = Player(input(), input())
user.intro()

# Inheritance

class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cato(Animal):
    def purr(self):
        print("Purr...")
        
class Dogo(Animal):
    def bark(self):
        print("Woof!")

fido = Dogo("Fido", "brown")
print(fido.color)
fido.bark()


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")
    
class Dogs(Wolf):
    def bark(self):
        print("Woof")
    
husky = Dogs("Max", "grey")
husky.bark()


class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

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


class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

first = Vector2d(5, 7)
second = Vector2d(3, 9)
result = first + second
print(result.x)
print(result.y)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
    
    def __mul__(self, x):
        return "\n" + self.cont + " x " + x.cont

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
print(spam * hello)

# Magic methods

class SpecialStrings:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialStrings("spam")
eggs = SpecialStrings("eggs")
spam > eggs

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])


class Shapes: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shapes(w1, h1)
s2 = Shapes(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)


class Mammal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        return "My name is " + self.name

m1 = Mammal("Dave", 17, "Brown")
m2 = Mammal("Bob", 21, "Green")
print(m2.introduce())

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_Sitting = i

    def to_sit(self):
        is_Sitting = True

    def to_stand(self):
        is_Sitting = False

p1 = Person("Alice", "wild", True)
p2 = Person("Rebecca", "quiet", False)
print(p1.is_Sitting)

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)


class Player1:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")

p = Player1("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()

# @classmethods

class Rectangles:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangles.new_square(5)
print(square.calculate_area())

# @staticmethod

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

class Shape1:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

m = Shape1(int(input()), int(input()))
print(m.area())

class Shape2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(w, h):
        return w * h

w = int(input())
h = int(input())

print(Shape2.area(w, h))

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`-=,./;'[]\\<>?:\"{|}"

guess = input("Enter your guess: ")
if guess[0] in symbols:
    print("Invalid input.")
else:
    print("correct!")
    print(guess)

# @property

class Pizza1:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza1(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

class Pizza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza2(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

# @.setter

class ClassName: 
    def __init__(self, value): 
        self.__varName = value 
        
    @property
    def varName(self): 
        return self.__varName 
    
    @varName.setter 
    def varName(self, value): 
        self.__varName = value

instance = ClassName(42) 
# getter: 
print(instance.varName) 
# setter: 
instance.varName = 0


class Player3:
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

p = Player3("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break

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

user_input = input()
for i in user_input:
    position = user_input.index(i)
    if i.isupper():
        if position == 0:
            change = i.lower()
            user_input = user_input.replace(i, change)
            print(user_input)
        elif position != 0:
            change = "_" + i.lower()
            user_input = user_input.replace(i, change)
            print(user_input)

a = "hello hi hello hellolo"
print(a.title())

# -------------------------------------------------------

Price_Nachos = 6.00
Price_Pizza = 6.00
Price_Cheeseburger = 10.00
Price_Water = 4.00
Price_Coke = 5.00
Tax = 0.07

order = input()
order_list = order.split(" ")

total = 0
for i in order_list:
    if i == "Nachos":
        total += Price_Nachos
    elif i == "Pizza":
        total += Price_Pizza
    elif i == "Cheeseburger":
        total += Price_Cheeseburger
    elif i == "Water":
        total += Price_Water
    elif i == "Coke":
        total += Price_Coke
    else:
        total += Price_Coke

Tax = (total * Tax)
Final_total = total + Tax
print(Final_total)

# Isogram Detector

word = input()
output = ""
for i in word:
    if word.count(i) > 1:
        output = "false"
        break
    elif word.count(i) == 1:
        output = "true"
        continue

print(output)

number = int(input("Enter number: "))
count = 0
binary = []

while number > -1:
    number /= 2
    binary.insert(0, number % 2)

print(binary)

houses = int(input())

dollarchance = 2  / houses
percent = (dollarchance * 100) + .5
print(round(percent))

answer = (2 / houses) * 100
format2 = "{:.0f}".format(answer)
print(format2)


if houses >= 3:
    print("yes")
else:
    print("Invalid input.")

yards = int(input())

if yards > 10:
    print("High Five")
elif yards < 1:
    print("shh")
else:
    print("Ra!" * yards)

points = int(input())
price = int(input())
tickets = points // 12

if tickets >= price:
    print("Buy it!")
else:
    print("Try again")

number_of_paint = int(input())
paint = 5 * number_of_paint
c_a_b = 40
tax_value = (c_a_b + paint) * 0.1
total = c_a_b + paint + tax_value
print(round(total))

pesos = int(input())
dollars = int(input())
pesos = (pesos * 2)/100

if pesos < dollars:
    print("Pesos")
elif pesos == dollars:
    print("Pesos")
else:
    print("Dollars")

class Currency:
    def __init__(self, pesos, dollars):
        self.pesos = pesos
        self.dollars = dollars

    def compare(self):
        self.pesos = (self.pesos * 2)/100
        if self.pesos < self.dollars:
            print("Pesos")
        elif self.pesos == self.dollars:
            print("Pesos")
        else:
            print("Dollars")
        
pesos = int(input())
dollars = int(input())
x = Currency(pesos, dollars)
x.compare()

# print(((9 * 6) + (5 ^ 3)) >= ((92 - 45) * 5 - (210 - 9 * 3)) or !(66 / 6 == 9 + 2) and (5 * 8 - 40) or (35 * 3 + 52 <= (23 + 75)) and !(34 % 73))
# print(9 + ((48 / 6) * 5 * (97 % 8) + 12 - (6 * 7)) - 8 + 5 + ((18 - 10) + 50 - (27 * 2)) - 6)

door_height = int(input())
door_width = int(input())
tape_feet = 60

vertical_area = door_height * 6
door_area = (vertical_area * door_width) * 2
if door_area % tape_feet == 0:
    print(door_area // tape_feet)
else:
    print((door_area // tape_feet) + 1)

num = int(input())
binary = bin(num)
total = binary.count("1")
print(total)



# remote control

# Command = input()

Open = True
Close = False
Temperature = 24
State = Close
while True:
    Command = input()
    if Command == "Power":
        State = Open
        print("\nPower On.")
        print(f"Temperature: {Temperature}°C")
    while State == Open:
        Command = input()
        if Command == "+":
            Temperature += 1
            print(f"Temperature: {Temperature}°C")
        else:
            if Command == "-":
                Temperature -= 1
                print(f"Temperature: {Temperature}°C")
            else:
                if Command == "Power": 
                    State = Close
    if (State == Close and Command == "Power"):
        print("\nPower Off.")
        break

Activated = True
Not_Activated = False
System = Not_Activated

varSystem = 1234
varInput = int(input())
while varSystem != varInput:
    print("Wrong Password. ")
    varInput = int(input())

print("Close the Doors")
System = Activated
print("System Activated. ")
while System == Activated:
    varInput = int(input())
    
    Door = input()
    while Door != "move":
        Door = input()
    if Door == "move":
        print("Ring ring ring!")
    varInput = int(input())
    while varSystem != varInput:
        print("Wrong Password. ")
        print("Ring ring ring!")
        varInput = int(input())
    if varSystem == varInput:
        print("System Disabled.")
        System = Not_Activated





    



car_from = input("Car is from: ")

if car_from == "west" or car_from == "east":
    print("Top Left Traffic Light: Green")
    print("Bottom Right Traffic Light: Green")
    print("Top Right Traffic Light: Red")
    print("Bottom Left Traffic Light: Red")
    print("\nCars from east and west GO!")
else:
    print("Top Left Traffic Light: Red")
    print("Bottom Right Traffic Light: Red")
    print("Top Right Traffic Light: Green")
    print("Bottom Left Traffic Light: Green")
    print("\nCars from north and south GO!")





while State == Close:
    if Command == "Power":
        State = Open
        print(f"Temperature: {Temperature}°C")
    else:
        Command = input()

# -------------------------------------------------------

# Exception Handling
try:
    meaning = 42
    print(meaning / 0)
    print("the meaning of life")
except (ValueError, TypeError):
    print("ValueError or TypeError occurred")
except ZeroDivisionError:
    print("Divided by zero")

def withdraw(amount):
   print(str(amount) + " withdrawn!")

try:
   money = int(input())
   withdraw(money)
except ValueError:
    print("Please enter a number")

try:
  print(1)
except:
  print(2)
finally:
  print(3)

# File Handling

file = open("btch.txt")
cont = file.read(5)
print(cont)
file.close()


file = open("btch.txt", "rb")
cont = file.read()
print(cont)
file.close()

n = int(input())

file = open("btch.txt", "w+")
#your code goes here
for i in range(1, n + 1):
    file.write(f"{i}\n")
file.close()

f = open("btch.txt", "r")
print(f.read())
f.close()