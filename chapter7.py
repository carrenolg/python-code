'''
# Chapter7 - Mangle Data Like a Pro
# Text String


# Python 3 Unicode strings
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('J')
unicode_test('\u004A')
unicode_test('\u2603')

# Encoding
# Encode a string to byte
snowman = '\u2603'
print(len(snowman))  # Character
ds = snowman.encode('utf-8')
print(len(ds))  # Bytes
print(ds)
print(type(ds))

# Decoding
place = 'caf\u00e9'
print(place)
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
place2 = place_bytes.decode('utf-8')
print(place2)

# Format
# Integer
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

# float
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

# Integer and literal
print('%d%%' % 100)

# Integer interpolation
cat = 'Chester'
weight = 28
print("Our cat %s weighs %s pounds" % (cat, weight))


# New style formatting
n = 42
f = 7.03
s = 'string cheese'
print('{} {} {}'.format(n, f, s))

# Specify the order
print('{2} {1} {0}'.format(n, f, s))

# Using dict or name arguments
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))  # {0} is dict, and {1} is 'other'

# Positional arguments
print('{var1:d} {var2:f} {var3:s}'.format(var1=42, var2=7.03, var3='string cheese'))

# minimum field width, maximum character width, alignment, and son on
# Minimum field width 10, right-aligned (default):
print('{0:<10d} {1:f} {2:s}'.format(n, f, s))
print('{0:>10d} {1:f} {2:s}'.format(n, f, s))

# Minimum field width 10, centered:
print('{0:^10d} {1:f} {2:s}'.format(n, f, s))

# 1:>10.4f - .4 precision value (not integer)
# 2:10.10s - .10 max numbers of characters
print('{0:>10d} {1:>10.4f} {2:10.10s}'.format(n, f, s))

# fill characters - Wow
print('{0:*^50s}'.format('BIG SALE'))


# Match with Regular Expressions
import re
result = re.match('You', 'Young Frankenstein')
print(result)
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')

# Exact match with match()
import re
source = 'Young Frankenstein'
m = re.match('You', source)  # match starts at the beginning of source
if m:  # match returns an object; do this to see what matched
    print(m.group())

m = re.match('^You', source)
if m:
    print('match:', m.group())

m = re.match('.*Frank', source)
if m:
    print('match:', m.group())

# First match with search()
m = re.search('Frank', source)
if m:
    print('search:', m.group())

# findall()
m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

# 'n' followed by any character
m = re.findall('n.?', source)
print(m)

# Split at matches with split()
m = re.split('n', source)
print(m)

# Replace at matches with sub()
m = re.sub('n', '?', source)
print(m)

# Patterns: special characters
import string
import re
printable = string.printable
print(len(printable))
print(printable[0:50])

# print only digit
result = re.findall('\d', printable)
print(result)

# print only alphanumeric
result = re.findall('\w', printable)
print(result)

# print spaces
result = re.findall('\s', printable)
print(result)

# RE not only ASCII
x = 'abc' + '-/*' + '\u00ea' + '\u0115'

# find only letters
result = re.findall('\w', x)
print(result)

# Patterns: using specifiers
import re
source = \'''I wish I may, I wish I might Have a dish of fish tonight.\'''
# find anywhere
print(re.findall('wish', source))

# find wish or fish anywhere
print(re.findall('wish|fish', source))

# find wish at the beginning
print(re.findall('^wish', source))

# fish at the end
print(re.findall('fish$', source))
print(re.findall('fish tonight.$', source))
print(re.findall('fish tonight\.$', source))

# Begin by finding w or f followed by ish
print(re.findall('[wf]ish', source))

# Find one or more runs of w , s , or h :
print(re.findall('[wsh]+', source))

# Find ght followed by a non-alphanumeric
print(re.findall('ght\W', source))

# Find I followed by wish :
print(re.findall('I (?=wish)', source))

# And last, wish preceded by I :
print(re.findall('(?<=I) wish', source))

# Here, would have some conflict, "\b" means the beginning of a word
# scape characters vs. regular expressions
print(re.findall(r'\bfish', source))

# Patterns: specifying match output
# some outputs
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())
my_source = \'''a has a dish of fish tonight \'''
m = re.search(r'(?P<DISH>.has\b).*(?P<FISH>\bfish)', my_source)
print(m.group())
print(m.groups())
print(m.groups('DISH'))
print(m.groups('FISH'))

# Binary Data
# bytes and bytearray
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)
# the_bytes[1] = 127  # It's immutable
the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)  # It's mutable
b = bytes(b'\x0a')
print(str(b))
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
print(the_bytes)
print(the_byte_array)

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
print(len(valid_png_header))
print(len(data))
print(data[20:24])
print(b'x9a')
# Python data to bytes
data = struct.pack('>L', 256)
print(data)

# Things to Do
mystery = '\U0001f4a9'
print(mystery)


# Funct
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test(mystery)

# 7.2
pop_bytes = mystery.encode('UTF-8')
print(pop_bytes)
print(type(pop_bytes))
pop_string = pop_bytes.decode('UTF-8')
print(pop_string)

# 7.12
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + \
          '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))

# Examples
string = '\u0071'
sd = '{'
print(string)
print('{' == '\u007B')
'''

