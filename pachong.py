import pandas as pd
import requests
from fake_useragent import UserAgent
from lxml import etree

# 创建空的 DataFrame
df_movies = pd.DataFrame(columns=['排名', '片名', '票房', '上映时间', '平均票价', '场均人次'])

# 基础 URL
base_url = 'https://piaofang.maoyan.com/rankings/year'

# 请求头信息
headers = {
    'Cookie': '_lxsdk_cuid=18bdb48ef64c8-0497c236612b9f-26031051-e1000-18bdb48ef64'
              '3d; _lxsdk=E8F3467084F711EEBE06A598E1FFE969C92E5856750C483CA8F094870B5B85'
              '38; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1700191072; _lxsdk_s=18be6ac0fbe'
              '-4e5-acb-7dd%7C%7C2',
    'User-Agent': UserAgent().random
}

# 将base_url赋值给url变量，表示要访问的网页的URL地址。
url = base_url
#使用requests.get()方法发送一个GET请求，访问指定的URL地址
response = requests.get(url, headers=headers)
#通过response.text获取响应的内容
html = response.text

xp = etree.HTML(html)

movies = xp.xpath('//*[@id="ranks-list"]/ul[1]')
# 遍历每个电影块
for movie in movies:
    #循环296次 爬取296个电影块
    for num in range(296):
            # 提取电影信息
            ranking = movie.xpath('//*[@id="ranks-list"]/ul/li[1]/text()')[num]
            name = movie.xpath('//*[@id="ranks-list"]/ul/li[2]/p[1]/text()')[num]
            number = movie.xpath('//*[@id="ranks-list"]/ul/li[3]/text()')[num]
            time = movie.xpath('//*[@id="ranks-list"]/ul/li[2]/p[2]/text()')[num].replace(
                "上映", "")
            price = movie.xpath('//*[@id="ranks-list"]/ul/li[4]/text()')[num]
            people = movie.xpath('//*[@id="ranks-list"]/ul/li[5]/text()')[num]
            #输出所爬信息

            movie_info = {
                '排名': [ranking],
                '片名': [name],
                '票房': [number],
                '上映时间': [time],
                '平均票价': [price],
                '场均人次': [people]
            }
            df_movie = pd.DataFrame(movie_info)
            df_movies = pd.concat([df_movies, df_movie])
            print(ranking,name,number,time,price,people)

# 重置索引
df_movies.reset_index(drop=True, inplace=True)

# 保存 DataFrame 到 Excel 文件
df_movies.to_excel("MaoYanTop.xlsx", index=False)