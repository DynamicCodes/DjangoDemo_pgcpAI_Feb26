step 1:- check django installed :- django-admin --version
                                 - pip install django
  go to folder,create a django project - django-admin startproject projectName


step 2 :- to run first app :- python manage.py runserver

        - create the first app -> python manage.py startapp calc (appName)

step 3 :- create urls.py in your app for routing for the app

        - register your paths of app in main calc urls.
        - create the home page in views.py
        - register the url in MAIN app URLS

step 4 :- make a templete folder

        - create home.html file
        - add in dir template section of settings.py file this =>  'DIRS': [BASE_DIR / 'templates']
        - now from calc views return the home.html 

step 5:- create base.html file for jinja patern

      - if jinja is not recognized then add the plugin from extension for DTL.
      - add the { } to home.html


step 6:- for adding 2 numbers
        
        - add form tag in home.html
        - create result.html for showing addition result.
        - in calc.urls register add mapping.
        - in views create the add function to add 2 numbers, start with GET method
        - change GET to POST method with csrf token.

step 7 :- static files (Travello Files)      

          - create a new app, python manage.py startapp travello
          - copy the index.html to template folder
          - create urls.py in travello folder
          - create function in travello VIEW file
          - update the main app urls with travello

step 8 :-  create folder static for static files

          - copy all in static folder.
          - add path in settings.py ( if not present)             
          - after creating static files :-  python .\manage.py collectstatic

step 9 :- add {% load static %} in index.html and add {% static 'static url' %} in href's and src

step 10 :- create models in travel/models for dynamic adding values

          - create variable => id: int ....

          - create object in view.py
          - pass object frm the return => {'des1':des1}
          - go to index.html line no 340, add {{ des1.name }} for object details display

# can also send multiple objects in a line => dest = [des1, des2]      

step 11 :-  add FOR loop for the above objects in index.html

step 12 :- in index top add {% static "images" as baseUrl %} for images in the card.

           add in image src => {{baseUrl}}/{{dest.image}}

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
