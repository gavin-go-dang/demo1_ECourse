from .base import *

DEBUG = False
ALLOWED_HOSTS = ["0.0.0.0", "*"]

sentry_sdk.init(
    dsn=os.getenv("SENTRY_KEY_PRODUCTION"),
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
