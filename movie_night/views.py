from django.shortcuts import render
from django.utils.safestring import mark_safe

from movie_night.forms import MovieForm
from movie_night.utils import create_cal


def calendar(request):
    # check for form submission
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            cal = create_cal()

            return render(request, 'movie_night/base_content.html',
                          {'calendar': mark_safe(cal), 'movie_form': movie_form})

    else:
        # Create full HTML Cal - This is from <body> to </body>
        movie_form = MovieForm()
        cal = create_cal()
        return render(request, 'movie_night/base_content.html', {'calendar': mark_safe(cal), 'movie_form': movie_form})
