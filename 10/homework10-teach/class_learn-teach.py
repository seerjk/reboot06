import random


class Animal():

    def __init__(self, name, blood, dps, armor):
        self.name = name
        self.blood = blood
        self.max_blood = blood
        self.dps = dps
        self.armor = armor

    def attack(self, other):
        if self.blood <= 0:
            print '%s is dead' % (self.name)
            return 1
        print '%s attack %s' % (self.name, other.name)
        ran = random.random()
        print ran
        if other.name == 'cat' and ran < other.rate:
            print '%s attack %s faild ' % (self.name, other.name)
        else:
            other.blood -= self.dps - other.armor
        if other.blood <= 0:
            print '%s is dead' % (other.name)
        else:
            other.report()

    def report(self):
        print '%s has %s blood left' % (self.name, self.blood)


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, 'dog', 100, 20, 3)


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self, 'cat', 200, 30, 1)
        self.rate = 0.1


class Rat(Animal):

    def __init__(self):
        Animal.__init__(self, 'rat', 40, 5, 2)
        self.cure_num = 15

    def cure(self, other):
        other.blood += self.cure_num
        if other.blood > other.max_blood:
            other.blood = other.max_blood
        other.report()

dog1 = Dog()
cat1 = Cat()
rat1 = Rat()


while dog1.blood > 0 and cat1.blood > 0:
    dog1.attack(cat1)
    cat1.attack(dog1)
    if dog1.blood > dog1.max_blood / 2:
        rat1.attack(cat1)
    else:
        rat1.cure(dog1)
