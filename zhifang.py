import pandas as pd
from matplotlib import pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取电影数据
datas = pd.read_excel('MaoYanTop.xlsx')

# 按场均人次数字降序排列
sorted_movies = datas.sort_values(by='场均人次', ascending=False)

# 选择数字最大的前六位电影和对应的数量
top_movies = sorted_movies.head(6)
names = top_movies['片名']
counts = top_movies['场均人次']

# 绘制柱状图
plt.figure(figsize=(8, 4))  # 图形大小
#绘制图像，设置其x轴y轴数据，边框颜色，内部颜色
plt.bar(names, counts, facecolor='#add8e6',edgecolor='#0099ff')
#设置总标题，x轴y轴标签
plt.title('场均人次最高的六部电影')
plt.xlabel('电影')
plt.ylabel('场均人次')

# 设置x轴刻度标签的字体大小
plt.xticks(fontsize=10)
plt.show()