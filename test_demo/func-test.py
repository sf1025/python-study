#coding:utf-8
#!usr/bin/env python
#解一元二次方程
"""
solving a quadratic equation
"""
import math

def quadratic_equation(a,b,c):
    delta = b*b - 4*a*c
    if a<=0:
        print("a不能小于等于0")
        return False
    if delta<0:
        return False
    elif delta==0:
        return -(b/2*a)
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return x1,x2
if __name__ == "__main__":
    print("a quadratic equation: x^2+2x+1 = 0")
    coefficients = (0,2,1)
    roots = quadratic_equation(*coefficients)
    if roots:
        print("the result is {}: ".format(roots))
    else:
        print("the equation has no solution.")

    #统计考试成绩
    #1. 最高分或者最低分可能有人并列
    #2. 要实现不同长度的字典作为输入值
    #3. 输出结果中, 除了平均分, 其他的都要有姓名和分数两项.
    """
    统计考试成绩
    """
    #平均分
    def average_score(scores):
        """
            统计平均分
        """
        score_values = scores.values()
        sum_scores = sum(score_values)
        average = round(sum_scores/len(score_values), 2)#保留两位小数
        return average

    def sorted_score(scores):
        """
            成绩从高到低排列
        """
        score_lst = [(scores[k], k) for k in scores]
        sort_lst = sorted(score_lst, reverse=True)
        return [(i[1], i[0]) for i in sort_lst]

    def max_score(scores):
        """
            成绩最高的分数
        """
        lst = sorted_score(scores) #引用分数排序的函数
        max_score = lst[0][1]
        return [(i[0], i[1])for i in lst if i[1]==max_score]

    def min_score(scores):
        """
            成绩最低的分数
        """
        lst = sorted_score(scores) #引用分数排序的函数
        min_score = lst[len(lst)-1][1]
        return [(i[0], i[1])for i in lst if i[1]==min_score]

    exam_scores = {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}

    ave = average_score(exam_scores)
    print("the average is:{}".format(ave))    #平均分

    sor = sorted_score(exam_scores)
    print("list of the scores:{}".format(sor))#成绩表

    max = max_score(exam_scores)
    print("xueba is:{}".format(max))          #最高分

    min = min_score(exam_scores)
    print("xuezha is:{}".format(min))         #最低分

    #找素数-找出100以内的素数
    def is_prime(n):
        """
        判断一个数是否是素数
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i ==0:
                return False
        return True
    primes = [i for i in range(2,101) if is_prime(i)]
    print(primes)

    def find_primes(n):
        primes_list = []
        for x in range(2,n+1):
            is_prime = True
            for y in range(2, int(x**0.5 + 1)): #x**0.5相当于math.sqrt(x)
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime:
                primes_list.append(x)
        print(primes_list)
    max = int(input('Find primes up to:'))
    find_primes(max)
    #1. 尽量不要使用全局变量
    #2. 如果参数是可变类型数据, 在函数内不要修改
    #3. 给个函数的功能和目标要单纯.
    #4. 函数的代码行数尽量少
    #5. 函数的独立性越强越好, 不要更其他的外部东西产生关联










