# Chapter8
# File Input/Output
# Write a Text File with write()
import pickle
'''
poem = \'''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.\'''
print(len(poem))
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

# another way
fout = open('print-relativity', 'wt')
print(poem, file=fout)

# more about print()
fout = open('advance-relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

# large strings, use chunks
size = len(poem)
offset = 0
chuck = 100
while True:
    if offset > size:
        break
    try:
        fout = open('chunk-relativity', 'xt')
        fout.write(poem[offset:offset+chuck])
    except FileExistsError:
        print('relativity already exists!. That was a close one.')
    offset += chuck
fout.close()

# Read a Text File with read(), readline(), or readlines()
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)
# read() returns limit of characters at the time
poem = ''
file = open('relativity', 'rt')
chunk = 100
while True:
    fragment = file.read(chunk)
    if not fragment:
        break
    poem += fragment

file.close()
print(len(poem))

# read file with readline()
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

# read file using by iterator
poem = ''
fin = open('relativity', 'rt')
print(type(fin))
for line in fin:
    poem += line

fin.close()
print(len(poem))

# Write a Binary File with write()
bdata = bytes(range(0, 256))
print(len(bdata))
fout = open('bdata', 'wb')
fout.write(bdata)
fout.close()

# Write binary data in chunks
fout = open('bdata', 'wb')
offset = 0
size = len(bdata)
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()

# Read a Binary File with read()
fin = open('bdata', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

# Close Files Automatically by Using with
letter = 'does bible say God is love'
with open('relativity', 'wt') as fout:
    fout.write(letter)

# Change Position with seek()
fin = open('bdata', 'rb')
print(fin.tell())
print(fin.seek(255))
bdata = fin.read()
print(len(bdata))

# Structured Text Files
# CSV
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]
with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# read CSV file
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    read_villains = [row for row in cin]

print(read_villains)

# read CSV with DictReader()
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    dict_villains = [row for row in cin]

print(dict_villains)

# rewrite file 'villains'
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(dict_villains)

# read again with DictReader
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    dict_villains = [row for row in cin]

print(dict_villains)

# XML
import xml.etree.ElementTree as et
tree = et.ElementTree(file='file.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print("tag:{0} attributes:{1}".format(child.tag, child.attrib))
    for grandchild in child:
        print("\ttag:{0} attributes:{1}".format(grandchild.tag, grandchild.attrib))

# accessing by offset
print(len(root[0]))

# Json
# menu is a dict
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

import json

json_data = json.dumps(menu)
print(type(json_data))
print('json:', json_data)

dict_data = json.loads(json_data)
print(type(dict_data))
print('dict:', dict_data)

# working on JSON with date
import datetime
import json
now = datetime.datetime.utcnow()
print(now)
# convert date to string
now_str = str(now)
json_data = json.dumps(now_str)
print(json_data)

# working with epoch value ('mktime')

import time
now_epoch = int(time.mktime(now.timetuple()))
json_epoch = json.dumps(now_epoch)
print(json_epoch)


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(time.mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)


json_epoch = json.dumps(now, cls=DTEncoder)
print(json_epoch)

# yaml file to dict
# pip install -U PyYAML
import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.safe_load(text)  # Important
print(type(data))  # type: dict
# example dict/list/dict reference
# print(data['poems'][1]['title'])
data['poems'][1]['title'] = 'Canadian Charms - Edit'
# print(data['poems'][1]['text'])

# dict to yaml file
yaml_data = yaml.safe_dump(data)
with open('mcintyre.yaml', 'wt') as fout:
    fout.write(yaml_data)

# Serialize by Using pickle
import datetime
now_01 = datetime.datetime.utcnow()
pickled = pickle.dumps(now_01)
pickle_now = pickle.loads(pickled)
print(now_01)
print(pickled)
print(pickle_now)


class Tiny:
    def __str__(self):
        return 'tiny'


obj1 = Tiny()
print(obj1)
pickle_obj1 = pickle.dumps(obj1)
print(pickle_obj1)
obj2 = pickle.loads(pickle_obj1)
print(obj2)
'''
# Relational Databases
# import sqlite3
# conn = sqlite3.connect('enterprise.db')
# curs = conn.cursor()
# curs.execute('''CREATE TABLE zoo\
#             (critter VARCHAR(20) PRIMARY KEY,\
#             count INT,\
#             damages FLOAT)''')
# curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
# curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
# ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
# curs.execute(ins, ('weasel', 1, 2000.0))
# curs.execute('SELECT * FROM zoo')
# rows = curs.fetchall()
# print(rows)
# curs.execute('SELECT * from zoo ORDER BY count')
# print(curs.fetchall())
# curs.execute('SELECT * from zoo ORDER BY count DESC')
# print(curs.fetchall())
# curs.execute('''SELECT * FROM zoo WHERE \
#                 damages = (SELECT MAX(damages) FROM zoo)''')
# curs.close()
# conn.close()
# import sqlalchemy as sa
# conn = sa.create_engine('sqlite://')
# conn.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
# ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
# conn.execute(ins, 'duck', 10, 0.0)
# conn.execute(ins, 'bear', 2, 1000.0)
# conn.execute(ins, 'weasel', 1, 2000.0)
# rows = conn.execute('SELECT * FROM zoo')
# print(rows)
# for row in rows:
#     print(row)

# The SQL Expression Language
# import sqlalchemy as sa
# conn = sa.create_engine('sqlite://')
# meta = sa.MetaData()
# zoo = sa.Table('zoo', meta,
#     sa.Column('critter', sa.String, primary_key=True),
#     sa.Column('count', sa.Integer),
#     sa.Column('damages', sa.Float)
# )
# meta.create_all(conn)
# conn.execute(zoo.insert(('bear', 2, 1000.0)))
# conn.execute(zoo.insert(('weasel', 1, 2000.0)))
# conn.execute(zoo.insert(('duck', 10, 0)))
# result = conn.execute(zoo.select())
# rows = result.fetchall()
# print(rows)

# The Object-Relational Mapper
# import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
# conn = sa.create_engine('sqlite:///zoo.db')
# Base = declarative_base()
#
#
# class Zoo(Base):
#     __tablename__ = 'zoo'
#     critter = sa.Column('critter', sa.String, primary_key=True)
#     count = sa.Column('count', sa.Integer)
#     damages = sa.Column('damages', sa.Float)
#
#     def __init__(self, critter, count, damages):
#         self.critter = critter
#         self.count = count
#         self.damages = damages
#
#     def __repr__(self):
#         return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)
#
#
# # create database and table
# Base.metadata.create_all(conn)
#
# first = Zoo('duck', 10, 0.0)
# second = Zoo('bear', 2, 1000.0)
# third = Zoo('weasel', 1, 2000.0)
# print(first)
#
# # SQL land
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=conn)
# session = Session()
#
# session.add(first)
# session.add_all([second, third])
# session.commit()
# dbm
# import dbm
# db = dbm.open('definitions', 'c')
# db['mustard'] = 'yellow'
# db['ketchup'] = 'red'
# db['pesto'] = 'green'
# print(len(db))
# print(db['pesto'])
# db.close()
# # open again
# db = dbm.open('definitions', 'r')
# print(db['mustard'])
# Memcached
# from pymemcache.client import base
# client = base.Client(('localhost', 11211))
# print(client.set('luis', 'giovanny'))
# print(client.get('luis'))
# Redis

import redis
try:
    conn = redis.StrictRedis(
        host='localhost',
        port=6379,
        password='a8ixJG21j9mtjqsQEDz8s18pjTNhKrK2E4VPCorhtzIYD8D3hzSwF6CPfoo2MrB2csO2zRVShgduhamR',
        db=0
    )
except Exception as ex:
    print(ex)
'''
keys = conn.keys('*')
print(type(keys))
conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
print(conn.get('secret'))
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
print(conn.mget(['pie', 'cordial']))
# Redis with list[]
conn.lpush('zoo', 'bear')
conn.lpush('zoo', 'alligator', 'duck')
conn.linsert('zoo', 'before', 'bear', 'beaver')
conn.linsert('zoo', 'after', 'bear', 'cassowary')
conn.lset('zoo', 2, 'marmoset')
conn.rpush('zoo', 'yak')
print(conn.lindex('zoo', 3))
conn.lrange('zoo', 0, 2)
conn.ltrim('zoo', 1, 4)
print(conn.lrange('zoo', 0, -1))
# Hashes (similar to Python dict)
conn.hset('song', 'mi', 'a note to follow re')
conn.hget('song', 'mi')
print(conn.hmget('song', 're', 'do'))
print(conn.hkeys('song'))
print(conn.hvals('song'))
print(conn.hlen('song'))
print(conn.hgetall('song'))
# set
# conn.sadd('zoo', 'duck', 'goat', 'turkey')
conn.sadd('zoo2', 'duck', 'goat', 'turkey')
print(conn.scard('zoo2'))
print(conn.smembers('zoo2'))
conn.srem('zoo2', 'turkey')
print(conn.smembers('zoo2'))
conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')
# intersection
print(conn.sinter('zoo2', 'better_zoo'))
conn.sinterstore('fowl_zoo', 'zoo2', 'better_zoo')
print(conn.smembers('fowl_zoo'))
print(conn.sunion('zoo2', 'better_zoo'))
conn.sunionstore('fabulous_zoo', 'zoo2', 'better_zoo')
print(conn.smembers('fabulous_zoo'))
conn.sdiff('zoo2', 'better_zoo')
conn.sdiffstore('zoo_sale', 'zoo2', 'better_zoo')
print(conn.smembers('zoo_sale'))
'''
# Sorted sets
import time
now = time.time()
print(now)
conn.zadd('logins', {'smeagol': now})
conn.zadd('logins', {'sauron': now+(5*60)})
conn.zadd('logins', {'bilbo': now+(2*60*60)})
print(conn.zrank('logins', 'bilbo'))
print(conn.zscore('logins', 'bilbo'))
print(conn.zrange('logins', 0, -1))
print(conn.zrange('logins', 0, -1, withscores=True))
# Bits
days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212
conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)
conn.setbit(days[1], big_spender, 1)
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)
for day in days:
    print(conn.bitcount(day))

conn.getbit(days[1], tire_kicker)
print(conn.bitop('and', 'everyday', *days))
print(conn.bitcount('everyday'))
print(conn.getbit('everyday', big_spender))
print(conn.bitop('or', 'alldays', *days))
print(conn.bitcount('alldays'))
# Caches and expiration
key = 'now you see it'
conn.set(key, 'but not for long')
conn.expire(key, 5)
print(conn.ttl(key))
conn.get(key)
time.sleep(6)
print(conn.get(key))
