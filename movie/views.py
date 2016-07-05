# Create your views here.
from django.views.generic.list import ListView
from movie.models import WatchList, Movie


class MovieListView(ListView):
    model = Movie
