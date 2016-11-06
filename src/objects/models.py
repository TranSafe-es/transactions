from django.db import models
from register.models import AppRegister
import uuid


class Object(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256)
    url = models.URLField(blank=False, unique=True)

    app = models.ForeignKey(AppRegister, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ObjectByIdentifier(models.Model):
    identifier = models.CharField(max_length=128, default=uuid.uuid4, blank=False)
    object = models.ForeignKey('Object', blank=False)

    app = models.ForeignKey(AppRegister, blank=False)
