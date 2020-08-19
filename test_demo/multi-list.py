#coding: utf-8
#!usr/bin/env python


#在字符串中每个元素只能是字符, 元素可以是任何类型的数据
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#在多位的情况下, 里面的list被当做一个元素对待
mult = [[1, 2, 3], 'a', 'b']

#内置函数str.split(sep,[maxsplit])--将字符串转化为lsit, 参数是分隔符
str = "cry.on.my.shoulder"
print(str.split("."))#如果不适用任何参数, 就是遇到任何分隔符符号, 就将其分割了

#str.join(list) join可以说是split的逆运算
name = ["sss", "aaa"]
print("".join(name))#不适用连接符, 一个一个紧连着
print(".".join(name))#使用.连接列表

#join()函数是字符串方法, 不是列表方法
a = [1, 2, 3, "aaa", "bbb"]
#print("+".join(a)) 会报错: TypeError: sequence item 0: expected str instance, int found


#元组, 元组是python中的一种对象类型. 它与之前的列表, 字符串, 整数, 浮点数等并列. 但, 因为他跟列表接近, 经常被忽略
s = "abc"
t = 123, 'abc', ["come", "here"]
print(t)#将对象放到了一个圆括号里面, 这个带有圆括号括起来的对象, 这是一种新的对象(或数据)类型:tuple(元组)
print(type(t))#元组中的元素类型是任意的Python对象(数据)
#元组中的元素不能修改, 跟str类似:他的元素又可以使任何类型的数据, 类似list
t = 1, "dsfd", ["abc", 111], ("qqq", 222) #元素多样性, 近list
print(t)
#'tuple' object does not support item assignment 不支持修改, 近str
#t[0] = 8
# #'tuple' object has no attribute 'append'
#t.append("no")

#元组是序列, 因此, 元组的进本操作就和列表和字符串相似
print(t[2])
print(t[2][1])
#特别提醒, 如果一个元祖只有一个元素, 应该在元素后面加一个英文半角逗号(,)
a = (3)
print(type(a)) #int
a = (3,)
print(type(a)) #tuple
if type(a)==tuple:
    print("这是元组类型")

#所有在列表中可以修改元素的方法, 在元祖中都失效,使用list()和tuple()可以实现两者转化
tls = list(t)
print(tls)
t_tuple = tuple(tls) #list-[]
print(t_tuple) #tuple-()

#元组的使用情景:
#1. 元组比列表操作速度快.如果你定义了一个值的常量集,并且唯一要做的是不断的遍历他,请使用元组代替列表
#2. 如果对不需要修改的数据进行"写保护",可以使代码更安全.使用元组而不是列表如同拥有一个隐含的assert
#语句, 说明这一数据是常量.如果必须要改变这些值,则需要执行元组到列表的转换.(使用list()函数)
#3. 元组可以再字典中被用作key,但是列表不行.字典的key必须是不可变的.元组本身是不可变的,列表式可变的.
#4. 元组可以用在字符串格式化中.

