BEFORE_DJANGO_APPS = (
    'daphne',
)

DJANGO_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
)

LOCAL_APPS = ()

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework_simplejwt',

    'drf_spectacular',
    'drf_spectacular_sidecar',
    'corsheaders',
    'django_celery_results',
    'django_celery_beat',
    'django_countries',
    'django_filters',
)

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
