#coding: utf-8
#!usr/bin/env python
#迭代--iterate
#循环--loop, 指的是满足条件的情况下, 重复执行同一段代码, 如while
#迭代--iterate, 指的是按照某种顺序逐个访问列表中的每一项, 比如for语句.
#递归--recursion, 指的是一个函数不断调用自身的行为, 比如, 以编程方式输出著名斐波那契数列.
#遍历--traversal, 指的是按照一定的规则访问树形结构中的每个节点, 而且每个节点都只访问一次.

#逐个访问, 访问对象中每个元素:
if __name__ == "__main__":
    lst = ["q", "w", "e", "r", "t"]
    for i in lst:
        print(i, end=',')

lst_iter = iter(lst) #对原来的lst实施了一个iter()
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())
# print(lst_iter.__next__())  报错 stopIteration 终止迭代
#iter()是内建函数, 返回一个迭代器对象--所有的迭代器对象都有一个__next__方法
print(help(iter))
#while True:
 #   print(lst_iter.__next__())#迭代完成后继续迭代会报错, StopIteration(终止迭代)

#通过上面的代码. 可以发现, 使用for循环来迭代, 当到文件末尾的时候, 就自动结束了, 不会报错.
#如果用next()或者__next__(), 当最后一个完成后, 它不会自动结束, 还要向下继续, 但是后面没有元素了,
#于是就报一个称之为StopIteration(停止迭代)的信息

#使用迭代器来操作文件
f = open("16.txt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

for line in f:
    print(line)#这里没有打印数据, 因为上面已经将指针移到最后了. 这就是迭代的特点, 要小心指针

f = open("15.txt")
for i in f:
    print(i)

#使用__next__()函数也可以读取
f = open("15.txt")
print(f.__next__())
print(f.__next__())
print(f.__next__())
#print(f.__next__())#指针到最后会报错StopIteration(循环终止)
#如果用__next__()可以直接读取文件的每行内容. 这说明文件是天然的可迭代对象, 不需要用iter()转换

#多种获取文件迭代对象元素的方法
print(list(open("15.txt")))
print(tuple(open("15.txt")))
print("$$$".join(open("15.txt")))
a,b,c = open("15.txt")
print(a, b, c)



