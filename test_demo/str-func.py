#!user/bin/env python
#coding: utf-8
if __name__ == "__main__":
    # help(str.isalpha)
    # isalpha函数字符串全是字母返回true, 否则返回false
    print("python".isalpha())
    print("1python".isalpha())

#根据字符分割字符串split(), 返回值是列表类型
print("I love python".split(" "))

#去除字符串两头空格, 特别注意,原来的值没有变化, 而是返回了一个新的结果
#lstrip--去除左边空格, rstrip--去除右边空格
b = " help "
print(b.strip())
print(b)

#字符大小写转换
#s.upper()-s中的字母大写
#s.lower()-s中的字母小写
#s.capitalize()-s中的首字母大写
#s.isupper()-s中的字母是否全是大写
#s.islower()-s中的字母是否全是小写
#s.istitle()-s中的字符串中多有的单词首字母是否都是大写, 且其他字母为小写(标题格式)

#用.join()拼接字符串
b = "www.abc.com"
c = b.split('.')
print(c)
print(".".join(c))
print("*".join(c))

#内建函数-ord() | chr() 实现字符和对应数字之间的转换
print(help(ord))
print(chr(81))

#str.encode()--字符串编码
help(str.encode)


