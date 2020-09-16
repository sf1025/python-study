#coding: utf-8
#!usr/bin/env python
if __name__ == "__main__":
    f = open("15.txt")
    for line in f:
        print(line)
    for line2 in f:
        print(line2)#这里没有数据返回, 因为上面已经读取到了文件的末尾, 重复操作从末尾开始,所以没有内容
#使用过open()函数后, 就已经建立了一个文件对象, 可以使用dir()查看这个对象的方法和属性
#print(dir(f))
#创建文件
nf = open("16.txt", "w")
nf.write("1111ceshi")
nf.close()
print(nf)
#open() 默认r方式打开, 只读模式. w写方式打开, 如果文件存在, 则清空文件, 再写入新内容
#a已追加方式打开(文件指针自动移动到文件尾), 文件不存在则创建
#r+以读写方式打开, 对文件进行读写操作
#w+消除文件内容, 以读写方式打开文件
#a+以读写方式打开文件, 并将指针移动到文件尾
#b以二进制打开文件, 而不是以文本模式. 该模式只对windows或Dos有效, 类Unix的文件使用二进制进行操作的
fa = open("16.txt", "a")
fa.write("\nsss.com\n")
fa.close()
print(fa)

#使用with
#在对文件操作后, 一定要记得file.close(), 忘记了可以补上
#实现安全的关闭文件,使用with..as..可以不用close()
with open("16.txt", "a") as f:
    f.write("This is about whit ... as..\n")
with open("16.txt", "r") as r:
    print(r.read())
