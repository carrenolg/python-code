# import modules
from collections import Counter
from collections import OrderedDict
import itertools
from pprint import pprint

# chapter5 - Py Boxes: Modules, Packages,
# and Programs
from collections import defaultdict

# setdefault()
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

# key was not already in the dict
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)

# other example
helium = periodic_table.setdefault('Helium', 947)
print(helium)

# the 'defaultdict()'
periodic_table = defaultdict(list)
periodic_table['Hydrogen'] = [0, 1]
periodic_table['Lead']
periodic_table['Gio']
print(periodic_table)


# defaultdict() with function as arguments
def no_idea():
    return 'Huh?'


bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
bestiary['C']
print(bestiary['C'])

# defaultdict() with lanbda
bestiary = defaultdict(lambda: 'Huh?')
bestiary['G']
print(bestiary['G'])

# defaultdict() using int like argument, we can create counter() function
data_types = defaultdict(int)
for element in ['int', 'str', 'boolean', 'list', 'int', 'int']:
    print(data_types[element])
    data_types[element] += 1

for key, value in data_types.items():
    print(key, value)

# Count Items with Counter()
breakfast = ['spam', 'spam', 'eggs', 'spam', 'eggs', 'eggs']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
# print(breakfast_counter.most_common())

# another example
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

# combine counter
print('add:', breakfast_counter + lunch_counter)

# subtract counter
print('Sub:', breakfast_counter - lunch_counter)
print('Sub:', lunch_counter - breakfast_counter)

# intersection operator
print('Intersection:', breakfast_counter & lunch_counter)

# Order by Key with OrderedDict()

quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
}

for item in quotes:
    print(item)


qt = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

for item in qt:
    print(item)

# Stack + Queue = Deque


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))    

# Iterate over Code Structures with itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# cycle
for binary in itertools.cycle([0, 1]):
    print(binary)

# accumulate
for accumulate in itertools.accumulate([1, 2, 3, 4, 5, 6]):
    print(accumulate)


# accumulate with multiply
def multiply(x, y):
    return x * y


for accumulate in itertools.accumulate([1, 2, 3, 4, 5, 6], multiply):
    print(accumulate)

# pprint()
qt = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

print(qt)
pprint(qt)


# Things Do
# 5.1
import zoo
print(zoo.hours())

# 5.2
import zoo as menagerie
print(menagerie.hours())

# 5.3
from zoo import hours
print(hours())

# 5.4
from zoo import hours as info
print(info())

# 5.6
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)
from collections import OrderedDict
print(OrderedDict(plain))

# 5.7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
