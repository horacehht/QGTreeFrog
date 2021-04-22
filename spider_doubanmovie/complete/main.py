# 导入库部分
from movie import get_page_urls, MovieInfo
from numpy.random import uniform
import pymysql
import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}

# 连接本地数据库
conn = pymysql.connect(
    host="localhost",
    user="root",  # 要填root
    password="htht0928",  # 填上自己的密码
    database="doubanmovie",  # 数据库名
    charset="utf8"  # 字符集设为utf8
)
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

cnt = 1  # 计数器

# 获取排行榜分页
page_urls = get_page_urls()
for page_url in page_urls:
    # 每一分页都提取出每个电影的url
    wait1 = round(uniform(2, 5), 2)
    time.sleep(wait1)
    res = requests.get(page_url, headers=headers)
    html = etree.HTML(res.text)  # 转化成html文本
    movie_urls = html.xpath('//div[@class = "hd"]/a/@href')

    # 提取出每个电影的信息并存入数据库中
    for movie_url in movie_urls:
        wait2 = round(uniform(3, 6), 2)
        time.sleep(wait2)
        movie = MovieInfo(movie_url)  # 建立一个电影信息对象
        sql = """INSERT INTO MOVIEINFO(
        title, director, release_date, runtime,
        star, comments, type, summary, image, r5, r4, r3, r2, r1)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (movie.title, movie.director, movie.date, movie.runtime, movie.star,
        movie.comments, movie.type, movie.summary, movie.image,
        movie.r5, movie.r4, movie.r3, movie.r2, movie.r1)  # 要插入数据库的信息
        cursor.execute(sql, data)  # 执行sql语句
        conn.commit()  # 提交执行
        print('已获取排行榜第%d的电影' % cnt)  # 出错了也可以看到是第几部电影出的错，方便找出原因。
        # 还可以实时看到爬到第几部
        cnt += 1

print('爬虫结束!')
