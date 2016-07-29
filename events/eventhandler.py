#eventhandler.py
from .models import Event
from datetime import datetime

def get_events():
    date = str(datetime.now())
    event_list = Event.objects.filter(date__gte=date).order_by('-date')[:4]
    return event_list
