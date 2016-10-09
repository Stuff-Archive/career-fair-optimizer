from __future__ import unicode_literals

from django.db import models

class details(models.Model):
    company_name = models.TextField (default = "")
    upvotes = models.IntegerField (default = 0)
    downvotes = models.IntegerField (default = 0)
    def __unicode__(self):
        return self.company_name

class swag(models.Model):
    company = models.ForeignKey(details, on_delete=models.CASCADE)
    item = models.TextField(default = "")
    def __unicode__(self):
        return self.name




# Create your models here.
