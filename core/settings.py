import os, secrets, dj_database_url
from pathlib import Path
from dotenv import load_dotenv
from django.core.files.storage import storages
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# Overwriting If Running locally
if os.path.isfile("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()  # take environment variables from .env.

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
# if not SECRET_KEY:
#     SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))
# Django requires a unique secret key for each Django app, that is used by several of its
# security features. To simplify initial setup (without hardcoding the secret in the source
# code) we set this to a random value every time the app starts. However, this will mean many
# Django features break whenever an app restarts (for example, sessions will be logged out).
# In your production Heroku apps you should set the `DJANGO_SECRET_KEY` config var explicitly.
# Make sure to use a long unique value, like you would for a password. See:
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY
# https://devcenter.heroku.com/articles/config-vars
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9a&h7_m*p3!ctxgy0y#%3p#ztex=mjp_h3*jrbonz$qqia313#"

# The `DYNO` env var is set on Heroku CI, but it's not a real Heroku app, so we have to
# also explicitly exclude CI:
# https://devcenter.heroku.com/articles/heroku-ci#immutable-environment-variables
IS_HEROKU_APP = (
    ("DYNO" in os.environ and not "CI" in os.environ)
    or ("HEROKU_DYNO_ID" in os.environ)
    or ("HEROKU_APP_ID" in os.environ)
)
IS_RENDER_APP = "RENDER" in os.environ
IS_SERVER_APP = "APP_NAME" in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
if IS_RENDER_APP or IS_HEROKU_APP or IS_SERVER_APP:
    DEBUG = False
    ALLOWED_HOSTS = ["*"]
    RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    ALLOWED_HOSTS += ["", ""]
    # Add here your deployment HOSTS
    CSRF_TRUSTED_ORIGINS = ['']
else:
    DEBUG = True
    ALLOWED_HOSTS = []
    ALLOWED_HOSTS += ["127.0.0.1", "127.0.0.1:8000", "localhost", "localhost:8000"]
    # Add here your deployment HOSTS
    CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085']

RUNNING_APP_NAME = os.environ.get("APP_NAME") if not DEBUG else "debug"

DEBUG_USE_REMOTE_DB = bool(os.environ.get("DEBUG_USE_REMOTE_DB", False))
DEBUG_REMOTE_DB_URL = os.environ.get("DEBUG_REMOTE_DB_URL")
DEBUG_USE_REMOTE_CDN = bool(os.environ.get("DEBUG_USE_REMOTE_CDN", False))

# PYRO_JOB_INTERVAL = int(os.getenv("DEBUG_PYRO_JOB_INTERVAL", 5)) if DEBUG else int(os.getenv("PYRO_JOB_INTERVAL", 90))

PYRO_API_ID = os.environ.get("PYRO_API_ID")
PYRO_API_HASH = os.environ.get("PYRO_API_HASH")
PYRO_BOT_NAME = "bzrk_bot_prod" if (not DEBUG) else os.environ.get("DEBUG_PYRO_BOT_NAME")
PYRO_BOT_TOKEN = os.environ.get("PYRO_BOT_TOKEN") if (not DEBUG) else os.getenv("DEBUG_PYRO_BOT_TOKEN")
PYRO_SESSION_STRING = os.environ.get("PYRO_SESSION_STRING") if (not DEBUG) else os.getenv("DEBUG_PYRO_SESSION_STRING")

PYRO_ADMINS = list(map(int, os.environ.get("PYRO_ADMINS", "").split()))
PYRO_NOTIFY_ADMINS = os.environ.get("PYRO_NOTIFY_ADMINS") or True

PYRO_LOG_GROUP_ID = int(os.environ.get("PYRO_LOG_GROUP_ID"))
PYRO_LOGEXT_GROUP_ID = int(os.environ.get("PYRO_LOGEXT_GROUP_ID"))

PYRO_ADS_SCAN_ADMIN = int(os.environ.get("PYRO_ADS_SCAN_ADMIN"))
PYRO_ADS_SCAN_GROUPS = list(map(int, os.environ.get("PYRO_ADS_SCAN_GROUPS", "").split()))
PYRO_ADS_SCAN_GROUPS.append(PYRO_ADS_SCAN_ADMIN)

# Application definition
INSTALLED_APPS = [
    # Use WhiteNoise's runserver implementation instead of the Django default, for dev-prod parity.
    # "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Django doesn't support serving static assets in a production-ready way, so we use the
    # excellent WhiteNoise package to do so instead. The WhiteNoise middleware must be listed
    # after Django's `SecurityMiddleware` so that security redirects are still performed.
    # See: https://whitenoise.readthedocs.io
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # new
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ###
    "django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.tz",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                ###
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG and DEBUG_USE_REMOTE_DB:
    DATABASES = {
        "default": dj_database_url.config(
            default=DEBUG_REMOTE_DB_URL,
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
    print("‼️ Started local with remote db connection")
elif IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
else:
    DB_ENGINE = os.getenv("DB_ENGINE", None)
    DB_USERNAME = os.getenv("DB_USERNAME", None)
    DB_PASS = os.getenv("DB_PASS", None)
    DB_HOST = os.getenv("DB_HOST", None)
    DB_PORT = os.getenv("DB_PORT", None)
    DB_NAME = os.getenv("DB_NAME", None)

    if DB_ENGINE and DB_NAME and DB_USERNAME:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends." + DB_ENGINE,
                "NAME": DB_NAME,
                "USER": DB_USERNAME,
                "PASSWORD": DB_PASS,
                "HOST": DB_HOST,
                "PORT": DB_PORT,
            },
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
            }
        }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ## Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
# USE_L10N = True #new
USE_TZ = True
# USE_THOUSAND_SEPARATOR = True

LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

# Required paths to all locale dirs
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locales"),
]

# ## Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "home/static")]

STATIC_HOST = "" if (not DEBUG) or (DEBUG and DEBUG_USE_REMOTE_CDN) else ""
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") #if (DEBUG and not DEBUG_USE_REMOTE_CDN) else "https://cdn.bazaraka.com/"
STATIC_URL = STATIC_HOST + "static/"

MEDIA_HOST = "" if (not DEBUG) or (DEBUG and DEBUG_USE_REMOTE_CDN) else ""
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles") # if (DEBUG and not DEBUG_USE_REMOTE_CDN)
MEDIA_URL = MEDIA_HOST + "media/"

STORAGES = (
    {
        "default": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
        "mediafiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    # if (DEBUG and not DEBUG_USE_REMOTE_CDN)
    # else {
    #     "default": {
    #         "BACKEND": "extra.st0rages.cdn_bunny_storage.BunnyStorage",
    #     },
    #     "staticfiles": {
    #         "BACKEND": "extra.st0rages.cdn_bunny_storage.BunnyStorage",
    #         "OPTIONS": {
    #             # "cdn_url": STATIC_HOST,
    #             "cdn_dir": "static/",
    #             # "region": "de",
    #             "username": "bazaraka-storage-zone",
    #             "password": "4e176f3a-4319-4af6-b5d9d0107fc6-3fdd-424a",
    #         },
    #     },
    #     "mediafiles": {
    #         "BACKEND": "extra.st0rages.cdn_bunny_storage.BunnyStorage",
    #         "OPTIONS": {
    #             # "cdn_url": MEDIA_HOST,
    #             "cdn_dir": "media/",
    #             # "region": "de",
    #             "username": "bazaraka-storage-zone-media",
    #             "password": "d94f3329-b321-4a80-b924b1729ccc-dc1c-4a5c",
    #         },
    #     },
    # }
)


# STORAGES = {
#     #     # Enable WhiteNoise's GZip and Brotli compression of static assets:
#     #     # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
#
# # Don't store the original (un-hashed filename) version of static files, to reduce slug size:
# # https://whitenoise.readthedocs.io/en/latest/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
# WHITENOISE_KEEP_ONLY_HASHED_FILES = True
# if not DEBUG:
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Don't store the original (un-hashed filename) version of static files, to reduce slug size:
# https://whitenoise.readthedocs.io/en/latest/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
# WHITENOISE_KEEP_ONLY_HASHED_FILES = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# LOGIN_REDIRECT_URL = "/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# https://github.com/django/django/blob/main/django/utils/log.py
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "medium": {
            "format": "{asctime} | {module} | {levelname}: {message}",
            "style": "{",
        },
        "simple": {
            "format": "{module} | {levelname}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple"},
        "console-simple": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple"},
        "console-medium": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "medium"},
        "console-verbose": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"},
        "file-medium": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/".join([f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]),
            "formatter": "medium",
        },
        "file-verbose": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/".join([f"{BASE_DIR.as_posix()}", "pyrogram_bot.log"]),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console-simple", "file-medium"],
            "level": "DEBUG",
        },
        "pyrogram.session.session": {
            "handlers": ["console-medium", "file-medium"],
            "level": "WARNING",
        },
    },
}



# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": (
#                 "%(asctime)s [%(process)d] [%(levelname)s] "
#                 # "pathname=%(pathname)s lineno=%(lineno)s "
#                 # "funcname=%(funcName)s "
#                 "%(message)s"
#             ),
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#         "simple": {"format": "%(levelname)s %(message)s"},
#     },
#     "handlers": {
#         "null": {
#             "level": "DEBUG",
#             "class": "logging.NullHandler",
#         },
#         "console": {"level": "ERROR", "class": "logging.StreamHandler", "formatter": "verbose"},
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "django.request": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#     },
# }
