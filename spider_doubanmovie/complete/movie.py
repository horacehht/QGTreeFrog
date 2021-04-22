import requests
from lxml import etree
import pymysql

def get_page_urls():
    # 获取分页
    pre = 'https://movie.douban.com/top250?'
    last = '&filter='
    starts = list(range(0, 250, 25))
    page_urls = [pre + 'start=' + str(start) + last for start in starts]
    return page_urls



# 定义MovieInfo类
class MovieInfo:

    def __init__(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        self.html = etree.HTML(res.text)
        # 通过运行函数，获取电影信息，设为实例的属性
        self.get_title()
        self.get_director()
        self.get_dates()
        self.get_runtime()
        self.get_star()
        self.get_comments()
        self.get_types()
        self.get_summary()
        self.get_ratings()
        self.get_image()

    def get_title(self):
        title = self.html.xpath('//h1//span[@property]/text()')
        self.title = str(title[0])

    def get_director(self):
        director = self.html.xpath('//span/a[@rel = "v:directedBy"]/text()')
        self.director = str(director[0])  # 导演

    def get_dates(self):
        movie_dates = self.html.xpath('//span[@property = "v:initialReleaseDate"]/text()')
        dates = ''
        for movie_date in movie_dates:
            dates = dates + movie_date + '/'
        dates = dates.rstrip('/')  # 去掉最右方的/
        self.date = str(dates)

    def get_runtime(self):
        movie_times = self.html.xpath('//span[@property = "v:runtime"]/text()')
        runtimes = ''
        for movie_time in movie_times:
            runtimes = runtimes + movie_time + '/'
        runtimes = runtimes.rstrip('/')
        self.runtime = str(runtimes)  # 放映时长

    def get_star(self):
        star = self.html.xpath('//strong/text()')
        self.star = str(star[0])  # 豆瓣评分

    def get_comments(self):
        comments = self.html.xpath('//div/a[@href = "comments" and @class="rating_people"]/span/text()')
        self.comments = str(comments[0])  # 评价人数

    def get_types(self):
        movie_types = self.html.xpath('//span[@property = "v:genre"]/text()')
        types = ''
        for movie_type in movie_types:
            types = types + movie_type + '/'
        types = types.rstrip('/')  # 去掉最右方的/
        self.type = str(types)  # 电影类型

    def get_summary(self):
        summary = self.html.xpath('//div//span[@property = "v:summary"]/text()')
        content = ''
        for i in summary:
            content = content + i.strip()
        self.summary = str(content)  # 剧情简介

    def get_ratings(self):
        ratings = self.html.xpath('//div[@class = "ratings-on-weight"]/div/span[@class = "rating_per"]/text()')
        self.r5, self.r4, self.r3, self.r2, self.r1 = ratings

    def get_image(self):
        image = self.html.xpath('//img[@title = "点击看更多海报"]/@src')
        image_url = image[0].replace('jpg', 'webp')  # jpg图片不允许访问，换成webp可以
        self.image = str(image_url)