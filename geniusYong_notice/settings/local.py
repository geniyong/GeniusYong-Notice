# 개발환경 세팅파일
from .base import *

SECRET_KEY = '_qj8z^d7%b%*0qz^%nff3yj18&+bz#qkj=%ur^rknf31+13%v9'
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}