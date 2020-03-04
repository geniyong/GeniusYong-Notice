userAgent = 'Mozilla/5.0'
headers = {'User-Agent': userAgent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'ko-KR,ko;q=0.8',
           'Connection': 'keep-alive'}


def get_cleaned_text(text):
    return text.replace('/','').replace("\n", "").replace("\r", "").replace("\t", "").lstrip().rstrip().upper()