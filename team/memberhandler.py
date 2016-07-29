from django.db import models
from .models import Member

def get_visible_members():
    visible_members = Member.objects.filter(visible=True)
    return visible_members
