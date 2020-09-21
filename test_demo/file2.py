#coding:utf-8
#!usr/bin/env python
import os
import time
import fileinput
if __name__ == "__main__":
    #获取文件状态
    file_stat = os.stat("16.txt")
    print(file_stat)
#使用time模块查看可读时间
print(time.localtime(file_stat.st_ctime))
#分别使用read, readline, readlines读取文件
#read():如果制定了参数size, 就按照指定长度从文件读取内容, 否则, 就读取全文.被读取的内容全部被塞在一个字符串里面.
#如果文件内容过多, 内存吃不消.文档有提醒"non-blocking"模式下的问题.
#readline:以行为单位返回字符串, 每次读取一行, 依次循环, 如果不限定size, 直到最后一个返回的是空字符串, 意味着读取到文件末尾.
f = open("you.txt")
content = f.read()
print(content)
f = open("you.txt")
print(f.readline())#每操作依次readline(), 就读取一行,并且将指针向下移动一行, 如此循环
while True:
    line = f.readline()
    if not line:    #到EOF(end of line)返回空字符串, 终止循环
        break
    print(line, end=",")
#使用readlines()读取文件, 返回一个列表, 列表的每个元素是内容是文件的一行文字.可以使用for循环
f = open("you.txt")
content = f.readlines()
print(content)
for line in content:
    print(line, end="")

#读取大文件,可以使用while循环和readline()来完成这个任务, 还可以使用fileinput模块
for line in fileinput.input("you.txt"):
    print(line, end=":")
#seek(offset [,whence])函数, 让指针移动
f = open("you.txt")
f.readline()
print(f.readline(),end=",")
print(f.readline(),end="")
f.seek(0)#回到文件开头
print(f.readline())
print(f.tell())#显示指针位置

f.seek(4)#将位置固定在第四个字符之后
print(f.readline())
f.close()
#whence的值
#默认是0, 表示从文件开头开始计算指针偏移的量, 这时offset必须是大于等于0的整数
#1时, 表示从当前位置开始计算偏移量, offset如果是负数, 表示当前位置向前移动, 正数表示向后移动
#2时, 表示相对文件末尾移动.

