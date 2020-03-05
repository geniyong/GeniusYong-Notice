from selenium import webdriver

userAgent = 'Mozilla/5.0'
headers = {'User-Agent': userAgent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'ko-KR,ko;q=0.8',
           'Connection': 'keep-alive'}


def get_cleaned_text(text):
    return text.replace('/','').replace("\n", "").replace("\r", "").replace("\t", "").lstrip().rstrip().upper()


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