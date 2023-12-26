import pandas as pd
from matplotlib import pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取电影数据
datas = pd.read_excel('MaoYanTop.xlsx')

# 按票房数字降序排列
sorted_movies = datas.sort_values(by='票房', ascending=False)

# 选择数字最大的前六位电影和对应的数量
top_movies = sorted_movies.head(6)
names = top_movies['片名']
counts = top_movies['票房']

# 绘制横向柱状图
plt.figure(figsize=(10, 4.5))  # 图形大小
#绘制图像，设置其x轴y轴数据，边框颜色，内部颜色,内部线条
plt.barh(names, counts, color="#d2e9ff",edgecolor='#66b3ff',hatch="/")

#设置总标题，x轴y轴标签
plt.title('票房最高的六部电影')
plt.xlabel('票房')
plt.ylabel('电影')

plt.show()