from django.db import models
import uuid


class AppRegister(models.Model):
    name = models.CharField(max_length=256)


class AppToken(models.Model):
    token = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    app = models.ForeignKey("AppRegister", blank=False)
