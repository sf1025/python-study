#coding:utf-8
#!usr/bin/env python
if __name__ == "__main__":
    print("字典-dict")# dictionary字典
    #创建字典
    mudict = {}
    person = {"name":"aaa", "site":"reee", "lang":"gbk"}
    print(person)
    #字典可以原地修改
    person['name2'] = "www"
    print(person)
    #利用元组构建字典
    name = (["first","aa"], ["second", "bb"])
    website = dict(name)
    print(website)
    print(type(["a","b",1, (1, 2)]))
    ad = dict(name="website", age=25)
    print(ad)
    #使用fromkeys(iterable, value=None)函数 返回一个新的字典, iterable是可迭代的键, value是值
    help({}.fromkeys)
    website = {}.fromkeys(["third", "forth"], "facebook")
    print(website)
    #注意: 字典中的"键"必须是不可变的的数据类型(list, multi-list可变, int,string...不可变), "值"可以是任何类型数据
    #dd = {[1, 2]:1}#报错TypeError: unhashable type: 'list'
    #字典对象是以键值对的形式存储数据的, 所以只要知道键就能获取值. 这本质上是一种映射关系
    print(person['name'], person['lang'])
    #字典中没有索引和顺序, 也无法切片

#基本操作
#1. len(d)返回字典中的键值对数量
#2. d(key)返回字典中key的值
#3. d(key) = value赋值
#4. del(d)删除key项键值对
    print(len(person))
    print(person["name"])
    del person['name']
    print(person)
    print("name" in person)#键值对删除后返回false
    #字符串格式化输出, 可以用在html替换上面(具体使用的比较少)
    city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":11}
    print("suzhou is a beautiful city , its area code %(suzhou)s" % city_code)



