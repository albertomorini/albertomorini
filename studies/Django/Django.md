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

## Models
Using SQLite db

```python
from django.db import models

class Users(models.Model):
    username= models.CharField(max_lenght=10);
    password= models.CharField(max_lenght=512);
    
```
Then: `python manage.py makemigrations users`

```sql
CREATE TABLE "users_users"(
    "id" INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(10) NOT NULL,
    "password" varchar(512) NOT NULL
);
```

### Queries
```python
from users.models import Users 
Users.objects.all() #returns an empty queryset
user = Users(username='alby',password=':)')
user.save()

Users.objects.all().values() #QuerySet [{'id}:1,'username':'alby'...]

```
Show the results in browser:
```python
from django.http import HttpResponse
from django.template import loader

def idnex(request):
    template= loader.get_template('page.html')
    HttpResponse(template.render())
```
And the views.py has to be like:
```python
from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
  myUsers = Users.objects.all().values()
  output = ""
  for x in myUsers:
    output += x["username"]
  return HttpResponse(output)
```



## Templates

All the templates must be located in the templates folder.

```html
<h1>My page</h1>
<table border="1">
    {%for x in myusers %}
    <tr>
        <td>{{x.id}}</td>
        <td>{{x.user}}</td>
          <td><a href="delete/{{ x.id }}">delete</a></td>
    </tr>
    {%endfor%}
</table>
```

modify the view.pp
```python
from django.http import HttpResponse
from django.template import loader
from .model import Members

def index(request):
    myUser = Users.objects.all().values()
    template = laoder.get_template('page.html')
    contex = {
        'myuser':myUsers,
    }
    return HttpResponse(template.render(context, request))
```

## Add/delete/update records

### adding/delete
```html
<form action="addrecord/" method="post">
{% csrf_token %}
Username:<br>
<input name="username">
<br><br>
Password:<br>
<input name="password" type="password">
<br><br>
<input type="submit" value="Submit">
</form>
```
csrf_token -> handle cross site request forgeries in form where the method is POST

#### view
```python
from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
  myusers = Users.objects.all().values()
  template = loader.get_template('page.html')
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    x= request.POST['username']
    y= request.POST['password']
    user = Member(username=x, password=y)
    user.save()
    return HttpResponseRedirect(reverse('index'))
```

#### urls
int the urls file
```python
from django.urls import path
from . import views

urlpatterns = {
    path('', views.idex, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord', views.addrecord, name='addrecord'), #the action of the previous form
    path('delete/<int:id>', views.delete, name='delete'), 
}

```
