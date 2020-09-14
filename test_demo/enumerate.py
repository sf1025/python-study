#coding:utf-8
#!usr/bin/env python
#内建函数enumerate()|枚举|->同时获取元素索引和元素
week = ["monday", "tuesday", "wednesday", "thursday"]
for (i, day) in enumerate(week):
    print(day +" is "+ str(i))
my_list = ["sss", 55, "qwe"]
print(list(enumerate(my_list)))
#小练习, 讲字符串的某些字符串替换为其他字符串
raw = "do you like python ? python is a good language"
#先将字符串转为列表
raw_list = raw.split(" ")
for k,v in enumerate(raw_list):
    if v == "python":
        raw_list[k] = "php"
print(raw_list)
#获取1到9每个数字平方放入列表中
power2 = []
for i in range(1,10):
    power2.append(i*i)
print(power2)
#使用列表解析--在很多情况下, 列表解析的执行效率高, 代码简洁明了. 是实际写程序中经常被用到的
squares = [x**2 for x in range(1,10)]
print(squares)

#全局命名空间, 局部命名空间
i = 1#这里的i处于全局命名空间里面
print([i for i in range(10)], i)#列表解析的i处于局部命名空间
#python3中, for循环里面的变量不再与全局命名空间的变量有关联
