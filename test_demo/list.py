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
    #max()和min()--按照元素的字典顺序进行比较返回列表的最大最小值
    print(max(lst),min(alist))

    #向列表中追加字符串"like", append()向列表后面追加值
    lst.append("like")
    print(lst)
    lst.append(100)
    print(lst)
    #append方法等效于a[len(a:)]=[x]
    lst[len(lst):]=[3]    #len(lst)即获取lst的长度
    print(lst)
    lst[6:]=["sssss",222,333]
    print(lst)

    #list.extend(L)函数, 将L所有元素加入到list后面
    la=[1, 2, 3]
    lb=["qqq", "www", "eee"]
    la.extend(lb)
    print(la)
    #如果list.extend(str)的时候, 字符串被以字符为单位拆开, 追加到list里面
    b="abc"
    la.extend(b)
    print(la)
    #如果extend的对象是数值类型, 则报错
    # la.extend(555)
    #list.extend(L) 等效于 list[len(list):] = L ，L是待并入的列表。
    la[len(la):]="demo"
    print(la)
    # iterable--可迭代的  iterator--迭代器
    #用内建函数hasattr()判断一个字符串是否是可迭代的
    atr = "python"
    print(hasattr(atr, '__iter__'))
    clst = [1, 2]
    print(hasattr(clst, '__iter__'))
    print(hasattr(3, '__iter__'))
    #列表的重要特性: 列表是可以修改的.这种修改, 不是复制一个新的, 而是在原地进行修改.
    #原地修改没有返回值, 无法赋值给某个变量
    #append是整建制的追加, extend是个体化扩编
    clst.append([1, 5, 6])
    print(clst, len(clst))
    clst.extend([4, 5, 6])
    print(clst, len(clst))

    #count函数: 获取列表中重复元素出现的次数
    print(clst.count(1))
    #没有重复返回0
    print(clst.count(3))
    #index函数: 获取列表中元素的索引
    print(clst.index(5))
    #不能存在会报错
    # print(clst.index(3))

    #list.insert(i, x)函数: 第一个参数是函数的插入列表位置(索引)--插入索引i的前面位置, 第二个是需要插入的元素
    dlst=["www", "ccc", "ddd"]
    dlst.insert(1, 666)
    print(dlst)
    #a.append(x)等效于a.insert(len(dlst), x), 如果第一个参数超过了最大索引值, 都是自动追加在末尾
    #dlst.insert(len(dlst), 777)
    dlst.append(777)
    print(dlst)

    #list.remove(x)和list.pop([i])--删除元素的两种方法
    #仔细观察, 变量的名字是lst而不是list, 最好不要用list作为变量名字, 因为他是Python中内置的对象类型的名字.
    dlst.remove("ccc")  #直接删除列表中的元素, 原地删除没有返回值, 元素不存在会报错
    if "ddd" in dlst:
        dlst.remove("ddd")
        print(dlst)
    else:
        print("ddd is not in dlst")
    #.pop([i])函数-[i]参数可选, 如果不写, 默认删除最后一个, 并将删除的元素作为结果返回
    print(dlst.pop(2))
    print(dlst)
    print(dlst.index(666))
    #简单总结: 1.list.remove(x)中的参数是列表中元素, 且对列表原地修改, 无返回值
    #2. list.pop([i])中的i是列表中元素的索引值, 可选.为空则删除列表最后一个,否则删除
    #索引为i的元素, 并将元素作为返回值

    #a.reverse()函数--该函数没有返回值
    dlst.reverse()
    print(dlst)


#总结列表和字符串:
# 不管是组成列表的元素, 还是组成字符串的字符,都可以用从左到右, 一次用0,1,2,3,....这样的方式
#建立索引. 而要得到一个或多个元素, 可以使用切片

#区别:
#列表和字符串的区别是: 列表式可以改变的, 字符串是不可变的. 这个怎么理解呢? 首先看对列表的这些操作,
#其根源在于列表可以进行修改, 即列表是可变的.

