import os
import requests
from utils import log
from utils import user_agent
from urlparser.parser import movies_from_url


def download_image(url, name):
    folder = "img"
    movie_name = name.split(' ')[0]
    path = os.path.join(folder, movie_name)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if os.path.exists(path):
        return

    useragent = user_agent()

    headers = {
        'user-agent': useragent,
    }
    # 发送网络请求, 把结果写入到文件夹中
    r = requests.get(url, headers)
    with open(path, 'wb') as f:
        f.write(r.content)


def main():
    print('启动spider')
    log('启动spider')
    # 豆瓣top250电影页面一共10页，每页25条电影数据，所以for循环需要按照如下规则
    for i in range(0, 250, 25):
        # 每个页面的链接格式如下，不同页面数字不同
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        log('抓取的url -> ', url)
        # 通过 movies_from_url 函数处理每一个url
        movies = movies_from_url(url)
        print('top250 movies', movies)
        log('top250 movies', movies)
        [download_image(m.cover_url, str(m.name)) for m in movies]


if __name__ == '__main__':
    main()
