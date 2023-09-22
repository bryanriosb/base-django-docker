"""Development config."""
from .base import *  # NOQA
from corsheaders.defaults import default_headers
from .core.database import *

# Base
DEBUG = True

# Security
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "*bQE=R3$#&{(heZ120c9?z1$Fx807HiB-{iiD]^aC5#h$[5,FKN5;MVbh^Npkhr"
)
ALLOWED_HOSTS = [
    ".localhost",
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Database
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = os.getenv('CONN_MAX_AGE', default=60)

# Cache
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.getenv('REDIS_URL')],
        },
    },
}

# CSRF
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173"
]
CSRF_COOKIE_NAME = 'XSRF-TOKEN'
CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'x-xsrf-token',
    'access-control-allow-headers',  # this one is important
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http:\/\/localhost:*([0-9]+)?$",
]