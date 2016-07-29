from django.contrib import admin

# Register your models here.
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

admin.site.register(Event, EventAdmin)
