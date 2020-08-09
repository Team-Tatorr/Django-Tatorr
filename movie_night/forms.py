from django.forms import ModelForm
from .models import Event


# Form used to submit new movies the the movie night calendar
class MovieForm(ModelForm):
    class Meta:
        model = Event
        fields = ['movie_name', 'start_day', 'start_time']
