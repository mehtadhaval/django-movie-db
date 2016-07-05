# Create your views here.
from django.shortcuts import redirect


def index(request):
    return redirect('/movie/', request)