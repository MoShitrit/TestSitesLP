from __future__ import unicode_literals

from django.db import models


class GA(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    site_tag = models.CharField(max_length=10000)
    legacy = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}  [{1}]'.format(self.id, self.name)


class ALPHA(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    site_tag = models.CharField(max_length=10000)
    legacy = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}  [{1}]'.format(self.id, self.name)


class UK(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    site_tag = models.CharField(max_length=10000)
    legacy = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}  [{1}]'.format(self.id, self.name)


class APAC(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    site_tag = models.CharField(max_length=10000)
    legacy = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}  [{1}]'.format(self.id, self.name)
