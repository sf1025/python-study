#coding:utf-8
#!usr/bin/env python

#绑定方法和非绑定方法
class Foo:
    def bar(self):
        print("This is a normal method of class")

f = Foo()
f.bar()
#在类Foo()中, bar()本质上是一个函数, 只不过这个函数的第一个参数必须是self.
#当建立了实例后, 用实例开始调用这个方法的时候, 因为Python解释器把实例已经作为
#第一参数隐式地传给了该方法, 所以不需要显示的写出self参数了.
#要把实例显示的传给方法
Foo.bar(f)
#Foo.bar() 报错: TypeError: bar() missing 1 required positional argument: 'self'
print(Foo.bar)
print(Foo.__dict__['bar']) #进一步说明了bar是一个函数对象
#描述器
#Python中有几个特殊方法, 分别是__get__(), __Set__()和__delete__(), 有这些方法的对象叫描述器
#描述器是属性, 实例方法, 对象方法, 类方法和继承中使用的super的背后实现机制, 他在Python中使用广泛.
#上面的三个特殊方法, 可以用下面的方式来使用--所谓的描述器协议.
print(Foo.__dict__['bar'].__get__(None, Foo)) #返回结果和Foo.bar是一样的
#让self为None的意思就是没有给定的实例, 因此该方法被认为非绑定方法
print(Foo.__dict__['bar'].__get__(f, Foo))
#当通过类来获取方法的时候, 得到的是绑定犯法
#当通过实例来获取方法的时候, 得到非绑定方法

#静态方法和类方法
class Sta:
    one = 0
    def __init__(self):
        Sta.one = Sta.one+1
    @classmethod
    def get_class_attr(cls):
        return cls.one

f1 = Sta()
print("f1:"+str(Sta.one))

f2 = Sta()
print("f2:"+str(Sta.one))

print(f1.get_class_attr())
print("f1.one"+str(f1.one))
print(Sta.get_class_attr())

print("*"*10)
f1.one = 8
Sta.one = 9
print(f1.one)
print(f1.get_class_attr())
print(Sta.get_class_attr())
#所谓类方法, 就是在类里面定义的方法, 该方法由装饰器@classmethod装饰,
#其第一个参数cls所引用的是这个类对象, 即将类本身作为引用对象传入到此方法中.
T = 1
class Uoo:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def check_t():
        T =1
        return T

    def get_name(self):
        if self.check_t():
            return self.name
        else:
            return "no person"
u = Uoo("lilei")
print(u.get_name())