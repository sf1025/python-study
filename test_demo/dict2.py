#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #字典的一些方法使用
    #这是用赋值的方式，实现的所谓“假装拷贝”。
    a = 5
    b = a
    print(id(a), id(b))
    ad = {"name":"aaa", "lang":"python"}
    bd = ad
    print(id(ad), id(bd))
    #python中copy方法的使用实例
    cd = ad.copy()#在内存中另辟了一个空间
    print(id(cd))
    cd["name"] = "www"
    print(ad, cd)
    #列表的特殊情况
    x = {"name":"sss", "lang":["aa", "bb", "cc"]}
    y = x.copy()
    print(id(x), id(y))
    #删除列表里面的元素aa
    y["lang"].remove("aa")
    print(y, x)#这里发现x的列表也被改变了
    #但是操作name看看
    y["name"] = "www"
    print(y, x)#发现x没有改变
    #x,y对应着两个变量, 但这个对象(字典), 但这个对象是由键值对组成的.其中一个键的值是列表
    #说明列表是同一个对象,但是字符串是不同的对象
    print(id(x["lang"]), id(y["lang"]))
    print(id(x["name"]), id(y["name"]))
    #深层次的原因, 这根python存储的数据类型特点有关,python只存储基本类型的数据,
    #比如int,str对于不是基础类型的,比如上方的列表, python不会再被复制的那个对象中
    #重新存储, 而是用引用的方式, 指向原来的值.

    #所以, 在编程语言中, 把实现上面那种拷贝的方式成为'浅拷贝'. 没有解决深层次的问题.
    #言外之意, 还有能够解决深层次问题的方法.
    #要使用深拷贝, 使用import导入copy模块
    import copy
    z = copy.deepcopy(x)
    print(id(x["lang"]), id(z["lang"]))#现在的列表不是引用方式了.
    #现在修改列表不会影响到另外一个了
    x["lang"].append("java")
    z["lang"].remove("cc")
    print(x, z)

#clear

help(dict.clear)#Remove all items from D.清除字典中的所有元素, 没有返回值
help(dict.get)#D[k] if k in D, else d.  d defaults to None.
#获取某个键的值,如果不存在键,返回none
print(x.get("lang"))
print(x.get("llll"))
#如果不能得到aaa得值就返回后面指定的值"name", 这种操作不修改原来的字典
print(x.get("aaa", "name"), x)

help(dict.setdefault)#D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
#进一步操作, 如果k不存在, 在字典值增加这个键值对, 如果只有k, 返回none并追加
print(x.setdefault("bbb", 555), x)

#items/itreitems, keys/iterkeys, values/itervalues
#注意: 在python3中做了优化, 不需要iteritems, iterkeys, itervalues
#在python3中, D.items()返回一个可迭代的对象
help(dict.items)
help(dict.keys)
help(dict.values)
#如果要实现多键值对或者键或者值的循环, 用迭代器效率高一些
print(x.items(), x.keys(), x.values())





