from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import datetime

import uuid

class Task(models.Model):
    #uuid        = models.CharField(primary_key=True, max_length=36, editable=False, unique=True)
    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user        = models.ForeignKey(User)
    name        = models.CharField(max_length=50, blank=False)
    status      = models.BooleanField(default=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, editable=False)
    deleted     = models.BooleanField(default=False)    

    class Meta:
        db_table = 'task'

    def __unicode__(self):
        return self.name

    def create(self):
        self.save()

    def delete(self):
        self.deleted = True
        self.save()

    def done(self):
        self.status = True
        self.save()

