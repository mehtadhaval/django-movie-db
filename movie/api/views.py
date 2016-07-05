from movie.api.serializers import MovieSerializer
from movie.models import Movie
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class MoviesListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieListCreateView(RetrieveUpdateDestroyAPIView, MoviesListView):
    lookup_url_kwarg = 'id'
