# Chapter6 - Oh Oh: Objects and Classes

class Person():
    def __init__(self, name):
        self.name = name


soccer_player = Person('Juan Roman')
print(soccer_player)


# Inheritance
class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

    def need_a_push(self):
        print("A little help here?")
    pass


obj_car = Car()
obj_yugo = Yugo()

obj_car.exclaim()
obj_yugo.exclaim()


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name, doctor.name, lawyer.name)

obj_yugo.need_a_push()


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Daffy'
print(fowl.name)


class DDuck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('>>> inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('>>> inside the setter')
        self.hidden_name = input_name


dfowl = DDuck('Gio10')
print(dfowl.name)
dfowl.name = 'carrenolg10'
print(dfowl.name)


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius, c.diameter)
c.radius = 7
print(c.radius, c.diameter)


# Name Mangling for Privacy
class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    def get_name(self):
        print('inside the getter')
        return self.__name

    def set_name(self, input_name):
        print('inside the setter')
        self.__name = input_name

    name = property(get_name, set_name)


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)  # can't access
print(fowl._Duck__name)


# Method Types


# class method
class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A! ")

    @classmethod
    def kids(cls):
        print('A has', cls.count, 'little objects')


esay_a = A()
beezy_a = A()
whezzy_a = A()
A.kids()


# static method
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


# call method
CoyoteWeapon.commercial()

# Duty typing
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())


# Special Methods
class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


a = Word('ha')
b = Word('HA')
c = Word('eh')

print(a.__eq__(b))
print(a.__eq__(c))

print(a == b)
print(a == c)

print(c)


# Aggregation and Composition
class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a (', self.bill.description,
              ') bill and a (', self.tail.length, ') tail')


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
