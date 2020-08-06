# coding:utf8
#!/usr/bin/env python
#上面的写法是防止操作系统用户没有将python装在默认的/usr/bin/env路径里. 当系统看到这一行的时候, 首先会到env设置路径里查找
#python的安装路径, 在调用对应路径下的解释器完成操作.#!/usr/bin/env相当于写死了路径, 推荐使用#!/usr/bin/env python
import platform

if __name__ == '__main__':
    str = "I like {0} and {1}"
    #字符串中使用了{0}和{1}两个占位符, 然后字符串使用.调用了format方法
    print(str.format("movie", "music"))

    #format("movie", "music")是字符串输出方法, 第一个参数对应{0}, 第二个参数对应{1}
    str = "I like {1} and {0}"
    print(str.format("movie", "music"))

    #指定格式输出字符串
    str = "I like {0:10} and {1:>15}"
    #{0:10}表示第一个位置, 有10个字符那么长, {1:>15}表示第二个位置, 并且放在这个位置的字符是右对齐
    #{1:^15}表示居中对齐
    print(str.format("movie", "music"))

    #字符串截取输入
    str = "I like {0:.2} and {1:^10.4} ."
    #.2表示截取参数的前两位放入字符串中, ^10.4表示该位置10个字符串那么长,但放入的只有4个字符,并且居中显示
    print(str.format("movie", "music"))

#向format()中, 除了了能传入字符串, 还能传入数字(包括整数和浮点数), 而且也能有各种花样
    str = "he is {0:4d} years old and the arm is {1:5.2f}cm"
    #{0:4d}表示填充进去的是4位数字, {1:5.2f}表示填充的是5位字符的浮点数并且保留2位小数, 都是默认右对齐
    print(str.format(28, 9.555678))
    str = "he is {0:03d} years old and the arm is {1:05.2f}cm"
    #在数字前面加0的意思是参数位数不足, 则补0
    print(str.format(16, 9.2144))
    # 这种被称为"字典格式化"
    print("I like {lang} and {name}".format(lang="python", name="music"))



