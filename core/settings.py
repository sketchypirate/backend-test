from decouple import config
import dj_database_url
import os

# ROOT DIRECTORY
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = config('SECRET_KEY')

if config('PRODUCTION') == '1':
    SECURE_SSL_REDIRECT = True
    DEBUG = False
    ALLOWED_HOSTS = ['api.domain.url']

    # SAFE COOKIES
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # SECURE_HSTS_SECONDS
    SECURE_HSTS_SECONDS = 60

    # CORS, WHITELIST
    CORS_ALLOWED_ORIGINS = ["api.domain.url"]
else:
    DEBUG = True

    # UNSAFE COOKIES
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    # CORS, ALLOW ALL
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ['*']
    
    # DJANGO DEBUG TOOLBARS
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

# MODULES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # DJANGO REST
    'rest_framework',

    # DEBUG TOOLBAR
    'debug_toolbar',

    # CORS
    'corsheaders',

    # AXES
    'axes',

    # API
    'api',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# DB CONNECTION LIFETIME (in seconds)
CONN_MAX_AGE = 1800

# DB SETTINGS
if config('IS_LOCAL') == '0':
    DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL'), conn_max_age=CONN_MAX_AGE),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# STATIC CONFIGURATIONS
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
}

# PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# DEFAULT PK TYPE
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DJANGO AXES, bruteforce-protection on admin
AXES_ONLY_USER_FAILURES = True  # Never IP-ban. Only username-ban.
AXES_ONLY_ADMIN_SITE = True     # Only lock-out admin logins.
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1           # IN HOURS
AXES_DISABLE_ACCESS_LOG = True

# INTERNATIONALIZATIONS
LANGUAGE_CODE = 'sv-SE'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_TZ = True