from django.shortcuts import render
from django.utils.safestring import mark_safe

from movie_night.utils import create_cal


def calendar(request):
    # Create full HTML Cal - This is from <body> to </body>
    cal = create_cal()
    return render(request, 'movie_night/base_content.html', {'calendar': mark_safe(cal), })
