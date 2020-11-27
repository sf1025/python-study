#coding: utf-8
#!usr/bin/env python

class A:
    x = 7

print(A.x)
A.y = 9 #对类新增一个属性
print(A.y)
del A.x
#print(A.x) #AttributeError: type object 'A' has no attribute 'x'

#创建实例
class person:
    """
    This is a sample class
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def color(self, color):
        d = {}
        d[self.name] = color
        return d

    #创建实例, 就是调用类. 当类被调用后:
    #1. 创建实例对象.
    #2. 检查是否有____专业的说法: 是否实现__()方法. 如果没有, 则返回实例对象.
    #3. 如果有__init__(),则调用该方法并且将实例对象作为第一个参数self传进去
    #__init()__作为一个特殊方法, 是比较特殊的, 在它里面, 一般是规定一些属性或者
    #做一些初始化让类具有一些特征, 但是, 他没有语句.

    #__init__()初始化函数, 除了第一个参数必须是self, 不能有return语句之外, 其他方面和普通函数一样.
    #设置参数和里面的属性
class Room:
    def __init__(self, name, lang="golang", website="www.google.com"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "dsads@gmail.com"



