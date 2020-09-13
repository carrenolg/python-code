
# Merge two list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
others_2 = ['Goku']
marxes.extend(others)
marxes += others_2

# Insert
marxes.insert(3,'Gummo')

# Remove
marxes.remove('Gummo')

# Get and delete an Item at the same time, wow it is great
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)

# Find Item's offset by Value with Index
marxes = ['Groucho', 'Chico', 'Zeppo', 'Harpo', 'Zeppo']
print(marxes.index('Zeppo'))

# Test for a Value with in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Harpo']
find = 'Harpo' in marxes
print(find)

# Count Occurrences of a Value by Using count()
marxes = ['Groucho', 'Chico', 'Harpo', 'Chico', 'Chico', 'Chico']
count = marxes.count('Chico')
print(count)

# Convert to a String with join()
marxes = ['Groucho', 'Chico', 'Harpo']
res = '//'.join(marxes)
print(res)

# Reorder Items with sort()
marxes = ['Groucho', 'Carlos', 'Chico', 'Harpo', 'Aron']
sorted_marxes = sorted(marxes)
print(sorted_marxes)  # return a sorted copy of the list

# if items are string, they sorted in alpha order
# if items are numeric, they sorted in ascending numeric order
numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

# Get Length by Using len()
marxes = ['Groucho', 'Carlos', 'Chico', 'Harpo', 'Aron']
print(len(marxes))


# Assign with =, Copy with copy()
a = [1, 2, 3, 4]
print(a)
b = a  # copy by reference, WOW
print(b)
a[0] = 'surprise'
print(a)
print(b)
b[0] = 'I love the surprises'
print(a)
print(b)

# copy the values of a list to an independent
# use copy(), list(), or slice[:]
a = [1, 2, 3, 4, 5]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
a[0] = 'integer list are complex, the\'re not simples data types'
print(a)
print(d)
print(c)
print(d)

# Tuples ********************************************************

empty_tuple = ()
print(empty_tuple)
one_marx = 'Groucho',
print(one_marx)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
# tuple unpacking, Wow
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)
# change values with tuples
text = 'hello'
password = '1q2w3e'
text, password = (password, text)
print(text)
print(password)
# conversion, tuple() function
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_tuple))

# Dict ********************************************************
empty_dict = {}
print(empty_dict)
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)
# dict function
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lol)
print(type(lol))
dict_lol = dict(lol)
print(dict_lol)

# dict from list of strings
los = ['wr', 'ef', 'gt']
print(dict(los))

# dict from tuple
tos = ('ab', 'cd', 'ef')
print(dict(tos))
# Add or Change an Item by [ key ]
pythons = {'Chapman':'Graham', 'Cleese':'John', 'Idle':'Eric', 'Jones':'Terry', 'Palin':'Michael',}
pythons['Gilliam'] = 'Gerry'
print(pythons)
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

# Delete an Item by Key with del
del first['a']
print(first)
# delete all items
pythons = {'Chapman':'Graham', 'Cleese':'John', 'Idle':'Eric', 'Jones':'Terry', 'Palin':'Michael',}
print(pythons)
pythons.clear()
print(pythons)

# check if items exist into the dict
pythons = {'Chapman':'Graham', 'Cleese':'John', 'Idle':'Eric', 'Jones':'Terry', 'Palin':'Michael',}
res = 'Chapman' in pythons
print(res)

# get item by key
print(pythons['Jones'])

# check before getting if exist the item
res = pythons.get('Gio', 'Item not exist')
print(res)

# get all keys
print(pythons.keys())

# get values
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())

# Assign with =, Copy with copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(signals)
print(save_signals)
copy_signals = signals.copy()
copy_signals['green'] = 'Hello'
print(signals)
print(copy_signals)

# Set
empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

# Convert from Other Data Types with set()
new_set = set('letters')
print(new_set)
# Create set from a list
list_set = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(list_set)
# Set from a tuple
tuple_set = set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))
print(tuple_set)
# Set from a dict
dict_set = set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
print(dict_set)

# Test value
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
print(drinks)
# Check values
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# Combinations and Operators
# Check many values at the time (Combinations)
# Example: check if any drink has 'orange juice' or 'vermouth'
for name, contents in drinks.items():
    if contents & {'orange juice', 'vermouth'}:
        print(contents & {'orange juice', 'vermouth'})
        print(name)
print('###########')
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'cream', 'vermouth'}:
        print(contents & {'cream', 'vermouth'})
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# intersection
print(a & b)
print(a.intersection(b))
# Union
print(a | b)
print(a.union(b))
print(bruss | wruss)
# different
print(a - b)
print(a.difference(b))
# exclusive
print(a ^ b)
print(a.symmetric_difference(b))
# check subset
print(a <= b)
print(a.issubset(b))
# proper set
print(a < b)

# Things to do
years_list = [1990, 1991, 1992, 1993, 1994, 1995]
print(years_list[3])
print(years_list[5])
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)
things[0] = things[0].upper()
print(things)
things.remove("salmonella")
print(things)
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
surprise[-1] = surprise[-1].lower()
print(surprise)
surprise[-1] = surprise[-1].capitalize()
print(surprise)
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f['walrus'])
# P3.12
f2e = dict([(value, key) for key, value in e2f.items()])
print(f2e['chien'])
ekeys = set(e2f.keys())
print(ekeys)

# P3.15
life = {
    'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}},
    'plants': {},
    'other': {}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
