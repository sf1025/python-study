#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #参数收集
    #参数个数不确定的时候
    def func(x, *arg):
        print(x)
        result = x
        print(arg)
        for i in arg:
            result += i
        print(result)
    #如果输入的参数不确定, 其它参数全部通过*arg以元组的形式有arg收集起来.
    func(1,2,3,4,5,6,7,8,9)

    #进一步看出*agrs(名称可以不同, *号必填)
    def foo(*args):
        print(args)
    foo(1,2,3)
    foo("sss", "fff", 123)
    foo("python")#只有一个值, 也会收进元组中, 在元组中, 只有一个元素, 后面需要有一个逗号
    #不给*args传值也是可以的
    def foo(x, *args):
        print("x:"+str(x))
        print("tuple:"+str(args))
    foo(7)

    #如果用**kargs的形式收集值, 会得到dict类型的数据, 需要在传值的时候说明"键"和"值"
    def foo(**kargs):
        print(kargs)
    foo(a=1,b=2,c=3)#注意赋值方式和打印结果
    def foo(x,y,z,*args,**kargs):
        print(x)
        print(y)
        print(z)
        print(args)
        print(kargs)
    foo("aaa", 2, "dsads")
    foo(1,2,3,4,5,6)
    foo(1,2,3,4,5,b=6)