from __future__ import unicode_literals

from django.db import models
from cms.models import CMSPlugin


def profile_picture_path(instance, filename):
    return 'team_{0}/{1}'.format(instance.fullname)

class Member(models.Model):
    fullname = models.CharField(max_length=30)
    title = models.CharField(max_length=100, help_text="ie. CEO or Self-Proclaimed Smartest Man Alive.")
    bio = models.TextField(max_length=500, help_text="Include a short bio about yourself and any other information you need. ie. John Smith likes to go fishing on the weekends.")
    profile_picture = models.ImageField(upload_to='team/', help_text="This picture needs to have square dimensions or it will render incorrectly.")
    visible = models.BooleanField(default=True)
    def __str__(self):
        return str(self.fullname)

class MemberPluginModel(CMSPlugin):
    member = models.ForeignKey(Member)
    def __str__(self):
        return self.member.fullname
