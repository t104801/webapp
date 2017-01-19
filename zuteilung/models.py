from __future__ import unicode_literals

from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class ZuBaseFilNr(models.Model):
    mandant = models.IntegerField("Mandant", unique=False, blank=False)
    lanr    = models.IntegerField("Filiale", unique=True, blank=False)
    name    = models.CharField("Name", blank=False, max_length=150)


