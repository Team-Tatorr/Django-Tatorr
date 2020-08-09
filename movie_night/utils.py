import calendar
from datetime import date

from movie_night.models import Event


# Creates a HTML calendar for the current month and displays the current movie events
def create_cal():
    DAYS_IN_WEEK = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # We want to print the same number 5 rows (weeks) of 7 days.
    DAYS_IN_HTML_CALENDAR = 7 * 6
    current_year = date.today().year
    current_month_name = calendar.month_name[date.today().month]
    num_events_this_month = Event.objects.all().count()
    cal_string = '<div class="container py-5">'
    cal_string += '<header class="text-center text-white mb-5">'
    cal_string += '<h1 class="display-4">JanFlix Movie Night Schedule</h1></header>'
    cal_string += '<div class="calendar shadow bg-white p-5">'
    cal_string += '<div class="d-flex align-items-center"><i class="fa fa-calendar fa-3x mr-3"></i>'
    cal_string += '<h2 class="month font-weight-bold mb-0 text-uppercase">' + current_month_name + str(
        current_year) + "</h2></div>"
    cal_string += '<p class="font-italic text-muted mb-5">There are ' + str(
        num_events_this_month) + 'movies scheduled this month.</p>'

    # Days of the week start
    cal_string += '<ol class="day-names list-unstyled">'
    for day in DAYS_IN_WEEK:
        cal_string += '<li class="font-weight-bold text-uppercase">' + day + '</li>'
    cal_string += '</ol>'

    # Days in the Month start
    cal_string += '<ol class="days list-unstyled">'

    # Dynamically generate days with classes :)
    # Start with the days from last month - month range sets first day as Monday.
    this_months_range = calendar.monthrange(date.today().year, date.today().month)
    days_in_month = this_months_range[1]
    # TODO Remove magic number
    starting_weekday = this_months_range[0] + 1

    # Time to finally make some days
    day_counter = 1
    for day in range(0, DAYS_IN_HTML_CALENDAR):
        inside_month = '<li><div class="' + 'date' + '">' + str(day_counter) + '</div></li>'
        outside_month = '<li><div class="' + 'date' + '"></div></li>'
        if day < starting_weekday:
            cal_string += outside_month
        elif day_counter > days_in_month:
            cal_string += outside_month
        else:
            # check for Event objects
            events = Event.objects.filter(start_day__month=date.today().month, start_day__day=day_counter)
            if events.count() > 0:
                cal_string += '<li>'
                cal_string += '<div class="' + 'date' + '">' + str(day_counter) + '</div>'
                for e in events:
                    cal_string += '<div class="' + 'event all-day bg-primary' + '">' + e.movie_name + '<br />' + e.start_time.strftime(
                        "%#I:%M %p") + '</div>'
                cal_string += '</li>'
            else:
                cal_string += inside_month
            day_counter = day_counter + 1
    cal_string += '</ol></div></div>'
    return cal_string
