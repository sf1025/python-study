#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #并行迭代-计算两个列表对应元素的和
    a = [1,3,5,8,9,4,11]
    b = [3,12,45,8,1,2,10]
    c = []
    #列表长度一样
    for i in range(len(a)):
        c.append(a[i]+b[i])
    print(c)

#内置函数zip(),参数必须是序列.如果是字典, 那么键视为序列.然后将序列对应的元素一次组成元组.作为一个列表的元素
print(zip(a,b), list(zip(a,b)))
#如果序列长度不同, 那么就以"the length of the shortest argument sequence"为准
c = [1,2,3]
d = [10,20,55,44]
e = "ffrtghw"
print(list(zip(c, d)))
#参数是一个对象的时候
print(list(zip(c)), list(zip(e)))
#使用zip()实现两个列表值对象相加
f = []
for x,y in zip(c,d):
    d.append(x+y)
print(d)
#当两个列表长度不同还有一种方法解决
a = [1,10,54,30]
b = ["I", "come", "python"]
length = len(a) if len(a)<len(b) else len(b)
d = []
for i in range(length):
    d.append(str(a[i]) + ":" + b[i])
print(d)
#或者直接用zip
d =[]
for x,y in zip(a,b):
  d.append(str(x)+":"+y)
print(d)
#zip还有另外一种用法
result = [(2,11),(4,22),(6,33),(8,44)]
print(list(zip(*result)))
#字典键值反转
info = {"name":"python", "site":"google", "lang":"ccc"}
new_info = {}
for k,v in info.items():
    new_info[v] = k
print(new_info)
#用zip()实现反转
print(dict(zip(info.values(), info.keys())))#zip可以让某些循环简单

