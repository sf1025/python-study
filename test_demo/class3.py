#coding:utf-8
#!usr/bin/env python

#self的作用
#类里面的任何方法, 第一个参数是self

class Person:
    def __init__(self, name):
        self.name = name
        print(self)
        print(type(self))

girl = Person("youzi") #说明self就是类Person的实例

print(girl)
print(type(girl)) #说明self和girl引用的实例对象是一样的
#当创建实例的时候, 实例变量作为第一个参数, 被Python解释器悄悄传给了self, 所以我们说在初始化函数的self.name就是实例的属性
#注意, 初始化函数self.name就是实例的属性

#数据流转
#将类实例化, 通过实例来执行各种方法, 应用实例的属性, 是最常见的的操作
class People:
    def __init__(self, name):
        self.user = name

    def getName(self):
        return self.user

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print("{0} is {1}".format(self.user, color))

    def how(self):
        print("{0} breast is {1}".format(self.user, self.breast))

girl = People('yifei')
girl.breast(100)
girl.color("white")
girl.how()
