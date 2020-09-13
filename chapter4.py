# Chapter 4
# 60 sec/min * 60 min/hr * 24 hr/day
# seconds_per_day = 86400
seconds_per_day = 86400  # 60 sec/min * 60 min/hr * 24 hr/day

# Continue Lines with \
alphabet = 'abcdefg' + \
    'hijklmnop' + \
    'qrstuv' + \
    'wxyz'
print(alphabet)

# Compare with if, elif, and else
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

# Some examples about comparison
# make multiple comparisons and, or, not
x = 7
r = (5 < x) and (x < 10)
print(r)
r = (5 < x) and not (x > 10)
print(r)
# multiple comparisons with one variable
r = 5 < x < 10
print(r)
# longer comparisons
r = 5 < x < 10 < 5
print(r)

# Python use another ways to check for empty data structures
# No only use boolean values
# Considered an value "False"
# (null | None)
# (int | 0)
# (float | 0.0)
# (empty string | "")
# (empty list | [])
# (empty tuple | ())
# (empty dict | {})
# (empty set | set())

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

# Do Multiple Comparisons with in
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

# Check values using "in"
# string
vowels = "aeiou"
letter = 'o'
print(letter in vowels)

# Set
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

# list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_set)

# tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

# dict
vowel_dict = {'a': 'apple', 'e': 'elephant','i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict)


# Repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1

# loop infinite with break statement
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

# Skip Ahead with continue
while True:
    value = input("Integer, [please type q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)

# Use break with else
numbers = [1, 5, 3]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number: ", number)
        break
    position += 1
else:  # break not called
    print('No even number found')

# For
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# Better
for rabbit in rabbits:
    print(rabbit)

# dict
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:  # or, for card in accusation.keys():
    print(card)

# Values
for value in accusation.values():  # or, for card in accusation.keys():
    print(value)

# Item
for item in accusation.items():  # or, for card in accusation.keys():
    print(item)

# zip() to pair tuples
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
lst = list(zip(english, french))
print(lst)
zip_dict = dict(zip(english, french))
print(zip_dict)

# Zip
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

binary = ["True", "False", "Other"]
integer = [1, 0]

print(tuple(zip(integer, binary)))
new_dict = dict(zip(integer, binary))
print(new_dict[1])

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# Generate Number Sequences with range()
for item in range(0, 3):
    print(item)

print(list(range(0, 3)))

# make a range from 2 down to 0
for item in range(2, -1, -1):
    print(item)

# Comprehensions
# List Comprehensions
# create a list without using comprehension
number_list = list(range(1, 6))
print(number_list)
# create a list using comprehension
number_list = [number for number in range(1, 6) if number % 2 == 1]
print(number_list)

# Using comprehension to create cells
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# Dictionary Comprehensions
word = 'letters'
letters_count = {letter: word.count(letter) for letter in word}
print(letters_count)
# Now using set()
letters_count = {letter: word.count(letter) for letter in set(word)}
print(letters_count)

# Set Comprehensions
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# Generator
number_thing = (number for number in range(1, 6))
print(type(number_thing))
number_list = list(number_thing)
print(number_list)
try_again = list(number_thing)
print(try_again)

# Functions


def agree():
    return True


if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

# Parameters


def echo(anything):
    return print(anything + ' ' + anything)


echo('LAM')

# With parameters and arguments


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary('blue')
print(comment)


# None value on functions


def do_something():
    pass


print(do_something())

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

# distinguish None from boolean False

if thing is None:
    print("It's some thing")
else:
    print("It's no thing")


def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))
# Using
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# Specify Default Parameter Values


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))

# Important, Default argument values are calculated when the function is
# defined, not when it is run


def buggy(arg, result=[]):
    result.append(arg)
    print(result)

# In above function: there’s a bug: it’s empty only the first time it’s called. The second time, result
# still has one item from the previous call:


print(buggy('a'))
print(buggy('b'))

# fixing last bug


def works(arg):
    result = list()
    result.append(arg)
    return result


print(works('a'))
print(works('b'))


def non_buggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


print(non_buggy('a'))


# Wow


def print_args(*args):
    print('Positional argument tuple:', args)


print(print_args())  # Nothing return

print(print_args(3, 2, 1, 'wait!', 'uh...'))


# If your function has required positional arguments as well, *args goes at
# the end and grabs all the res


# Gather Positional Arguments with *


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


# Gather Positional Arguments with *


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# Docstrings


# Functions Are First-Class Citizens


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


print(run_something_with_args(add_args, 5, 4))

# another example with *arg and **kwarg


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4, 5))


# Closure functions examples

def parent_function(name):
    def child_function():
        print("I am a child function called " + name)
    return child_function


closure = parent_function('Gio10')
print(closure)
print(type(closure))
closure()

# Anonymous Functions: the lambda() Function


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):  # give that prose more punch
    return word.capitalize() + '!'


# edit_story(stairs, enliven)

edit_story(stairs, lambda arg: arg.capitalize() + '!')


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number * 2
        number += step


ranger = my_range(1, 20)
print(ranger)

for item in ranger:
    print(item)


# Decorators

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

# Another decorator


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# Manual decorator
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


# No manual
print(add_ints(3, 5))


# Things to Do

# 4.4
numbers = [number for number in range(10)]
print(numbers)
# 4.5
squares = {number: number*number for number in range(10)}
print(squares)
# 4.6
odd_numbers = set(number for number in range(10) if number % 2 == 1)
print(odd_numbers)
# 4.7
for item in ['Got %s' % num for num in range(10)]:
    print(item)


