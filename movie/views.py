from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html',{'name':'Sebastián Giraldo'})
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    if searchTerm:
        movies = Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'name': 'Sebastián Giraldo','searchTerm': searchTerm, 'movies': movies})

def about(request):
    #return HttpResponse('<h1>Welcome to About Page</h1>')
    return render(request, 'about.html')