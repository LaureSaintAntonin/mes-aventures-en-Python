# variables   (cant start w/ numbers, no space, or keywords like for etc)
name = 'Nathan'
age = 25

# expression = any code that returns a value
1+1

# statement = operation
name = 'Nathan' ; print(name) # can add multiple statement with ;

#data types : str, int, float, bool
print(type(name)) # ≠ ways to test datatype
print(type(name) == str)
print(isinstance(name,str))

age = float(25)     # can convert data types
print(isinstance(age, float))

#number = 'test'   # can't convert everything, str -> in if its letters  will not works
# age = int(number)
# print(isinstance(age, int))

# other datatypes
complex
bool
list
tuple
dict # type for dictionnary
set # type for sets

# arithmatics operators + ; - ; * ; / ; % ; ** ; // (arrondi à l'entier)
age = 8
age *= 4 # age = age * 8 ; can be done w/ any of arithm. op.
age = 9
print(age)
print(age % 2) # donnera le reste de la division par 2


# comparison operators
a = 1 ; b = 2
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

# boolean operators
condition1 = True
condition2 = False
print(not condition1)
condition1 and condition2
    # OR
print(0 or 1) #  OR return first non false value ; 0 is considered a falsie value
print(False or 'hey')
print('hi' or 'hey') # will return the first bc is not falsie value
print([] or False)   # ttt par la machine: if x is false; else return y etc...
print(False or []) # will return the 2nd if the first is false even if both are false, same way that for 'hi' & 'hey'
    # AND
print(0 and 1) # AND only evaluates the 2nd arg. if the 1st is True ; here 0 is False so it prints 0
print(1 and 0) # here 1 is True so print 0
print(False and 'hey') # False is falsy so it prints it
print('hi' and 'hey') # ttt par python: if x is True: else y

# Bitwise operators
# & performs binary AND
# | (opt + maj + L) performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# IS and IN
is # Identity operator: compare 2 objects and return True if both are the same object
in # Membership operator: True if a value is contained in a sequence

# Ternary Operator: also to quickly define a conditional
age = 20
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
def is_adult2(age):    # allowed to do an IF: ELSE statement on a single line
    return True if age > 18 else False
print(is_adult(age))
print(is_adult2(age))

# Strings
name = 'Nathan'
phrase = name + ' is my name'
print(phrase)
name += ' is my name'
print(name)
    # can make it multi-lines w/ """ flkze """
print("""Nathan is   
39 
years old
""")
    # .method DONT ALTER the original 'str', create new
print("Nathan".upper())
print("Nathan".lower())
print("NatHan pESneAu".title())
print("Nathan".islower()) # check if all lowercase and return True of False
print("Nathan3".isalpha()) # check if only letters
print(name.isalnum())      # if alpha-num
.isdecimal()
.islower()
.isupper()
print(name.startswith('Na'))
.endwith()
.replace()
.split()
print('   Nathan is handsome. '.strip()) # enlève esp av & ap
print(' '.join(["Nathan","is","cool"]))
.find() # donne position of a substring

# other related to 'str'
name = 'Nathan'
print(name.lower())
print(name)    # dont alter the original 'str' create a new one

print("an" in name)
print(len(name))

# add special character in 'str'
print("Nathan dit: \"Ah bon ?\"")
print('Nathan \nConsomme du code') # retour à la ligne au sein 'str'
print('Nathan\\Pesneau') # if you wanna add a \ in the str you have to put 2

print(name[0]) # 0 is the first letter, -1 is the last one etc
print(name[1:2]) # will start at name[1] and end before name[2]
print(name[:5])  # all until name[5] excluded

#bool type
done = 12        # except 0, all numbers are True, even -5
done = ''         # str are False only when empty ; same for list, tuple, dictonnary
done = True
if done:            # on test ici par défaut si done est True, si c'est le cas 'Yes'
    print('yes')
else:
    print('No')
# any
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read,book_2_read]) #if at least 1 one value is true
print(read_any_book)
# all
ingredients_purchased = True
meal_cooked = False
ready_to_serve = all([ingredients_purchased, meal_cooked]) # if all are True
print(ready_to_serve)

# complex numbers           all numbers are defined by 1 part in R, and an other one from imaginary
# i in maths, j in ingeneering
complex_num = 2+3j  # here 2 = Reels  ; 3 = Imaginary part
print(complex_num.real, complex_num.imag)
num = complex(2,3) # same here
print(num.real, num.imag)

## Built-in F° for numbers ##
print(abs(-5.5)) # return absolut value
print(round(5.465,1)) # 1 correspond to decimal rounded

# Enums
from enum import Enum

class State(Enum): #creating a var called State.INACTIVE which = 0 etc
    INACTIVE = 0
    ACTIVE = 1          # is use in python to create a constant

print(State.ACTIVE.value) # to get the value
print(State(1))
print(State['ACTIVE'])

print(list(State))
print(len(State))

# User input
age = input('What is your age? ')
print('You are '+ age + ' years old.')
print(f'You are {age} years old.')
# exists more complex input

# Control statement: if ; While ; for etc
condition = False
if condition == True:
    print('The condition was true')
elif condition == False:
    print('The condition was false')
else:
    print('Unknown')

#lists
dogs = ['Roger', 'Syd', True, 16, 'Quincy', 7] # can mix ≠ types of datatypes
print('Roger' in dogs)
print(dogs[0]) # through position
no_dogs = [] # can be empty & will be falsy
dogs[2] = 'Bazil' # can modify through index
print(dogs[-2])

print(dogs[2:4]) #will print from 2 to 4 excluded => [2] & [3]
print(len(dogs))

dogs.append('Loumi')
dogs.extend(['Emy',5])
dogs += ['Fish','Doggo']        # add at the end like .extend / .append
print(dogs)

dogs.remove('Quincy')   # remove, possible by name, index...
print(dogs.pop())   # pop remove and return the last item from the list
print(dogs)

items = ['Roger', 'Syd', True, 16, 'Quincy', 7]
items.insert(2, 'test')   # will be added after items[2] which is: True
print(items)
items = ['Roger', 'Syd', True, 16, 'Quincy', 7]
items[1:1] = ['test1','test2']    # will add from index 1, but stop before 1 => will not smash 'Syd'
items = ['Roger', 'Syd', True, 16, 'Quincy', 7]
items[1:2] = ['test1','test2']   # here its stop before index 2, so it will delete 'Syd'
print(items)


dogs_only = ['Roger', 'Syd', 'Bazil', 'Quincy', 'Loumi', 'Emy', 'Fish']
dogs_only.extend(['albert']) # UPPERCASE are ordered first before lowercase
dogs_only_copy = dogs_only[:] # [:] means from beginning to end
dogs_only.sort()             # .sort modify the list
print(dogs_only)
dogs_only.sort(key=str.lower) # can add key to modify conditions of sorting
print(dogs_only)
print(dogs_only_copy)# .sort modify the list so can create a copy

dogs_only.reverse() # permet d'inverser l'ordre de la list
#other way to sort w/out modifying the list
dogs_only = ['Roger', 'Syd', 'Bazil', 'Quincy', 'Loumi', 'Emy', 'Fish']
print(sorted(dogs_only,key=str.lower)) #return a new list sorted
print(dogs_only)

## tuples = immutables group of obj.    ;  written like lists but w/ ()
names = ('Roger','Syd','George')
names[0]
names.index('Roger')
print(len(names))
print('Roger' in names)

print(names[0:2]) #can also slice

sorted(names) #can be used bc creates a list which is a copy of the tuple
newTuple = names + ('Quincy','')
print(newTuple)

## Dictionaries   { key: value }     create key value pairs
dog = { 'name': 'Roger', 'age': 8}
print(dog['name'])
dog['name'] = 'Syd' # directly modify the name
print(dog)
print(dog.get('name'))  # get the the key or the value associated w/ the arg (here name, so will return 'Syd')
print(dog.get('color','brown'))  # return none if doesn't exist / 2nd arg. if specified

print(dog.pop('name')) #pop = here will delete key name & the value associated
print(dog)

dog['color'] = 'Brown'
print(dog)
print(dog.popitem())  #.popitem() will delete last item add to the dict
print(dog)

print('name' in dog)
print(dog.keys()) # will show the dictionary's key
print(dog.values())
print(dog.items())
print(list(dog.keys())) #add list to just obtain the list without dict_keys in front
print(len(dog)) # 1 per pair {key : value}

dog['favorite food'] = 'chicken' # directly add new item
print(dog)
dog_copy = dog.copy()
del dog['favorite food']
print(dog)

## Sets   ;   works with bitwise operators   ;  CANT have 2 times the same item
set1 = {'Roger','Syd'}  # { item1 , item2 , ... } but arent ordered
set2 = {'Luna'}
mod = set1 & set2 # AND in binary => va prendre les items communs
mod = set1 | set2 # OR  ......... => get every item in both sets
print(mod)

set1 = {'Roger','Syd'}  # { item1 , item2 , ... } but arent ordered
set2 = {'Roger'}
mod2 = set1 - set2  # order is important
print(mod2)

mod = set1 > set2  # check if one is included in the other
print(mod)  # True => Set1 is a superset of Set2, and set2 is a subset of set1

print(list(set1))

## Functions ##
# essentials in programming: 1) allow to decompose prog. in manageable part 2) promote redability / code reuse
# name of fun must be descriptive of what it does
def hello(name = 'my friend'): # here name is optional and if there is no arg, will use it by default
    print('Hello! ' + name)
hello()
hello('Nathan')
#   parameters = value accepted by the funct inside the definition
# ≠ arguments  = value that pass through the funct when we call it

def hello(name, age): # here name is optional and if there is no arg, will use it by default
    print(f'Hello  {name}, you are {age} years old!')
hello('Nathan', 25)

# all types in python are objets
# some are immutable: int, str, bool, float, tuples
#   => if you pass them as parameters, and you modify them values inside the f°
#      the new value will no be reflected in the outside of the function.

# others objects are mutable, for ex: dictionary
def change(value):
    value['name'] = 'Syd'
val = {'name': 'Roger'}
change(val)
print(val)  # so here the change in the function reflects outside of it

def hello(name):
    name += ', tu es très sympathique.'
    print('Hello ' + name + '!')
    return name    # when a fun hits return
print(hello('Nathan')) # print will also show parameters which are returned


## Variable scope
age = 8   # global var. bc declared outside a function
def test():
    age = 8    # local var. bc declared inside a function
    print(age)

print(age)
test()

# Nested functions    = f° in an other f°
def talk(phrase):
    def say(word):    #f° that you need for an other f° to work must be nested to simplify the code + we can make use of ?closures ?
        print(word)
    words = phrase.split(' ') # .split create a list from a 'str' every ' ' it founds
    for word in words: # ? is word pre-build detected or is it just a parameter ?
        say(word)
talk("I am going to buy milk")

def count():
    count = 0
    def increment ():
        nonlocal count # nonlocal permits to detect count even if not defined here in this f°
        count = count + 1
        print(count)
    increment()
count()

# closures
def counter():
    count = 0
    def increment ():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter() # we stock counter() results in increment
print(increment())   # bc we are calling only the inner it'll not re-asignes 0 to var. count
print(increment())   # so even if we just call the inner f, it still has access to var. count
print(increment())

## 0bjects ##
# everything in python are objects
# the have attributes & methods (.example)

age = 8  # the object age has now accesses to the properties & methods defined for all objects
         # for ex: has access to imaginary part of numbers
print(age.real)
print(age.imag)
print(age.bit_length()) # .bit_length returns the number of bits necessary to represents the numb. in bit notation

items = [1,2]
items.append(3)
print(items.pop())
print(id(items))  # id() access location in memory

# objects are mutable or immutable
# if there is .method usable => its mutable

#ex: int are immutable
age = age + 1 #will not modify it but re-create a new object age
# but will be possible for a dictionary for example

## Loops    : 2 kinds : while   & for   ##

condition = True
while condition == True:  # infinite loop
    print('The condition is True')
    condition = False

#while loop
count = 0
while count < 10:  #common to have an iteration to stop the loop after a certain amount of cycle
    print('The condition is true')
    print(count)
    count += 1
print('After the loop')

#for loop
for item in range(15): # range of 15 items begin to 0 => 0:14
    print(item)

items = ['Nathan','Val','Toto','Coco']
for index, item in enumerate(items): # enumerate() show the index of items
    print(index, item)

# continue -> stops the current iteration and go to the next one
# break stops the loop altogether and go to next instruction after the loop ends
items = [1,2,3,4]
for item in items:
    if item == 2:
        continue   #skip current iteration & go to the next iteration
    print(item)

items = [1,2,3,4]
for item in items:
    if item == 2:
        break    # here stops the loop entirely
    print(item)

# Classes    ; we can declare our own classes & then instanciate objects
class Dog:              # ici on créée une classe de type Dog
    def __init__(self, name, age):  # here we use constructor to initialise one more properties when we create a new objet of that class
        self.name = name       # here we added 2 var. we can pass in when we create a dog
        self.age = age
    def bark(self):
        print('woof!')
roger = Dog('Roger', 8)           # ici on attribue la class Dog() à l'objet roger
print(roger.name)
print(roger.age)
roger.bark()

# Class feature : inheritance
class Animal:
    def walk(self):
        print('Walking...')

class Dog(Animal):   # by putting Animal inside the () => objects of dog class will inherit the method walk
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('woof!')
roger = Dog('Roger', 8)
roger.bark()
roger.walk()

# Modules
# every python file is a module, you can create a python software from ≠ python files
from lib import dog
dog.bark()

from lib.dog import bark # here we just import the function we need
bark()   # here I can run bark() directly bc we imported just it from the module dog

# if module is a subfile, we need __init__.py function
from lib import dog
dog.bark()

from lib.dog import bark
bark()

## Python standard library (prebuilt function) ##

# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work w/ dates
# sqlite3 to use SQLite
# os for Operation System utilities
# random for random generation
# statistics for stats
# requests  to perform HTTP network requests
# urllib    to manage URLs
import math
print(math.sqrt(4)) # square root of 4
from math import sqrt
print(sqrt(4))

# Accepting Arguments from Command Line
# CF fromtheterminal.py
# in the terminal:     python BasicsCommand.py
print('Hello')
import sys
print(sys.argv)

# Lamda functions       : tiny functions (no name, 1 expr as body)
lambda num : num * 2  # num = argument ; num * 2 = the expression (returns a value (≠ statement does not))
                      # here it doubles the value of a number
multiply = lambda a, b : a * b   # can be stock in object ; can have more than 1 argument
print(multiply(2, 4))
# utility when combined w/ other functionalities ex: map, filter, reduce

## functions : Map, Filter, Reduce ##

# map ()
numbers = [1, 2, 3]
# def double(a):   when a function is 1 lign => common to use lambda
#    return a * 2
result = map(lambda a : a * 2, numbers) # map() creates a new list w/ same values BUT those are iterables / can be changed w/ a function we specify
print(list(result))
# lambda is here very useful to reduce length of the code

# filter()    takes an iterable object, returns a filter object which is another iterable but w/out some of the original items
numbers = [1, 2, 3, 4, 5, 6]
def isEven (n):        # the filtering function
    return n % 2 == 0  # retourne True si reste == 0 après div <=> si la valeur est un multiple de 2
result = filter (isEven, numbers)
print(list(result))

numbers = [1, 2, 3, 4, 5, 6]  # here code optimize w/ lambda f°
result = filter (lambda a : a % 2 == 0, numbers) # va retourner les valeurs pour lesquelles le résultats de l'argument 1 est vrai, et l'applique à l'ensemble de l'argument 2
print(list(result))

## reduce()   calculates a value out of a sequence (like list)
# w/out reduce()
expenses = [            # here is a list stored as tuples
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)

# w/ reduce()     : way shorter
from functools import  reduce
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum = reduce (lambda a, b: a[1] + b[1], expenses) # va effectuer l'opération de l'argument 1 sur l'argument 2 en répétant l"opération jusqu'à ne plus avoir qu'une valeur
print(sum)

## Recursion
# a python function can call itself
def factorial(n):
    if n == 1: return 1            # this line will stop the recursion    : always need to have a base case so eventually the recursion will stop
    return n * factorial(n-1)      # recursion = calling the f° in the f°
print(factorial(4))

# Decorators    @  :   way to change how a python f° works w/out changing the function itself
# ex of usage:  add logging, test performance, perform caching, verify permissions...
# ex2: also when you need to run the same code on multiple functions
def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper
@logtime    # this decorator function make hello() be an inner function of logtime ?
def hello():
    print('hello')
hello()

## Docstrings
# comments with # are helpful to get other to understand your code  /  for you if you come back to it after a long time

def increment(n):
    """Increment a number"""  # docstring are a convention to define what does a f°, a class, a method
    return n + 1

# at the beginning of a code to explain what the file is all about
"""Dog module

This module does ... and provides the following classes:
- Dog
-
...
"""
class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialise a new dog"""
        self.name = name
        self.age = age
    def bark(self):
        """Let the dog bark"""
        print('Woof!')

print(help(Dog))    # just by adding these comments, help() will give info
# there are others method to access this info about code

# Annotations
def increment(n: int) -> int:  # even if python is a dynamic language (no need to specify the type of the values)
    return n+1                 # you can still specify the types (Python will ignore those)
count: int = 0
    # a separate tool called mypi can be use to check for types error.


# Exceptions : to handle errors and move on with the program
try:
    result = 2/0
    # some lines of code
except <ERROR1>:    # specify a type of error to see if it happened
    # handler <ERROR1>
except: # to catch all exceptions
else: # will run if no errors are found
finally:
    # do something in any case

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1
print(result)

raise Exception('An error!') # to print a general exception

try:
    raise Exception('An error!')
except Exception as error:
    print(error)

class DogNotFoundException(Exception):
    print ('inside')
    pass # means nothing, used when we define a class without methods or a function w/out code

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')


# With  :    really useful to simplify working w/ exception handling

filename = '/User/npesneau/test.txt'
try:
    file = open(filename,'r')
    content = file.read()
    print(content)
finally:
    file.close()

with open(filename,'r') as file:  # same thing but using 'with' which will autoatically close the file at the end + built-in implicit handling
    content = file.read()
    print(content)


# Third-party packages    :     how to install using pip
        # people / companies make packages as open source software for the community
        # modules are collected in a single place at: pypi.org (270 000 available)
# in the shell: pip install 'name of the package'
# to update     pip install -U 'name of the package'
# to uninstall  pip uninstall 'name of the package'
# to get info   pip show 'name of the package'


# List Compressions     : way to create lists in a very concise way
numbers = [1, 2, 3, 4, 5]

numbers_power_2 = []        # long version
for n in numbers:
    numbers_power_2.append(n**2)
print(numbers_power_2)

# w/ list compression
numbers_power_2 = [n**2 for n in numbers]  # use when operation can be written on a single line -> better readability
print(numbers_power_2)


# Polymorphism  :   generalize a functionality so it can work on ≠ types
class Dog:
    def eat(self):
        print ('Eating dog food')
class Cat:
    def eat(self):
        print('Eating cat food')
animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()


# Operators Overloading
class Dog:
    """The Dog class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):  # method to use to compare (can use > < == ...)
        return True if self.age > other.age else False

roger = Dog('roger', 8)
syd = Dog('Syd', 7)

print(roger > syd) # return True

# there are also a lot of method w/ arithmetic operations
# __add__() respond to the + operator
# __sub__() to -
# __mul__() to *
# __truediv__() to /
# __floordiv__() to //
__mod__() to %
__pow__() ** #power
__rshift__() >> operator
__lshift__() << operator
__and__() & operator
__or__() | operator
__xor__()  ^ operator


# to select all the iteration of a word at the same time: cmd + d

