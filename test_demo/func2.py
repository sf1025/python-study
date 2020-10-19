#coding: utf-8
#!usr/bin/env python
if __name__ == "__main__":
    def add(x, y):
        print("x={}".format(x))
        print("y={}".format(y))
        return x+y
    #所谓调用: 最关键的是要弄清楚如何给函数的参数赋值. 下面是按照参数的次序赋值, 根据参数的位置, 值与之对应.
    print(add(10,3))

    #也可以直接吧赋值语句写到里面, 就明确了参数和对象的关系. 参数的顺序这时候就不重要了.
    print(add(x=5, y=6))
    print(add(y=11, x=8))

    #在定义函数的时候, 参数可以被等待赋值, 也可以定义的时候就赋给一个默认的值
    def time(x, y=2):
        print("x={}".format(x))
        print("y={}".format(y))
        return x*y
    print(time(3)) #x=3, y=2
    print(time(3,4))#x=3, y=4
    print(time("qqq"))#x=qqq, y=qqq

#单个函数返回值
def fibs(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result
lst = fibs(10)
print(lst)

#多个返回值
def my_fun():
    return 1,2,3
print(my_fun())#多个返回值以元组方式返回

#对于多个返回值, 可以这样接收
x,y,z = my_fun()
print(x,y,z)

#没有return函数, 事实上返回一个none.
def foo():
    pass
print(foo())

#return的作用, 中断函数体的流程, 离开这个函数. 类似循环的break
def fun_test():
    print("I am coding")
    return 1
    print("I finished")
print(fun_test())

#函数文档说明(函数的一种属性), 使用三个引号的方式.

def my_fun1():
    """
    This is my function
    :return:doc
    """
    print("this is explain")
my_fun1()
print(my_fun1.__doc__)

#增加函数对象的属性
my_fun1.breast = 90
print(my_fun1.breast)
print(dir(my_fun1))
print(  my_fun1.__name__, my_fun1.__module__)

#形参和实参
def add(x): #x是参数, 准确说是形参
    a = 10  #a是变量
    return a+x #x就是那个形参作为变量, 其本质是要传递赋给这个函数的值
x = 3 #x是变量, 在函数外面
print(add(x)) #这里x是参数, 有前面的变量x传递对象3
#关键是要理解函数名括号里面的作用是"传对象引用".
def foo(lst):
    lst.append(99)
    return lst
x = [1,3,5]
y = foo(x)
print(y, x, id(x), id(y))



