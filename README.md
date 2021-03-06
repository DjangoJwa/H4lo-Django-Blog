# H4lo-Django-Blog

Studying Django, Python Web Application Framwork.

## Commands

#### Execute venv

```
$ venv\Scripts\activate
```

#### Show Django version

```
$ python -m django --version
```

#### Create Project

```
$ django-admin startproject [project_name]
```

#### Run Server

```
$ python manage.py runserver [Port num]
```

포트 번호를 뒤에 입력하면 해당 입력값을 포트로 하는 서버가 열린다.<br>
포트는 기본적으로 8000으로 설정되어 있다.

#### Create Application in Project

```
$ python manage.py startapp [Application name]
```

`Project`는 다수의 `app`을 포함할 수 있고, `app`은 다수의 `project`에 포함될 수 있다.

#### Database Migration

```
$ python manage.py migrate
```

#### Make Migrations

```
$ python manage.py makemigrations [Application name]
```

`app`을 `Project`에 포함시킴을 알리기 위하여, `[Project Name]/setting.py`에 들어가 `[Application Name].apps.[Application Name]Config`를 추가해준다.<br>
`makemigrations`를 진행하기 전에 `app`의 포함여부를 알리기 위하여 선행되어야 할 작업이다.

#### Show SQL Query in migration

```
$ python manage.py sqlmigrate [Application name] [number]
```

`[number]_initial.py`와 같이 `migration`이 되었음을 확인하였다면 `sqlmigrate` 명령을 통해 `sql`문을 확인할 수 있다.


#### Use Python Shell in Django

```
$ python manage.py shell
```

#### Import Model

```python
from [Application name].models import [Class name]  # Import the model classes we just wrote
from django.utils import [Library name]  # Django Util Library
```


#### Create Administrator Account

```
$ python manage.py createsuperuser
```

```
Username (leave blank to use '[Local Name]'): [Admin name that you want to create]
Email address : [Your email address]
Password: [Your password]
Password (again): [Your password again]
Superuser created successfully.
```

`django.contrib.auth` 모듈에서 제공되는 `Django`에서 제공되는 인증 프레임워크이다.

#### Django Template System

```python

from django.template import loader
from django.http import HttpResponse

def index(request):
    ...
    template = loader.get_template('[Template Directory]')
    return HttpResponse(template.render((parameter), request))

* Directory

(Application Name)/
    template/
        (Custom - Application Name)/
            index.html
            ...
```

```python

# Different Way - Using render()

def index(request):
    ...
    return render(request, '[Template Directory]', (parameter))

```

#### Abort 404 Error

```python

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Question

...

def func(request, param):
    question = get_object_or_404((Django Model), (Keyword Parameter)))
    return render(request, '[Template Directory]', {'Key': value})

```

#### URL namespace

`Project` 내에는 수많은 `Application` 이 존재할 수 있기 때문에 하드 코딩하였을 경우에 어떤 `Application`의 `View`에서 URL을 생성하는 지에 대해 알고자 `URLconf`에 `namespace`를 추가한다.

```python
# [Application Name]/urls.py

from django.urls import path
from . import views

app_name = '[Application Name]'
urlpatterns = [
    path('', views.index, name='index'),
    path(...),
    ...,
]
```

```html
<!-- [Application Name]/templates/[Application Name]/index.html -->
<!-- 하드코딩했던 부분을 수정해보자! -->

<li><a href="{% url '[Path - Views Name]' (Parameter) %}">{{ (Data Binding) }}</a></li>

위의 코드는 하드코딩된 코드

---

<li><a href="{% '[Application Name]:[Path - Views Name]' (Parameter) %}">{{ (Data Binding) }}</a></li>

다음과 같이 `Path` 명 앞에 `Application Name` + `:` 을 덧붙여 `namespace`를 이용하자.
```