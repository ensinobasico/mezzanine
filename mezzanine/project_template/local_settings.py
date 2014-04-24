DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "%(SECRET_KEY)s"
NEVERCACHE_KEY = "%(NEVERCACHE_KEY)s"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

FABRIC = {
    "SSH_USER": "", # SSH username for host deploying to
    "HOSTS": ['188.226.188.21'], # List of hosts to deploy to (eg, first host)
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
