import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取电影数据
datas = pd.read_excel('MaoYanTop.xlsx')

# 提取年份和月份信息
datas['year'] = datas['上映时间'].str.split('-').str[0]
datas['month'] = datas['上映时间'].str.split('-').str[1]

# 按年份统计电影数量
year = datas.groupby('year')['year'].count()

# 绘制年份的分布情况折线图
plt.figure(figsize=(7, 4))  # 显示的图形大小

#绘制折线图，list(year.index): 折线图的 x 轴数据，使用year的索引值作为 x 轴的数据。list()将其转换为列表格式。

plt.plot(list(year.index), list(year), marker='o', linestyle='-', color='#9393ff', linewidth=2)

#设置标题，x轴标签，y轴标签和字体大小
plt.title('猫眼票房榜电影年份的分布情况', fontsize=12)
plt.xlabel('年份', fontsize=10)
plt.ylabel('电影数量', fontsize=10)

plt.xticks(rotation=45)  # 旋转x轴刻度标签
plt.grid(True, linestyle='--', alpha=0.5)  # 添加网格线
plt.tight_layout()  # 调整子图之间的间距

#展示图片
plt.show()