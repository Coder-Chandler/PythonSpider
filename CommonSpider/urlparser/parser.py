from downloader.download import cached_url
from pyquery import PyQuery as pq
from utils import log
from dataModel import Movie


def movie_from_div(div):
    # print('开始获取每部电影的具体数据')
    # log('开始获取每部电影的具体数据')
    """
    从一个 div 里面获取到一个电影信息
    """
    # 使用 PyQuery 处理每一个div
    e = pq(div)

    # 小作用域变量用单字符
    # 创建一个Movie实例， Movie包含(name,score,quote, cover_url,ranking)这些属性
    m = Movie()
    # print('m -> ', m)
    # 把每一个属性赋值
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()
    return m


def movies_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的电影
    """
    '''
    只会下载一次
    '''
    # 通过 cached_url 处理每个传入的url得到url对应的html并写入文件
    page = cached_url(url)
    # print('page', page)
    '''
    1. 解析 dom
    2. 找到父亲节点
    3. 每个子节点拿一个movie
    '''
    # 使用 PyQuery 处理每一个page
    e = pq(page)
    # print('使用 PyQuery 处理每一个page', e)
    # print(page.decode())
    # 2.父节点
    # 找到所有的.item
    items = e('.item')
    # print('拿到 .item -> ', e)
    # 调用 movie_from_div处理所有的item
    # list comprehension
    movies = [movie_from_div(i) for i in items]
    return movies
