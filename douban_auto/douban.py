import time
from selenium import webdriver
from scrapy import Selector
import urllib.request
from PIL import Image
browser = webdriver.Chrome()

# selenium 完成模拟登陆
browser.get("http://accounts.douban.com/login")
time.sleep(5)
browser.find_element_by_css_selector(".article .item #email").send_keys("13770955080")
browser.find_element_by_css_selector(".article .item #password").send_keys("iloveyou1314")
try:
    catcha = browser.find_element_by_css_selector("#captcha_image")
    if catcha is not None:
        print('saving captcha image...')
        captcha_link = browser.find_element_by_css_selector('#captcha_image').get_attribute('src')
        urllib.request.urlretrieve(captcha_link, 'captcha.jpg')
        Image.open('captcha.jpg').show()
        captcha_code = input('Pls input captcha code:')
        browser.find_element_by_id('captcha_field').send_keys(captcha_code)
except Exception as e:
    browser.find_element_by_css_selector(".article .item .btn-submit").click()
# 自动控制鼠标滚轮下拉
# for i in range(10):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); "
#                            "var lenOfPage=document.body.scrollHeight; return lenOfPage")
#     time.sleep(3)

# print(browser.page_source)
# t_selector = Selector(text=browser.page_source)
# 我的帖子
tag_url = 'https://www.douban.com/group/topic/112995648/'
browser.get(tag_url)
reply = []
browser.find_element_by_css_selector(".comment-wrapper .comment_textarea").send_keys("我是房主13770955080同v信")
# browser.find_element_by_css_selector(".article .item .btn-submit").click()
browser.quit()