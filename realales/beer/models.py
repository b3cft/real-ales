from django.db import models
from brewery.models import Brewery

class Beer(models.Model):
    name      = models.CharField(max_length=200) 
    brewery   = models.ForeignKey(Brewery)
    notes     = models.TextField(null=True, blank=True)
    abv       = models.FloatField(null=True, blank=True)
    og        = models.IntegerField(null=True, blank=True)
    parent    = models.ForeignKey('self', null=True)
    active    = models.NullBooleanField(default=1, null=True)
    
    
    def __unicode__(self):
        return self.name