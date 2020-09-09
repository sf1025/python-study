#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #三元操作符
    name = "ceshi" if "" else "python"
    print(name)
    #总结: A = Y if X else Z
    #如果x为真 执行 A = Y  如果X为假 执行 A = Z
    x = 2
    y = 8
    a = "python" if x<y else "php"#true python
    b = "python" if x>y else "php"#false php
    print(a, b)
#for循环应用-列表
ls_line = ["hello", "world", "welcome", "come"]
for word in ls_line:
    print(word)
for i in range(len(ls_line)):#range(4)返回的是(0,4)对应列表元素的索引
    print(ls_line[i])

#字典, 元组
d = dict([("website", "www.baidu.com"), ("lang", "python"), ("author", "aaa")])
print(d)
for k in d:#注意到，上面的循环，其实是读取了字典的key。在字典中，有一个方法， dict.keys() ，得 到的是字典key列表。
    print(k)
for k in d.keys():#这种方法和上面一样, 但是执行速度欠佳, 不建议使用
    print(k)
#获取字典的key和value
for k,v in d.items():#python中国d.items()做了速度优化
    print(k+"-->"+v)
#注意: for循环不能对int进行循环, int对象是不可迭代的
#判断对象是否是可迭代的:
import collections
print(isinstance(123, collections.Iterable))#返回false
#字符串-str, 列表-list, 字典-dice, 元组-tuple, 集合-set都是和迭代的

#range(start, stop[, step])的含义:
#1.这个函数可以创建一个数字元素组成的列表
#2.最常用月for循环
#3.函数的参数(start)必须是整数, 从0开始, 返回值是类似[start, strar+step,start+step*2...]
#4.step默认是1
#5.如果step是正数, 返回列表的最后值不包括   stop值, 即start+isstep这个值小于stop;如果step
#是负数, start+isstep的值大于stop
#6.step不能等于0, 等于0报错
print(range(9))
print(list(range(0,9)))
print(range(0,9,2), list(range(0,9,2)))#step=2, 每个元素等于start+i*step
#如果想返回[0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
print(list(range(0, -9, -1)))
#获取100以内的偶数
print(list(range(0,100,2)))
#获取列表所有序号组成的列表
lst = ["I","am","list","I","am","python","hello","world"]
py_index = range(len(lst))
print(list(py_index))
#找出100以内能被3整除的正整数列表
int_lst = []
for n in range(1,100):
    if n%3 == 0:
        int_lst.append(n)
print(int_lst)
#或者直接利用range函数的step参数
print(list(range(3,100,3)))
#for循环在python中应用广泛, 内涵深刻




