#coding: utf-8
#!usr/bin/env python
import math
if __name__ == "__main__":
    #斐波那契数列数学表达式:
    #a[0] = 0                   n=0
    #a[1] = 1                   n=1
    #a[n] = a[n-1] + a[n-2]     n>=2
    #使用for循环递归实现
    a,b = 0, 1
    for i in range(5):
        a, b = b, a+b
    print(a, b)

    #dir()
    #可以使用dir()内置函数检查模块(以及其他对象)的内容
    #它返回传递给他的任何对象的属性名称经过排序的列表. 如果不指定对象, 则返回当前作用域的名称.
    print(dir())
    import keyword
    print(dir(keyword))
    print(dir(__builtins__))#查看内建函数
    #dir()函数适用于所有对象类型, 包括字符串,整数,列表,元组,字典,函数,定制类,类实例和类方法
    print("字符串:", dir("you"))#应用于字符串时返回的属性
    print("列表:", dir([]))
    print("整数:", dir(666))
    print("元组:", dir(()))
    print("字典:", dir({}))
    print("函数:", dir(dir))

    #文档字符串:在dir()里面打印出来的属性__doc__. 这个属性是一个字符串, 它包含了描述对象的注释. Python称之为文档字符串或docstring
    print(str.__doc__)

    #并非所有对象都有名称, 但那些有名称的对象都将名称储存在__name__属性中. 注:名称是从对象而不是引用该对象的变量中派生的
    print(dir())
    director = dir#新变量
    print(director())
    print(dir.__name__, director.__name__, __name__)
    #模块拥有名称, Python解释器本身被认为是顶级模块或主模块. 当以交互的方式运行python时, 局部__name__变量被赋予'__main__'.
    #同样的, 当从命令行执行python模块, 而不是将其导入另一个模块时, __name__属性被赋予值'__main__', 而不是该模块的实际名称.
    #这样, 模块可以查看自身的__name__值来自行确定自己正被如何使用, 是作为另一个程序的支持, 还是作为命令行执行的主命令程序.
    #因此, 下面这条惯用的Python语句在模块中是很常见的:
    if __name__ == '__main__':
        #
        print(1)
    else:
        #
        print(2)

    #type()函数确定对象是字符串还是整数, 或者是其他类型对象
    import types
    print(types.__doc__)
    print(dir(types))

    #标识: 每个对象都有标识, 类和值. 可能有多个变量引用同一对象, 同样的, 变量可以引用看起来相似(有相同的类型和值),
    #但拥有截然不同标识的多个对象.当变量改变时(比如向列表中增加元素), 这种关于变量的标识的概念就很重要, 如在下面的示例中,
    #blist和clist引用同一个列表对象. 示例中, id()函数给任何给定对象返回唯一的标识符.
    print(id.__doc__)
    alist = [1,2,3]
    blist = [1,2,3]
    clist = blist
    print(id(alist), id(blist), id(clist))
    print(alist is blist, blist is clist)
    clist.append(4)
    print(blist, clist)

    #属性: 对象拥有属性, 并且dir()函数会返回这些属性的列表. 测试一个或多个属性是否存在.
    #可以使用hasattr()和getattr()
    print(hasattr.__doc__)
    print(getattr.__doc__)
    print(hasattr(id, '__doc__'))
    print(getattr(id, '__doc__'))



