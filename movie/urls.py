from django.conf.urls import url
from movie import views

urlpatterns = [
    url(r'', views.MovieListView.as_view()),
]
