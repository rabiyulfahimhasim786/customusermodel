# customusermodel

# Developing Django on Custom User Model

Install requirements.txt 

if it not done then manually inatall one by one 
```
-django
-rest_framework  #commaned is pip install djangorestframework
-rest_framework.authtoken
-rest_auth 
#commaned is pip install django-rest-auth
#Documnetations https://django-rest-auth.readthedocs.io/en/latest/installation.html
```

Dont for got to add these below code in setting.py

```
AUTH_USER_MODEL = "accounts.MyUser"
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'accounts',
    'rest_framework.authtoken',
    'rest_auth',
]
```
also these restframe work too
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = f"http://127.0.0.1:8000/media/"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated",],
}
```

root url configuration

```
ROOT_URLCONF = 'mysite.urls'
```
