import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取Excel文件
data = pd.read_excel('MaoYanTop.xlsx')

# 提取相关数据列
price = data['平均票价']

# 统计9.0分以上和9.0分以下的数量
above_9_count = price[price >= 35.0].count()
below_9_count = price[price < 35.0].count()

# 创建饼图
labels = ['35元及以上', '35元以下']  # 设置标签
sizes = [above_9_count, below_9_count]
colors = ['#deffac', '#fff0ac']  # 设置颜色
explode = (0.1, 0)  # 突出显示第一块

# 调整图表尺寸
plt.figure(figsize=(5, 5))

# 绘制饼图
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 保持饼图为正圆形

# 调整标题和图例样式
plt.title('猫眼票房榜电影平均票价分布', fontsize=14, fontweight='bold')
plt.legend(labels, loc='upper right')

# 显示饼图
plt.show()