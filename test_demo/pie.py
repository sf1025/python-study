#coding:utf-8
#声明编码格式为utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
if __name__ == '__main__':
    squares = [1, 4, 9, 15, 25]
    plt.plot(squares)
# 保存图片
    plt.savefig('./test')
    plt.show()
# 指定字体为SimHei, 用于显示中文, 如果Ariel, 中文会乱码
    mpl.rcParams["font.sans-serif"] = ["simHei"]
# 用来正常显示负号
    mpl.rcParams["axes.unicode_minus"] = False
# 定义饼图的各组分项目名称, 颜色代码, 具体数值
    g = ["SCI一区", "SCI二区", "SCI三区", "SCI四区", "中文核心"]
    c = ["r", "b", "g", "y", "c"]
    t = [1237, 2134, 3456, 2345, 1245]
# 修改为分列式饼图
    explode = (0.1, 0.1, 0.1, 0.1, 0.1)#(0.1, 0, 0, 0, 0)
# autopct="%3.1f%%" 代表三位数, 其中一位是小数位
    plt.pie(t, explode=explode, labels=g, autopct="%3.1f%%", startangle=60, colors=c)
    plt.title("图1 近三年来发表论文的统计")
# plt.savefig('./test1')
    plt.show()
