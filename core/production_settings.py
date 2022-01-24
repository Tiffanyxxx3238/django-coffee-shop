import dj_database_url

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['gitclass.herokuapp.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True),
}
