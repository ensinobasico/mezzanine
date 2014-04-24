from __future__ import unicode_literals

SECRET_KEY = "%(secret_key)s"
NEVERCACHE_KEY = "%(nevercache_key)s"
ALLOWED_HOSTS = ['yeslow.com']

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "%(proj_name)s",
        # Not used with sqlite3.
        "USER": "%(proj_name)s",
        # Not used with sqlite3.
        "PASSWORD": "%(db_pass)s",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "%(proj_name)s"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
FABRIC = {
    "SSH_USER": "", # SSH username for host deploying to
    "HOSTS": ['188.226.188.21', ], # List of hosts to deploy to (eg, first host)
    "DOMAINS": ['yeslow.com'], # Domains for public site
    "REPO_URL": "https://github.com/ensinobasico/mezzanine/edit/master/mezzanine/project_template", # Project's repo URL
    "VIRTUALENV_HOME": "/www/home", # Absolute remote path for virtualenvs
    "PROJECT_NAME": "", # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt", # Project's pip requirements
    "GUNICORN_PORT": 8000, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "DB_PASS": "admin", # Live database password
    "ADMIN_PASS": "admin", # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
