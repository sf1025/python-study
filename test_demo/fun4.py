#coding:utf-8
#!usr/bin/env python

def fib(n):
    """
    This is Fibonacci Recursion
    斐波那契数列指的是这样一个数列：
    0,1,1,2,3,5,8,13,21,34,55,87,144,233,377,610,987,1579,2584,4181,6765,10944,17711,28657,46368
    0,1,2,3,4,5,6,7 ,8 ,9, 10,11,12 ,13 ,14 ,15, 16, 17,  18,  19,  20,  21,   22,   23,   24
    :param n:
    :return:
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    #递归: 在函数的定义中使用自身的方法.
    f = fib(5)
    print(f)

    #因为a0=0, a1=1是已知的, 不需要每次都判断一遍. 函数可以优化下
    memo = {0:0, 1:1}
    def fib(n):
        if not n in memo:
            memo[n] = fib(n-1)+fib(n-2)
        return memo[n]
    f = fib(10)
    print(f) #递归要慎重使用, 迭代和循环一般比递归要高. 使用递归要考虑周密, 不小心就会进入死循环

    #传递函数
    def bar():
        print(" I am in bar()")
    #foo()参数要求是一个函数, 否则函数体内的代码块无法执行func(), 因为这是一个调用函数
    def foo(func):
        func()
    foo(bar)#调用foo, 传递函数执行

    #应用
    def convert(func, seq):
        return [func(i) for i in seq]


    myseq = (111, 3.14, -9.21)
    r = convert(str, myseq)#str是实现字符串转化的函数str()的名字
    print(r)

    def num(n):
        if n%2==0:
            return n**n
        else:
            return n*n

    mysum = (3,4,5)
    r = convert(num, mysum)
    print(r)



