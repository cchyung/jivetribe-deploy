from django.shortcuts import render, get_object_or_404
from .models import Event
from datetime import datetime


# Create your views here.
def index(request):
    all_events = Event.objects.order_by('-date')[:5]
    context = {'all_events' : all_events}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event' : event})

def edit(request, event_id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        location = request.POST['location']
        date = request.POST['date']
        updated_values = {'name':name, 'location':location, 'date':date, 'description':description}
        event = get_object_or_404(Event, pk=event_id)
        event = Event.objects.update_or_create(name='name', date='date', defaults=updated_values)
        return detail(request, event_id)

    else:
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'events/edit.html', {'event' : event})
