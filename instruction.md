to run first app :- python manage.py runserver

create the first app -> python manage.py startapp appName

create urls.py in your app for routing for the app

register your paths of app in main app urls.

enable jinja plugin for dtl

for travel templete:- copy the index in template folder

create urls in the new app travel

copy other static files in the new static folder

add path in settings.py

after creating static files :-  python .\manage.py collectstatic

add {% load static %} in index.html and add {% static 'static url' %} in href's and src

create models in travel/models for dynamic adding values

show if else in index.html

connect DB, settings line 76

connector => pip install psycopg2


add in settings installed apps => 'travel.apps.TravelConfig',
commadn to migrate the model to DB  => python manage.py makemigrations

for doing sql migration to DB tables :=> python .\manage.py sqlmigrate travel 0001
                                     =>  python .\manage.py migrate


create a super user for admin => python manage.py createsuperuser
user=> david
mail=> cdac mail
pass => root

add Destination in admin.py in travel app


for fetching data from DB =>add in views.py =>  Destination.objects.all()
