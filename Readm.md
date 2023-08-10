1 - Create file Pipfile

pipenv lock

2 - Instalando o django + Dependências

pipenv install django
pipenv install djangorestframework
pipenv install django-cors-headers
pipenv install psycopg2-binary
pipenv install pillow
pipenv djangorestframework-simplejwt

3 - Entrar no ambiente do python

pipenv shell

4 - Criar um projeto em django

django-admin startproject api .

5 - Startar o servidor do django

python manage.py runserver

6 - Criar apps

python manage.py startapp users

7 - Criar as migration caso tenha alteração no model

python manage.py makemigrations

8 - Execute migration

python manage.py migrate

