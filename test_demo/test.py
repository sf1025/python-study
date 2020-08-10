#/usr/bin/env python
#coding:utf-8
import requests
import math
if __name__ == '__main__':
    # print ('hello world')
    # print (id(3))
    # print (type(3.0))
    # x=6
    # print(x/2)
    # print('我是6')
    # print(123123123132123123123123123123231323232 * 1312332321231231231231322312313)
    # print(2 * 3)
    # print(10 / 2)
    # print(2e3)
#    print(2.0 ** 10000)
    #divmod()取余函数, 返回(商, 余数)
    print(divmod(5 , 2))
    #round()对浮点数进行近似取值, 保留几位小数, 简单的说就是，round(2.675, 2) 的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67，为什么？
    # 这跟浮点数的精度有关。我们知道在机器中浮点数不一定能精确表达，因为换算成一串1和0后可能是无限位数的，机器已经做出了截断处理。那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。
    # 这一点点就导致了它离2.67要更近一点点，所以保留两位小数时就近似到了2.67。
    # 如果对浮点数精度要求很高的话, 使用decimal模块
    # print(round(1.5555 , 2))
    # print(round(1.2345, 3))
    # print(math.pi)
    #列出math库中的所有方法
    # print(dir(math))
    #幂
    print(help(math.pow))
    #pow(x, y)返回x的y次方
    print(math.pow(2 , 10))
    #abs()函数返回绝对值
    # print(abs(-10))
    #基本的四则运算
    print(19 + 2 * 4 - 8 / 2)
    #type返回python对象类型
    print(type(666))
    print(type('666'))
    #字符串拼接
#     print('te' + 'st')
#     a = 55
#     print('gfgfd' + str(a))
#     print('free' + repr(a)) #repr
    #input函数是内置函数(built-in function), 在交互模式下主管键盘的函数
   # name = input("input your name:")
   #  age = input("How old are you?")
   #  print(name)
   #  print(age)
    #加转义符避免\n换行
    # print('c:\news')
    # print('c:\\news')
    #字符串前面加r, 就是原始字符串, 在里面放任何字符串都表示该字符的原始含义--
    # 这种方法在设置网站目录时非常有用
    # print(r'c:\www')
    lang = "study python"
    # print(lang[7])
    # print(lang.index("s"))
    #前包括后不包括
    # print(lang[3:8])
    #查看该对象在内存地址(就是在内存的位置编号)
    # print(id(lang))
    #字符串是一种序列, 所有序列都有如下基本操作: 这是序列的共有操作
    #求字符串序列的长度
    # print(len(lang))
    #连接两个序列
    
