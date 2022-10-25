# Django (python)

A back-end, open source server side web framework.

## Model View Template

- Model: the data you want to manage (from a DB)
  >  The data is delivered as an Object Relational Mapping
- [View](##Views): a handler manager which returns the revelant template and content based on the request 
- Template: an HTML file showing the layout of the  webpage etc


-----

## Workflow

1. Django receives the URL -> check on urls.py and call the match.
2. The view, located in views.py checks for relevant models
3. models are imported from models.py file
4. the view sends the data to a specified template in the 'template' folder
5. template contains HTML and Django tags, 

-------

## Start

Set up a virtual enviroment
```sh
python -m venv myproject;
source myproject/bin/activate;
```
Install Django
´pip install Django`


### Create project
```sh
django-admin startproject $nameproject
```
Run with `py manage.py runserver` and starts the website at port 8000

### Create app

Is a webapp with a specific meaning in your project, like home page/contact form/memebrs database
`py manage.py startapp $myApp`
Create a structure like
```
nameProject
    manage.py
    nameProject/
    nameApp/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```


----------

## Views
Django takes http and returns http

This is the response (myapp/view.py)
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
```
The request via URL, in the file myapp/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### some routing
project/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
```
`py manage.py runserver` => 127.0.0.1:8000/myapp
