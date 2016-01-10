# coding:utf-8
import random
# def qiche(ren, che):
#     return 'riding
# 猫狗大战

# class 首字母一般大写
class Animal():
    # 新建对象（初始化）调用
    def __init__(self, name, blood, dps, armor):
        self.name = name
        self.blood = blood
        self.max_blood = blood
        self.dps = dps
        self.armor = armor
        # self.dodge_rate = dodge_rate
        # self.critical_strike_rate

    def attack(self, other):
        if self.blood <= 0:
            print '%s is dead' % (self.name)
            return 1
            
        print "%s attacks %s" %(self.name, other.name)

        # 闪避 20%闪避概率 dodge_rate
        # if random.random() > 0.2:
        ran = random.random()
        # if other.ran:
        #     if ran < other.rate:
        if other.name == 'cat' and ran < other.rate:
            print '%s attack %s failed.' % (self.name, other.name)
        else:
            other.blood -= self.dps - other.armor

        if other.blood <= 0:
            print '%s is dead.' % (other.name)
        else:
            other.report()

    def report(self):
        print "%s has %s blood left" % (self.name, self.blood)


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, 'dog', 100, 20, 3)


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, 'cat', 80, 30, 1)
        self.rate = 0.1


class Rat(Animal):
    # 奶妈 dps 少 具备cure回血功能
    def __init__(self):
        Animal.__init__(self, 'rat', 40, 5, 2)
        self.cure_num = 15

    def cure(self, other):
        # if other.blood + self.rcure_num >= other.max_blood:
        #     other.blood = other.max_blood
        # else:
        #     other.blood += self.cure_num
        print "%s cure %s of %d blood" % (self.name, other.name, self.cure_num)
        other.blood += self.cure_num
        if other.blood >= other.max_blood:
            other.blood = other.max_blood

        other.report()

# 还可以做暴击，闪避等功能，用random，控制概率
# random.random()>0.7 闪避和暴击实现

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

# dog1.attack(cat1)
# cat1.attack(dog1)
# rat1.attack(cat1)
# rat1.cure(dog1)
# rat1.cure(dog1)
# rat1.cure(dog1)

