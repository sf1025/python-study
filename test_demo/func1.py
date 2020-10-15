#coding: utf-8
#!usr/bin/env python
def multip_function(a, b):
    c = a*b
    return c
#定义函数的格式:
#def 函数名(参数1, 参数2, ...,参数n)
#     函数体(语句块)

#说明:
#1. 函数名的命名规则. 一般用小写字母和单下划线, 数字等组合
#2. def是定义函数的关键字(define)
#3. 函数名后面的括号里面, 可以有参数列表, 也可以没有参数
#4. 括号后面的冒号必须记得
#5. 函数体(语句块), 相对于def缩进, 锁近四个空格
if __name__ == "__main__":
    result = multip_function(4,6)
    print(result)

def name():
    print("xiaoke")
name()

#python不需要严格定义变量的类型
def add(a,b):
    return a+b
print(add(10,11))
print(add('dsa','weq'))
#print(add(10,"sad")) TypeError: unsupported operand type(s) for +: 'int' and 'str'
#从上面实验结果发现: a+b的意义完全取决于对象的类型. 在Python中, 将这种依赖关系, 称之为多态.

#可以将函数通过赋值语句, 将变量与函数建立关系
result = add
print(add, result, type(add)) #查看函数在内存汇总的存储信息
#这说明add是一个对象, 因为只有对象才有类型, 并且他是一个function类. 按照经验, 对象都可以和一个变量建立引用关系, 从而通过那个变量访问对象.


