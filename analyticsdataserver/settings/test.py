"""Test settings and globals."""

from analyticsdataserver.settings.base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

INSTALLED_APPS += (
    'django_nose',
)

LMS_USER_ACCOUNT_BASE_URL = 'http://lms-host'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
