#coding: utf-8
#!usr/bin/env python

#zip()补充
if __name__ == "__main__":
    color = ["red", "green", "blue"]
    values = [12, 54, 22, 66]
    for col, val in zip(color, values):
        print((col, val)) #zip自动匹配, 会抛弃不对应的项
    #参数*iterables
    docs = [(1, 2), (3, 4,), (5, 6)]
    x, y = zip(*docs)
    print(x, y)
    #利用这个功能实现矩阵的专置
    m = [[1, 2], [3, 4], [5, 6]]
    print(list(zip(*m)))
    seq = range(1, 10)
    print(list(zip(*[iter(seq)]*3)))
    #网络示例
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]
    lst_a = map(lambda pair: max(pair), zip(a, b))
    print(list(lst_a))
    #命名空间
    #全局变量和局部变量
    x = 2
    def func_x():
        x = 9
        print("this x is in the func_x:-->", x)
    func_x()
    print("----------")
    print("this x is out of func_x:-->", x)
    #global
    y = 2
    def func_y():
        global y
        y = 10
        print("this y is in the func_y:-->", y)
    func_y()
    print("----------")
    print("this y is out of func_y:-->", y)

    #作用域

