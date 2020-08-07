from django.shortcuts import render


# Create your views here.
def movie_calendar(request):
    return render(request, 'moviecal.html', {})
