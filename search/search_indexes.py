from haystack import indexes
from movie.models import Movie


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    director = indexes.CharField(model_attr='director__name')
    release_date = indexes.DateField(model_attr='release_date')

    def get_model(self):
        return Movie
