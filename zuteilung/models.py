# zuteilungen/models.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models, connection
from django.db.models import Max
from django.core.urlresolvers import reverse
from parler.models import TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager

# Create your models here.
EIGENSCHAFT_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
    )


class ZuBaseFilNrManager(models.Manager):
    def get_queryset(self):
        return super(ZuBaseFilNrManager, self).get_queryset().filter(mandant='2')

class ZuBaseFilNr(models.Model):
    mandant = models.IntegerField("Mandant", unique=False, blank=False)
    lanr    = models.IntegerField("Filiale", unique=True, blank=False)
    name    = models.CharField("Name", blank=False, max_length=150)

    objects = models.Manager()
    manr = ZuBaseFilNrManager()

    tags = TaggableManager()

    class Meta:
        ordering = ('lanr',)

    def get_absolute_url(self):
        return reverse('zuteilung:filial_list',
                       args=[self.pk])

class ZuBaseFilNrDet(models.Model):
    effdt   = models.DateField("Gültig ab", auto_now=False, default=timezone.now)
    filiale = models.ForeignKey('ZuBaseFilNr',on_delete=models.CASCADE, related_name='zubasefilrdets')
    aktiv   = models.BooleanField("Aktiv", default=False)
    flaeche = models.FloatField("Fläche")
    eigenschaft = models.CharField("Eigenschaft", max_length=1, choices= EIGENSCHAFT_CHOICES, default='E')
    umsatz      = models.DecimalField("Umsatz",max_digits=10,decimal_places=2,default=0)
    updated = models.DateTimeField(auto_now=True)

class ZuBaseWabe(models.Model):
    mandant = models.IntegerField("Mandant", unique=False, blank=False)
    wabe    = models.IntegerField("Warenbereich", unique=True, blank=False)
    name    = models.CharField("Name", blank=False, max_length=150)

class ZuBaseWabeKat(models.Model):
    filiale = models.ForeignKey('ZuBaseFilNrDet', on_delete=models.CASCADE, related_name='zubasewabekats')
    wabe    = models.ForeignKey('ZuBaseWabe', on_delete=models.CASCADE, related_name='wabehistory')
    eigenschaft = models.CharField("Eigenschaft", max_length=1, choices=EIGENSCHAFT_CHOICES, default='E')
    umsatz = models.DecimalField("Umsatz", max_digits=10, decimal_places=2,default=0)

class MyUtil():
    '''
    Its pretty clean and nice way to define stored procedures inside the class,
    especially models.py (I hope someone will write a automatic generation for all
    stored procedure calls soon.)
    '''
    def getfilialumsatz(self, in_jahr, in_manr, in_lanr):
        cursor = connection.cursor()
        cursor.execute("select PKG_ZUTEILUNG.GET_FILIALUMSATZ(%s, %s, %s) from dual", (in_jahr, str(in_manr), str(in_lanr)))
        ret = cursor.fetchone()
        cursor.close()
        return ret[0]

    def getfilialumsatzwabe(self, in_jahr, in_manr, in_lanr, in_wabe):
        cursor = connection.cursor()
        cursor.execute("select PKG_ZUTEILUNG.GET_FILIALUMSATZ_WABE(%s, %s, %s, %s) from dual", (in_jahr, str(in_manr), str(in_lanr), str(in_wabe)))
        ret = cursor.fetchone()
        cursor.close()
        return ret[0]
