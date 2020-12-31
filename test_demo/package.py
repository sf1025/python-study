#coding: utf-8
#!usr/bin/env python

#repr()函数, 它能够针对输入的任何一个对象返回字符串. 多态的代表之一
print(repr(1))
print(repr([1,2,3]))
def length(x):
    print("The length of", repr(x), "is",len(x))#返回输入对线的长度

length([1, 2, 3])
length("zhao zi long")
length({"name":"zi long", "age":2002})
#length(7222) 报错 object of type 'int' has no len()
#上述的种种多态表现, 都说明Python是一种解释型的语言, 不需要进行预编译, 只在运行时才确定状态.

#Speaking pets in Python, but without base classes;
class Cat:
    def speak(self):
        print("meow!")

class Dog:
    def speak(self):
        print("woof!")

class Bob:
    def speak(self):
        print("thank you thank you!")
    def drive(self):
        print("beep beep!")
    def bow(self):
        print("hello welcome to china")

def command(pet):
    pet.speak()

pets = [Cat(), Dog(), Bob()]
for pet in pets:
    command(pet)

#python不检查传入对对象的类型, 这种方式被称之为"隐式类型(laten typing)"或者"结构式类型(structurcal typing)", 也被俗称为"鸭子类型"
#鸭子类型就意味着可以向任何对象发送任何消息, 语言只关心该对象能否接收消息, 不强求该对象是否某一特定的类型


