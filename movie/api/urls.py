from django.conf.urls import url
from movie.api import views

urlpatterns = [
    url(r'(?P<id>[0-9]+)', views.MovieListCreateView.as_view(), name='detail'),
    url(r'$', views.MoviesListView.as_view(), name='list'),
]
