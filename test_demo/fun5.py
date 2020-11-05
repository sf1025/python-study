#coding: utf-8
#!usr/bin/env python
def foo(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

def bar():
    print(" I am in bar()")
if __name__ == "__main__":
    f = foo(bar)
    print(f)
    f()
    #这里的foo()是装饰函数, 使用@foo来装饰bar()函数. 装饰器本身是一个函数, 将被装饰的类或者函数当做参数传递给装饰器函数.
    @foo
    def bar():
        print("I am in bar")
    bar()

    #闭包(Closure):
    a = 3
    def foo():
        print(a)
    foo()
    #在函数外面使用函数里面的变量
    def aoo():
        b = 10
        def aar():
            return b
        return aar
    f = aoo()
    print(f)
    print(f())
    #使用闭包
    def parabola(a,b,c):
        def para(x):
            return a*x**2 + b*x + c
        return para
    p = parabola(2,3,4)
    print(p(5))
    #在上面函数中. p=parabola(2,3,4)定义了一个抛物线函数对象--状2x^2+3x+4, 计算x=5时. 改抛物线函数的值, 只需要p=5即可.

    
















