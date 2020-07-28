from django.shortcuts import render
from django.utils.safestring import mark_safe
<<<<<<< HEAD
=======
from movie_night.utils import create_cal
>>>>>>> movie-night-cal

from movie_night.utils import create_cal

<<<<<<< HEAD

def calendar(request):
    # Create full HTML Cal - This is from <body> to </body>
=======
def calendar(request):
>>>>>>> movie-night-cal
    cal = create_cal()
    return render(request, 'movie_night/base_content.html', {'calendar': mark_safe(cal), })
