import openpyxl
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np

# 加载XLSX文件
workbook = openpyxl.load_workbook('MaoYanTop.xlsx')
sheet = workbook.active

# 从特定列（例如列A）读取评论
comments = [cell.value for cell in sheet['B']]

# 将评论连接成单个字符串
text = ' '.join(comments)

# 读取形状图片
shape_image = np.array(Image.open('beijing.jpg'))

# 创建词云对象，并设置形状图片作为词云形状
wc = WordCloud(background_color='white', mask=shape_image, contour_color='#ffff00', contour_width=2,font_path='msyh.ttc')

# 生成词云
wc.generate_from_text(text)

# 根据形状图片着色
image_colors = ImageColorGenerator(shape_image)
wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('word.jpg', dpi=800)