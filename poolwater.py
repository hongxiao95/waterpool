#coding=utf-8
import copy
from random import randint
import matplotlib.pyplot as plt
    
def main():
    #模拟天数为100
    days_total = 100
    #总水滴量为100万
    water_total = 1000000
    #日换水率
    day_change_rate = 0.1

    #第0天开始时的水池状态
    pool = [0 for i in range(water_total)]
    day_change_amount = int(day_change_rate * water_total)

    #记录每一天开始时水量比例的数组 water_history[x][y] 表示第x天开始时，水池中第y天的水所占水滴数
    water_history = [[0 for i in range(days_total)] for j in range(days_total)]

    #初始化第0天开始时的水滴比例
    water_history[0][0] = water_total

    for day in range(days_total - 1):
        #拷贝前一天开始时的初始数据作为基础
        water_history[day + 1] = copy.copy(water_history[day])
        print("计算第%d天的换水" % (day,))
        for _ in range(day_change_amount):
            #此次要换水的单元
            change_pos = randint(0, water_total - 1)
            #换水记录中，该单元所属天数的水 - 1, 当天的水量 + 1
            water_history[day + 1][pool[change_pos]] -= 1
            water_history[day + 1][day + 1] += 1
            #换水
            pool[change_pos] = day + 1

    #验证计算后每天总水量是否正确
    verify = True
    day_water_total = [sum(line) for line in water_history]
    for day in range(days_total):
        if(day_water_total[day] != water_total):
            verify = False
            break
    if(not verify):
        print("水量计算出错")
    else:
        print("水量计算成功")

    #水量归一化
    for i in range(days_total):
        for j in range(days_total):
            water_history[i][j] /= water_total

    print(water_history)

    days_limit = [i for i in range(days_total)]

    #准备绘制
    figure = plt.figure()
    main_ax = figure.add_subplot(111)
    main_ax.set(title="水量演变图", xlim=[0,100], ylim=[0,0.15], xlabel="天数", ylabel="水量百分比")
    for day in range(1, days_total):
        main_ax.plot(days_limit[day:], [item[day] for item in water_history[day:]], color="red", marker=".")
    plt.show()


if __name__ == "__main__":
    main()








