import pandas as pd
import matplotlib.pyplot as plt
#设置中文显示
plt.rcParams['font.sans-serif']=['SimHei']

# 读取Excel文件
data = pd.read_excel('MaoYanTop.xlsx')

# 提取相关数据列
price = data['场均人次']

# 统计9.0分以上和9.0分以下的数量
above_9_count = price[price >= 30].count()
below_9_count = price[price < 30].count()

# 创建饼图
labels = ['30及以上', '30以下'] #设置标签
sizes = [above_9_count, below_9_count]
colors = ['#ceceff', '#d0d0d0'] #设置颜色
explode = (0.1, 0)  # 突出显示第一块

plt.title('猫眼票房榜电影平场均人次分布') #设置标题
#绘制饼图
#设置大小 标签 颜色 文本格式 阴影 起始角度
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 保持饼图为正圆形

# 显示饼图
plt.show()