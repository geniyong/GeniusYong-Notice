import ssl
import urllib.request
import csv
import time

from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.timezone import datetime
from pytz import timezone
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apps.shared.utils import headers, get_cleaned_text

# ---------------------------------
# from apps.crawl.crawler import *
# ---------------------------------

def slr():
    name = 'SLR'
    site_url = 'http://www.slrclub.com'
    page = 'http://www.slrclub.com/service/search/local?id=used_market&category=1&setsearch=subject&keyword=m50'

    crawler = Crawler()
    crawler.link = site_url
    crawler.start()


class Crawler(object):
    link = None

    def start(self):
        driver = self.init_chrome_driver()  # 셀레니움 크롬 드라이버 실행
        driver.get(self.link)
        driver.implicitly_wait(1)

    def init_chrome_driver(cls):
        userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        # Get HTML source - using selenium
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument('--user-agent=' + userAgent)
        driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        return driver


def init_chrome_driver():
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    # Get HTML source - using selenium
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('--user-agent=' + userAgent)
    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    return driver


driver = init_chrome_driver()  # 셀레니움 크롬 드라이버 실행
site_url = 'http://www.slrclub.com'
driver.get(site_url)
driver.implicitly_wait(1)
driver.find_element(By.NAME, 'user_id').send_keys('monkey0201')
driver.find_element(By.NAME, 'password').send_keys('*')