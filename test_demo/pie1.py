#coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
if __name__ == '__main__':
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    # 正常显示负号
    mpl.rcParams["axes.unicode_minus"] = False
    elements = ["SCI一区", "SCI二区", "SCI三区", "SCI四区", "中文核心"]
    t1 = [1237, 2134, 3456, 2345, 1245]
    t2 = [120, 134, 456, 845, 245]
    # 颜色
    outer_colors = ["r", "b", "g", "y", "c"]
    inner_colors = ["r", "b", "g", "y", "c"]

    wedges1,texts1,autotexts1=plt.pie(t1,autopct="%3.1f%%",radius=1,pctdistance=0.85,colors=outer_colors,textprops=dict(color="w"),wedgeprops=dict(width=0.3,edgecolor="w"))
    wedges1,texts1,autotexts2=plt.pie(t2,autopct="%3.1f%%",radius=0.7,pctdistance=0.75,colors=inner_colors,textprops=dict(color="w"),wedgeprops=dict(width=0.3,edgecolor="w"))

    plt.legend(wedges1, elements, fontsize=12, title="论文级别", loc="center left", bbox_to_anchor=(0.91, 0, 0.3, 1))
    plt.setp(autotexts1, size=15)
    plt.setp(autotexts2, size=15)
    plt.setp(texts1, size=12)
    plt.title("本校及合作单位发表论文情况")
    plt.show()


