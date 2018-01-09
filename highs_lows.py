import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #查询列号
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

#可视化
fig=plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
#着色
plt.fill_between(dates,lows,highs,facecolor='gray',alpha=0.6)#alpha表示透明度，0完全透明
#设置图形格式
plt.title("Daily high and low temperatures - 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制倾斜的日期标签
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=6)
plt.show()