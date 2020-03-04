# 배포환경 세팅파일
from geniusYong_notice.conf.utils import get_server_info_value
from .base import *

SETTING_PRD_DIC = get_server_info_value("prod")

SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]
DEBUG = False

ALLOWED_HOSTS = [

]

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']["default"]
}