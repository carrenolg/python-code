# Things To Do

'''
# 6.1
class Thing:
    pass


print(Thing)

# Created object
example = Thing()
print(example)


# 6.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)


# 6.3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


print(Thing3().letters)


# 6.4
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return 'Name:%s, Symbol:%s, Number:%s' % (self.__name, self.__symbol, self.__number)


# hydrogen = Element('Hydrogen', 'H', '1')
# print(hydrogen.__name)


# 6.5
_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 5}

# new_hydrogen = Element(**_dict)
# print(new_hydrogen.number)

# 6.6
# new_hydro = Element('Hydrogen', 'H', '1')
# new_hydrogen.dump()

# 6.7
# print(new_hydro)
# print(new_hydro.name)

# 6.8
element = Element(**_dict)
print(element.name)


# 6.9
class Bear:
    pass

class Rabbit:
    pass

class Octothorpe:
    pass

# 6.10
class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartPhone = SmartPhone()

    def does(self):
        return (\'''
I have many attachments:
My laser, to %s.
My claw, to %s.
My smartphone, to %s.
        \''') % (self.laser.does(), self.claw.does(), self.smartPhone.does())


robbie = Robot()
print(robbie.does())

'''
