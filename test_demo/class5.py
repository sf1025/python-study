#coding: utf-8
#!usr/bin/env python

#继承
#实现代码重用, 实现属性和方法继承
#在python中
class NewStyle:
    pass
#print(NewStyle.__base__)
#这个类继承了object, object类是所有类的父类, Python3中的所有类都隐式的继承了object类

#单继承
#只从一个父类那里继承
class P:
    def __init__(self):
        print("I am a rich man")
    pass
class C(P):
    pass
print(C.__base__)#可以查看类C的父类
c = C()


class Person:
    def __init__(self, name):
        self.name = name

    def height(self, m):
        h = dict((["height", m],))
        return h

    def breast(self, n):
        b = dict((["breast", n],))
        return b

class Girl(Person):
    def get_name(self):
        return self.name

liyun = Girl("liyun")
print(liyun.get_name())
print(liyun.height(160))
print(liyun.breast(90))

#调用覆盖类的方法
#重写子类的方法--super
class Girl(Person):
    def __init__(self, name):
        super(Girl, self).__init__(name)
        self.real_name = "Aoi sola"

    def get_name(self):
        return self.name

lilei = Girl("hanmeimei")
print(lilei.get_name())

#多重继承--指的是一个类的父类不止一个, 而是多个
class Person():
    def eye(self):
        print("two eyes")

    def finger(self, n):
        print("ten arm is", n)

class People():
    age = 25
    def color(self):
        print("The man is yellow")

class HotMan(Person, People):
    pass

kong = HotMan()
kong.eye()
kong.finger(5)
kong.color()
print(kong.age)
#继承的特点, 将父类的方法和属性全部继承到子类中; 如果子类重写了父类的方法, 就使用子类的该方法, 父类的被遮盖






