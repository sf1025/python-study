#coding:utf-8
#!usr/bin/env python
import random
i = 0
while i < 4:
    print('************************')
    num = input('请您输入0-100任意一个数:')
    #对用户输入的数据进行验证
    if not num.isdigit():
        print('请输入整数')
    elif int(num) < 0 or int(num) >= 100:
        print('请您输入0-100的整数')
    xnum = random.randint(0,9)
    x = 3-i

    if int(num) == xnum:
        print('运气真好, 您猜对了')
        break
    elif int(num) > xnum:
        print('''您猜大了!\n哈哈,正确答案是:%s\n您还有%s次机会！''' % (xnum, x))
    elif int(num) < xnum:
        print('''您猜小了!\n哈哈,正确答案是:%s\n您还有%s次机会！''' % (xnum, x))
    print('************************')
    i += 1

#break和continue
a = 8
while a:
    if a%2 == 0:
        break
    else:
        print("%d id odd number "%a)
        a = 0
#a等于8的时候, 执行循环的break, 跳出循环打印8 is even number,
#如果a等于9. 先执行else的打印语句, 然后a=0, 循环再次执行到break 输出 9 is odd number 0 is even number
print("%d is even number"%a)
#while..else类似于if...else, 走到else里面跳出了while循环
count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")
#for...else 跳出循环执行else
#上面的代码，读者不妨做注释，看看它到底在干什么。如果把 for n in range(99, 1, -1) 修 改为 for n in range(99, 81, -1) 看看是什么结果？
from math import sqrt
for n in range(99, 1, -1):
    root = sqrt(n)
    if root == int(root):
            print(n)
            break
else:
    print("nothing")
