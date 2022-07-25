# :bangladesh: Basic Django :bangladesh:

#### Create and Activate virtual environment

```
virtualenv venv -p python3
source venv/bin/activate
```

#### Create requirements.txt file

```
pip freeze > requirements.txt
or
echo "django>=3.2,<3.3" > requirements.txt
```

#### Install package or requirements.txt file

```
pip install django>=3.2,<3.3
or
pip install -r requirements.txt
```

#### Create Django project or app

```
django-admin startproject <project_name> .
or
python manage.py startapp <app_name>
```

#### Start development server

```
python manage.py runserver
```
