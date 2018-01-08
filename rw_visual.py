import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk(50000)
    rw.fill_walk()

    #调整窗口尺寸
    plt.figure(figsize=(10,6))#单位英寸,80像素/英寸
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("Make another walk? y/n:")
    if keep_running=='n':
        break