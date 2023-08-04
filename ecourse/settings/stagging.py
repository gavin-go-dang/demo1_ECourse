from .base import *

DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "*"]
print(os.getenv("SENTRY_KEY_STAGGING"))
try:
    sentry_sdk.init(
        dsn=str(os.getenv("SENTRY_KEY_STAGGING")),
        integrations=[DjangoIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
except:
    pass

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, "./static")
