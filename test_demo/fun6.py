#coding:utf-8
#!usr/bin/env python
from functools import reduce
#几个特殊函数
if __name__ == "__main__":
    #lambda函数: 是一个只用一行就能解决问题的函数
    def add(x):
        x += 3
        return x
    numbers = range(10)
    print(numbers)
    new_numbers = []
    for i in numbers:
        new_numbers.append(add(i))
    print(new_numbers)
    #在这个例子中, add()只是一个中间操作. 可以简写为
    new_numbers = [i+2 for i in numbers ]
    print(new_numbers)

    #使用lambda函数代替
    lam = lambda x:x+3#这里的lam相当于上面的add(), 这一行就完成了add(x)函数体里面的两行
    n2 = []
    for i in numbers:
        n2.append(lam(i))
    print(n2)

    #lambda的例子
    g = lambda x, y : x + y
    print(g(3,4))
    print((lambda x:x**2)(4))#返回4的平方
    #总结lambde的使用方法
    #1. 在lambda后面直接跟变量
    #2. 变量后面冒号
    #3. 冒号后面表达式, 表达式结果就是函数的返回值
    #4. lambda包含的表达式不能超过一个, 不能包含命令.
    # lambda agr1, agr2, ...argn : expression use arguments
    #打印一个列表, 里面依次是某个数字的一次方, 二次方, 三次方, 四次方
    lamb = [lambda x:x, lambda x:x**2, lambda x:x**3, lambda x:x**4]
    for i in lamb:
        print(i(3), end=",")

    #map函数:
    #1. 对可迭代对象的每个元素, 依次应用function的方法
    #2. 将所有结果返回一个列表(python2.x)|迭代器(python3.x)
    #3. 如果参数很多, 则对那些参数并执行function
    arr = [0,1,2,3,4,5,6,7,8,9]
    print(map(add, arr))
    lst1 = [1,2,3,4,5]
    lst2 = [6,7,8,9,0]
    lst3 = [7,8,9,1,2]
    m = map(lambda x,y,z:x+y+z, lst1, lst2, lst3)
    lst4 = list(map(lambda x,y,z:x+y+z, lst1, lst2, lst3))
    print(m, lst4)

    #reduce
    r = reduce(lambda x,y:x+y, [1,2,3,4,5])
    print(r)
    #map函数是多个列表元素上下运算, reduce是一个列表元素横向运算

    #filter(过滤器):
    number = range(-5,5)#range在python2中返回列表, 在python3中返回迭代器
    f = filter(lambda x:x>0, number)
    print(list(number), list(f))
    print([x for x in number if x>0])




