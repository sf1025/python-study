#coding:utf-8
#!usr/bin/env python
import random
if __name__ == "__main__":
    #将列表[1,2,3,4,5,7,8,9,0]变成[2,3,4,5,6,7,8,9,0,1]
    #将第一位元素取出, 然后追加到最后
    lst = [1,2,3,4,5,6,7,8,9,0]
    print(lst)
    a = lst.pop(0)
    lst.append(a)
    print(lst)

    #1.产生一个列表, 其中有40个元素, 每个元素是0到100的一个随机整数
    #2.如果这个列表的元素代表每个班级40人的分数, 计算成绩低于平均分的人数, 并输出
    #3.对上面的列表元素从大到小排列
    score = [random.randint(0,100) for i in range(40)]#0到100之间, 随机得到40个整数, 组成列表
    print(score)
    num = len(score)
    sum_score = sum(score)#求和
    ave_num = sum_score/num#计算平均数
    less_ave = len([i for i in score if i<ave_num])#将小于平均数的找出来, 组成列表, 并获取列表数量
    print("平均数是: {:.1f}".format(ave_num))#保留一位小数
    print("There are {} students less than average".format(less_ave))

#练习去将字符串中的多个空格合并成一个:
string = "I  study  python"
print(string)
str_lst = string.split(" ")#按照空格分割字符串为列表
print(str_lst)
new_lst = [s for s in str_lst if s!=""]#利用列表解析, 将空格验出
print(new_lst)
new_str = " ".join(new_lst)#用单个空格连接列表元素
print(new_str)













