
# DJANGO  
## Starts Django
`python3 manage.py runserver`

## Creates a project
`django-admin startproject project's name`  
 
### URL configuration for airline project.  

The urlpatterns list routes URLs to views. For more information please see
[here](https://docs.djangoproject.com/en/4.2/topics/http/urls/)

Examples:  

#### Function views  

1. Add an import:  from my_app import views  
2. Add a URL to urlpatterns:  `path('', views.home, name='home')`  
#### Class-based views      
1. Add an import:  `from other_app.views import Home  ``   
2. Add a URL to urlpatterns:  `path('', Home.as_view(), name='home')`  
#### Including another URLconf  
1. Import the include() function: `from django.urls import include, path`  
2. Add a URL to urlpatterns:  `path('blog/', include('blog.urls'))`  


## Creates an app
`python3 manage.py startapp app's name`
* Put the app's new name at settings.py
* Put the path at urls.py with the name's app  
`path('newyear/', include("apps-name.urls"))`
* Inside new app's folder create a new file called urls.py and put this code:  
  
`from django.urls import path`  
 `from . import views`  
 `urlpatterns = [`  
  >   `path("", views.index, name="index")`   
`]`
* Create a new view inside `views.py` file

#### Links
* [Wikipédia - MarkDown](https://es.wikipedia.org/wiki/Markdown)

* [Link to CS50W Lecture 3 - Django ](https://youtu.be/w8q0C-C1js4?si=bebiBGg8FLjOFPVV)

* [Week 3 Django - resources](https://cs50.harvard.edu/web/2020/weeks/3/)

* [Mozilla - Introducción a Django](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Introduction)


Marcos Davi 2023
