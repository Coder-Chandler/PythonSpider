import time
from selenium import webdriver
from scrapy import Selector
import urllib.request
from PIL import Image
browser = webdriver.Chrome()

# selenium 完成模拟登陆
browser.get("http://accounts.douban.com/login")
time.sleep(5)
print('selenium Chrome 正在控制你的PC')
time.sleep(2)
browser.find_element_by_css_selector(".article .item #email").send_keys("13770955080")
browser.find_element_by_css_selector(".article .item #password").send_keys("iloveyou1314")
print('selenium Chrome 等待网络通讯')
time.sleep(1)
try:
    catcha = browser.find_element_by_css_selector("#captcha_image")
    print('selenium Chrome Please Wait 等待验证码传输...........')
    time.sleep(1)
    if catcha is not None:
        print('saving captcha image 获取验证码图片...')
        time.sleep(1)
        captcha_link = browser.find_element_by_css_selector('#captcha_image').get_attribute('src')
        urllib.request.urlretrieve(captcha_link, 'captcha.jpg')
        Image.open('captcha.jpg').show()
        captcha_code = input('Pls input captcha code 输入验证码:')

        print('等待网络通讯............')
        browser.find_element_by_id('captcha_field').send_keys(captcha_code)
        browser.find_element_by_css_selector(".article .item .btn-submit").click()
        tag_url = 'https://www.douban.com/group/topic/112995648/'
        browser.get(tag_url)
        # # 自动控制鼠标滚轮下拉
        # for i in range(10):
        #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); "
        #                            "var lenOfPage=document.body.scrollHeight; return lenOfPage")
        #     time.sleep(3)
        #
        # print(browser.page_source)
        # t_selector = Selector(text=browser.page_source)
        # # 我的帖子
        reply = []
        browser.find_element_by_css_selector(".comment-wrapper .comment_textarea").send_keys("呵呵呵呵呵呵呵呵呵")
        catcha = browser.find_element_by_css_selector("#captcha_image")
        print('selenium Chrome Please Wait 等待验证码传输...........')
        time.sleep(1)
        if catcha is not None:
            print('saving captcha image 获取验证码图片...')
            time.sleep(1)
            captcha_link = browser.find_element_by_css_selector('#captcha_image').get_attribute('src')
            urllib.request.urlretrieve(captcha_link, 'captcha.jpg')
            Image.open('captcha.jpg').show()
            captcha_code = input('Pls input captcha code 输入验证码:')
            print('等待网络通讯............')
            browser.find_element_by_id('captcha_field').send_keys(captcha_code)
        browser.find_element_by_css_selector("input[name=submit_btn]").click()
except Exception as e:
    browser.find_element_by_css_selector(".article .item .btn-submit").click()
'''
# 自动控制鼠标滚轮下拉
for i in range(10):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); "
                           "var lenOfPage=document.body.scrollHeight; return lenOfPage")
    time.sleep(3)

print(browser.page_source)
t_selector = Selector(text=browser.page_source)
# 我的帖子
'''
browser.find_element_by_css_selector(".article .item .btn-submit").click()
tag_url = 'https://www.douban.com/group/topic/112995648/'
browser.get(tag_url)
reply = []
browser.find_element_by_css_selector(".comment-wrapper .comment_textarea").send_keys("苏宁易购你好！！！")
# browser.find_element_by_css_selector("input[name=submit_btn]").click()
# browser.quit()