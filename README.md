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
## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

