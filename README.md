# :bangladesh: Basic Django :bangladesh:

#### Create and Activate virtual environment

```shell
virtualenv venv -p python3
source venv/bin/activate
```

#### Create requirements.txt file

```shell
pip freeze > requirements.txt
or
echo "django>=3.2,<3.3" > requirements.txt
```

#### Install package or requirements.txt file

```shell
pip install django>=3.2,<3.3
or
pip install -r requirements.txt
```

#### Create Django project or app

```shell
django-admin startproject <project_name> .
or
python manage.py startapp <app_name>
```

#### Start development server

```shell
python manage.py runserver
```

#### Run migration

```shell
python manage.py makemigrations
python manage.py migrate
```

#### Django shell

```sh
python manage.py shell
```

---

#### Python dataclasses

```python
from dataclasses importdataclass

@dataclass
class BlogPost:
    title: str
    content: str

obj = BlogPost(title="Hello World", content="This is awesome")
```

#### Django Model Class

```python
from django.db import models

class Article(models.Model):
    title = models.CharField()
    content = models.TextField()

obj = Article(title="Hello World", content="This is awesome")
obj.save()

or

Article.objects.create(title="Hello World", content="This is awesome")
```

#### Get single data from database

```python
Article.objects.get(id=1)
```

#### Get random data from database

```python
Article.objects.all().order_by("?").first()
```
