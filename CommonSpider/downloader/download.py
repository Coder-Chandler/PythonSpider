from utils import log
import os
import requests


def cached_url(url):
    """
    缓存, 避免重复下载网页浪费时间
    """
    # 定义一个cached文件夹
    folder = 'cached'
    # 放入cached文件夹的每一个文件名根据传入的url来取名，比如，
    # https://movie.douban.com/top250?start=25，那么文件名就是25.html
    filename = url.split('=', 1)[-1] + '.html'
    # 找到文件夹路径
    path = os.path.join(folder, filename)
    # 如果找到这个路径，说明之前已经存过来，那么open这个文件
    if os.path.exists(path):
        log('path 已经存在')
        with open(path, 'rb') as f:
            s = f.read()
            return s
    # 如果没有找到路径，说明文件夹中没有对应的文件，那么久创建文件夹
    else:
        # 建立 cached 文件夹
        log('path 不存在 新建cached文件夹')
        if not os.path.exists(folder):
            os.makedirs(folder)

        headers = {
            'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
        }
        # 发送网络请求, 把结果写入到文件夹中
        r = requests.get(url, headers)
        log('通过requests方法拿到网络请求结果，拿不到返回headers -> ', r)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content
