#coding: utf-8
#!usr/bin/env python

if __name__ == "__main__":
    #问题空间:
    #1. 初始状态--一开始的不完全信息或令人不满意的状况
    #2. 目标状态--你希望获得的信息或状态
    #3. 操作--为了从初始状态迈向目标状态, 你可能采取的步骤

    #对象
    #Python中的一切都是对象, 不管是字符串, 函数, 模块还是类, 都是对象. "万物皆对象"
    #对象: 一个对象有自己的状态, 行为和唯一标识: 所有相同类型的对象所具有的结构和行为在他们共同的类中被定义.
    #状态(state): 包括这个对象已有的属性(通常是类里面已经定义好的)再加对象具有的当前属性(这些属性往往是动态的)
    #标识(identity): 是指一个对象所具有的区别于所有其它对象的属性.(本质上指内存中对象的地址)

    #创建类
    class Person: #要继承其它父类的时候, 都要在后面写上  (father_class_name)
        """
        This is a sample of class
        """
        def __init__(self,name):# 初始化实例属性
            self.name = name #self是默认参数,不需要传值; name需要传值
        def get_name(self):
            return self.name

        def color(self, color):
            d = {}
            d[self.name] = color
            return d

    girl = Person("cehsi") #利用类创建实例, 初始化了name的的值即name="ceshi", girl就是一个实例, 他有属性和方法
    print(girl.name)
    name = girl.get_name()
    print(name)
    her_color = girl.color("white")
    print(her_color)













