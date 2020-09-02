#coding: utf-8
#!usr/bin/env python
if __name__ == "__main__":
    #<集合1>中用set()简历的集合, 都可以原地修改, 或者说可变的, 也可以说unhashable-不可哈希
    #还有一种集合是无法修改的, 用frozenset(), 这种事hashable类型-可哈希
    a_set = frozenset("asdf")
    #a_set.add("qwe")#报错:forzenset object has no attribute 'add'
    #复习set()
    b_set = set("mnb")
    b_set.add("dsa")
    print(b_set)
    #集合运算
    #元素与集合的关系:只有一种关系, 元素要么属于集合, 要么不数据
    print("n" in b_set, "a" not in b_set, "a" in b_set)
    #集合与集合的关系:A是否是B的子集，或者反过来，B是否是A的超集。即A的元素也都是B的元素，但是B的 元素比A的元素数量多。
    #设定两个集合A, B, 判断A是否是B的子集, 可以使用A<B, 返回true或者false
    #还可以使用A.issubset(B)判断, 或者B.
    a = set(['q', 'w', 'r', 't', 'e'])
    b = set(['q', 'w', 'a', 'l', 'o'])
    print(a>b, b.issubset(a), a.issuperset(a))
    #A,B的并集, 即A,B的所有元素
    print(a|b, a.union(b))
    #A,B的交集, A和B公有的元素
    print(a&b, a.intersection(b))
    #A相对B的差, 即A相对B不同的元素部分
    print(a-b, a.difference(b), b-a)
    #A,B的对称差集
    print(a.symmetric_difference(b))

