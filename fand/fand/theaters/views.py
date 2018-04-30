from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
# ^CSabrinas-MacBook-Pro-3:fand sabrina$ docker run -v $PWD:/opt/project -it -p 8000:8000 nobel-app ./env/bin/python3and/manage.py shell
# Python 3.5.2 (default, Nov 23 2017, 16:37:01)
# [GCC 5.4.0 20160609] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# ******** >>> from fand.theaters.models import*
# >>> Showtime.objects.values_list("time")
# <QuerySet [('10:00p',), ('10:00p',), ('10:00p',), ('10:00p',), ('10:00p',), ('10:05p',), ('10:10p',), ('10:10p',), ('10:10p',), ('10:10p',), ('10:15p',), ('10:15p',), ('10:15p',), ('10:15p',), ('10:20p',), ('10:20p',), ('10:20p',), ('10:30p',), ('10:30p',), ('10:30p',), '...(remaining elements truncated)...']>
# >>> Showtime.objects.values_list("time").distinct()
# <QuerySet [('10:00p',), ('10:05p',), ('10:10p',), ('10:15p',), ('10:20p',), ('10:30p',), ('10:35p',), ('10:40p',), ('10:50p',), ('11:00a',), ('11:00p',), ('11:10a',), ('11:20a',), ('11:30p',), ('12:00p',), ('12:05p',), ('12:10p',), ('12:15p',), ('12:20p',), ('12:25p',), '...(remaining elements truncated)...']>
# ******** >>> times=Showtime.objects.values_list("time", flat=True).distinct()
# <QuerySet ['10:00p', '10:05p', '10:10p', '10:15p', '10:20p', '10:30p', '10:35p', '10:40p', '10:50p', '11:00a', '11:00p', '11:10a', '11:20a', '11:30p', '12:00p', '12:05p', '12:10p', '12:15p', '12:20p', '12:25p', '...(remaining elements truncated)...']>
# >>>


# >>> Showtime.objects.filter(time="11:30p")
# <QuerySet [<Showtime: 11:30p>]>
# >>> Showtime.objects.filter(time="10:00p")
# <QuerySet [<Showtime: 10:00p>, <Showtime: 10:00p>, <Showtime: 10:00p>, <Showtime: 10:00p>, <Showtime: 10:00p>]>
# >>> Movie.objects.filter(showtime__in=Showtime.objects.filter(time="10:00p"))
# <QuerySet [<Movie: Blockers - ID: 206654>, <Movie: Blumhouse's Truth or Dare (2018) - ID: 208538>, <Movie: Chappaquiddick - ID: 206369>, <Movie: Love, Simon - ID: 208042>, <Movie: Ready Player One - ID: 204139>]>
# >>> give me all the movies where the showtime query is 10 pm

from .models import *

def home(request):
    return render(request, "fand/home.html", {})

def movie(request, pk):
    movie = Movie.objects.get(movid=pk)
    showtimes = Showtime.objects.filter(movie=pk)
    consolidated = {}
    for st in showtimes:
        if st.theater not in consolidated:
            consolidated[st.theater] = []
        consolidated[st.theater] += [st]
    return render(request, "fand/movie.html", {'m': movie,
                                                'consolidated': consolidated,
                                                })

def theater(request, pk):
    theater = Theater.objects.get(id=pk)
    showtimes = Showtime.objects.filter(theater=pk)
    consolidated = {}
    for st in showtimes:
        if st.movie not in consolidated:
            consolidated[st.movie] = []
        consolidated[st.movie] += [st]

    return render(request, "fand/theater.html", {'t': theater ,
                                                'consolidated': consolidated,
                                                })

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, "fand/list_movies.html", {'movies': movies})

def list_theaters(request):
    theaters = Theater.objects.all()
    return render(request, "fand/list_theaters.html", {'theaters' : theaters })

def list_showtimes(request):
    return render(request, "fand/list_showtimes.html", {})

def api(request, slug):

    if slug == 'movies':
        data = Movie.objects.values()
    elif slug == 'showtimes':
        data = Showtime.objects.values()
    else:
        data = Theater.objects.values()

    f_data = {"Data": [w for w in data]}

    return JsonResponse(f_data)
    # return render(request, "fand/api.html", {})
