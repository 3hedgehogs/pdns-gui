#!/bin/sh
# Example .env file

# Don't change it: Django won't load .env again
READ_ENV=""

# Django application
DJANGO_SETTINGS_MODULE="pdns_gui.settings"

# Debug mode
# DEBUG="yes"
DEBUG_TOOLBAR_PATCH_SETTINGS="yes"
INTERNAL_IPS="localhost,127.0.0.1,::1"
ALLOWED_HOSTS="*"

# Application definition
EXTRA_BASE_APPS=
# LOCAL_APPS="debug_toolbar"

# Middleware definition
EXTRA_MIDDLEWARE=
# LOCAL_MIDDLEWARE="debug_toolbar.middleware.DebugToolbarMiddleware"

# Internationalization
LANGUAGE_CODE="en-us"
TIME_ZONE="GMT"

# Default directories
# SITE_DIR="/opt/pdns-gui"
# PROJECT_DIR="/opt/pdns-gui/lib/python*/site-packages/pdns_gui" # depends on Python version
# RUN_DIR="/opt/pdns-gui/run"

# Static files (CSS, JavaScript, Images)
STATIC_URL="/static/"
# STATIC_ROOT="/opt/pdns-gui/run/static"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL="/media/"
# MEDIA_ROOT="/opt/pdns-gui/run/media"

# Revproxy
USE_X_FORWARDED_HOST="yes"

# Database
# DATABASE_DEFAULT_URL="mysql:///hello_world?init_command=SET%20default_storage_engine=InnoDB,sql_mode=STRICT_TRANS_TABLES,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci&read_default_file=.my.cnf&read_default_group=client:hello_world"
# DATABASE_DEFAULT_URL="mysql:///hello_world?init_command=SET%20default_storage_engine=InnoDB,sql_mode=STRICT_TRANS_TABLES,character_set_connection=utf8mb4,collation_connection=utf8mb4_0900_ai_ci	&read_default_file=.my.cnf&read_default_group=client:hello_world"
# DATABASE_DEFAULT_URL="postgres://postgres:postgres@localhost/hello_world"
DATABASE_DEFAULT_URL="sqlite:///run/db/hello_world.sqlite"
# DATABASE_DEFAULT_URL="mysql:///django?init_command=SET%20default_storage_engine=InnoDB,sql_mode=STRICT_TRANS_TABLES,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci&read_default_file=.my.cnf&read_default_group=client:django"
# DATABASE_DEFAULT_URL="mysql:///django?init_command=SET%20default_storage_engine=InnoDB,sql_mode=STRICT_TRANS_TABLES,character_set_connection=utf8mb4,collation_connection=utf8mb4_0900_ai_ci	&read_default_file=.my.cnf&read_default_group=client:django"
# DATABASE_DEFAULT_URL="postgres://postgres:postgres@localhost/django"
DATABASE_DJANGO_URL="sqlite:///run/db/django.sqlite"
# DATABASE_DJANGO_URL="mysql:///django?init_command=SET%20default_storage_engine=InnoDB,sql_mode=STRICT_TRANS_TABLES,character_set_connection=utf8,collation_connection=utf8_unicode_ci&read_default_file=.my.cnf&read_default_group=mysql:django"
# DATABASE_CHARSET="utf8mb4"
# DATABASE_COLLATION="utf8mb4_unicode_ci"
# DATABASE_FOR_APPS="blog=default,*=django"

# LDAP authentication
# LDAP_AUTH_URL="ldaps://ldap.example.com:636"
# LDAP_AUTH_FORMAT_USERNAME="django_python3_ldap.utils.format_username_active_directory"
# LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN="DOMAIN"
# LDAP_AUTH_SEARCH_BASE="OU=Users and Workstations,DC=example,DC=com"
# LDAP_AUTH_OBJECT_CLASS="user"
# LDAP_AUTH_USER_FIELDS="username=sAMAccountName,first_name=givenName,last_name=sn,email=mail"
# LDAP_AUTH_CLEAN_USER_DATA="django_python3_ldap.utils.clean_user_data"
