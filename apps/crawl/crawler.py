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

from apps.crawl.models import Info
from apps.shared.utils import headers, get_cleaned_text, init_chrome_driver

from geniusYong_notice.conf.utils import get_private_info_value


# ---------------------------------
# from apps.crawl.crawler import *
# ---------------------------------
def slr():
    site_name = 'SLR'
    site_url = 'http://www.slrclub.com'
    page = 'http://www.slrclub.com/service/search/local?id=used_market&category=1&setsearch=subject&keyword=m50'

    # Connection and login procedure
    slr_user = get_private_info_value('slr')
    driver = init_chrome_driver()  # 셀레니움 크롬 드라이버 실행
    driver.get(site_url)
    driver.implicitly_wait(1)
    time.sleep(1)
    driver.find_element(By.NAME, 'user_id').send_keys(slr_user['id'])
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(slr_user['pw'])
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'bt_login').click()
    time.sleep(1)
    driver.implicitly_wait(1)

    # Loop by 1minute
    # 검색페이지 이동
    time.sleep(5)
    driver.get(page)
    driver.implicitly_wait(1)
    time.sleep(2)

    # 검색페이지 도착
    html_data = driver.page_source
    parsed_html = BeautifulSoup(html_data, 'html.parser')
    post_trs = parsed_html.select_one('#bbs_list').find('tbody').findAll('tr')
    kst = timezone(settings.TIME_ZONE)
    for post_tr in post_trs:
        pid = get_cleaned_text(post_tr.select_one('.list_num').get_text())
        if Info.objects.filter(pid=pid, site_name=site_name):
            print("이미 존재하는 정보")
            break
        content = get_cleaned_text(post_tr.select_one('.sbj').get_text())
        url = site_url + post_tr.select_one('.sbj').find('a')['href']
        pca_string = post_tr.select_one('.list_date').get_text()
        print(pca_string)
        if pca_string.find(':') != -1:
            # today hh:mm:ss
            pcss = pca_string.split(':')
            today = datetime.today()
            post_created_at = datetime(today.year, today.month, today.day, int(pcss[0]), int(pcss[1]), int(pcss[2])).astimezone(kst)
        else:
            # y:m:d
            pcss = pca_string.split('/')
            post_created_at = datetime(int("20"+pcss[0]), int(pcss[1]), int(pcss[2])).astimezone(kst)

        Info.objects.create(
            pid=pid,
            url=url,
            content=content,
            post_created_at=post_created_at,
            site_name=site_name
        )
