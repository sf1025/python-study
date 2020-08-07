#coding: utf-8
#!uer/bin/env python
if __name__ == "__main__":
    #在Python中用方括号表示一个列表, 在方括号里面可以是整数, 浮点数, 也可以是字符串,
    #还可以是True/False这种布尔值
    print(type([]))
    print(bool([]))
    #列表里面的元素在硬件设备理想是情况下可以无限大
    a = [2, 3, "dsads.github.com"]
    print(type(a))
    print(bool(a))
    print(type(a[0]))
    #可以对列表里面的元素做二次切片
    print(a[2][6:12])

    #从右边开始切片,-1开始, 注意一定要左边的数字小于右边的数字, 否则返回空
    lang = "python"
    print(a[-1])
    print(lang[-1:-3])
    print(type(lang[-1:-3]))
    print(a[-3:-1])
    print(lang[-4:-1])

    #反转--反转会生成一个新的值, 不会影响原来的对象
    alist = [1, 2, 3, 4, 5]
    print(alist[::-1])
    print(lang[::-1])

    #列表反转的方法-reversed-返回一个可以迭代的对象, 返回的是原来序列的反转对象
    #print(help(reversed))
    print(list(reversed(alist)))
    print(list(reversed("abcdefg")))

#序列的基本操作
lst = ["python", "php", "c++"]
print(len(lst))
#+--连接两个序列
print(alist+lst+lst)
#*--重复元素
print(lst*3)
#in 判断元素是否在序列中
print("python" in lst)
print("www" in lst)
#max()和min()--按照元素的字典顺序进行比较
print(max(lst),min(alist))
