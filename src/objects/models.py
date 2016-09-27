from django.db import models
import uuid


class Object(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256)
    url = models.URLField(blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ObjectByUser(models.Model):
    user_uuid = models.CharField(max_length=128, default=uuid.uuid4, blank=False)
    object = models.ForeignKey('Object', blank=False)

