from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
import pandas as pd

# 从 Excel 文件中读取数据
df = pd.read_excel('MaoYanTop.xlsx')
df['上映时间'] = pd.to_datetime(df['上映时间'])
years = df['上映时间'].dt.year.unique()
grouped = df.groupby(df['上映时间'].dt.year)
sorted_data = grouped.apply(lambda x: x.nlargest(10, '票房')).reset_index(drop=True)
years = sorted_data['上映时间'].dt.year.tolist()
box_office = sorted_data['票房'].tolist()
movies = sorted_data['片名'].tolist()

timeline = Timeline()
for year in years:
    year_data = df[df['上映时间'].dt.year == year]
    movies = year_data['片名'].tolist()
    box_office = year_data['票房'].tolist()

    bar = Bar()
    bar.add_xaxis(movies)
    bar.add_yaxis("票房", box_office)
    bar.set_global_opts(title_opts=opts.TitleOpts(title=f"{year}年上映电影票房"))

    timeline.add(bar, f"{year}年")

timeline.render("chart.html")