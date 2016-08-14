# django-movie-db
Sample django project to showcase its capability and extensibility

This project is meant to showcase Django framework capabilities. It includes following :

 1. User Auth
 2. Internationalization
 3. APIs through [Django-Rest-Framework](http://www.django-rest-framework.org/)
 4. Full text search with [Django Haystack](http://haystacksearch.org/) - WIP
 5. Debugging code with [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)

###Requirements: 
 1. Python 3.4
 2. Elasticsearch (1.7.x)
 
###Setup 
 1. Clone project
 2. Create/activate virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
 3. Install required python packages - `pip install -r requirements.pip`
 4. `python manage.py runserver` - visit http://localhost:8000/movie/
 5. Django admin - http://localhost:8000/admin/ - admin/admin@1234