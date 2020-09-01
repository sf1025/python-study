#coding: utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #元组算是列表和字符串的某些特征的杂合, 集合堪称列表和字典的某些特征杂合
    s1 = set("qweqewq")
    print(s1)#集合中的元素不能重复, 在创建集合的时候, 有重复元素会过滤掉
    s2 = set([123, "python", "baiud", "face", "google"])
    print(s2)
    #查看set的方法没有发现set, 说明集合没有索引, 没有顺序
    print(dir(set))
    #s2[1]#报错:  'set' object does not support indexing
    #特别说明{}在字典和集合中都用, 但是简历空集合必须用到set
    a1 = {"qq", "dd"}
    a1.add("ss")
    print(a1)
    b_set = set('dsadsa')
    print(b_set)
    b_set.add("ssss")
    print(b_set)
    #b_set.add([1,2,3])#集合添加列表会报错,TypeError: unhashable type: 'list'
    #others是指作为参数的不可变对象, 将他和原来的集合组成新的集合, 用新集合代替旧集合
    help(set.update)#Update a set with the union of itself and others.
    b_set.update("qwrego")
    print(b_set)
    b_set.update((2,3), "bmm", "789")
    print(b_set)
    #set.pop(): 从set中随机删除任意元素, 并返回被删除的值, 不能指定删除元素, 空集合会报错
    print(b_set.pop(), b_set)
    #set.remove(obj):指定删除set中的元素, 否则报错
    print(b_set.remove("d"), b_set)
    #set.discard(obj):obj如果是集合中的元素就删除, 否则无操作
    print(b_set.discard("g"),"666", b_set)
    #set.clear():删除集合的所有元素, remove all elements from this set
    print(b_set.clear(), b_set)


