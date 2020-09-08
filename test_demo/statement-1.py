#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    print(help(print))
    for i in [1,2,3,4,5]:
        print(i)
    for i in [1,2,3,4,5]:
        print(i, end=',')
#import的几种用法
#引入math模块
#这是最常用法, 并且不同模块的同名函数不会冲突
import math
print(math.pow(3, 2))
#这种适合引入模块少的时候用, 引入模块过多, 可读性下降
from math import pow
print(pow(4,2))
#引入多个函数可以这样:
from math import pow, e, pi
print(pow(e, pi), e, pi)

#赋值语句, 如a=3, 就是将一个整形赋值给了一个变量, 还可以使用多重赋值
x, y, z = "123", 756, ["ds", "hgh"]
print(type(x), x)
print(type(y), y)
print(z)
#将几个值赋值给同一个变量
a = "python", "study"#是将变量放到一个元祖, 然后把元组赋值给变量
print(a)
#实现数值对调
a = 2
b = 9
a,b = b,a
print(a,b)#变量相当于贴在对象上面的标签, 这个操作将标签换了位置, 分别指向了不同的对象
#链式赋值
m = n = "I use python"
print(m,n)
#判断两个变量所指向的值是不是一个
print(m is n)

