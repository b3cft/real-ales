from django.db import models
from region.models import Region
    
class Brewery(models.Model):
    name        = models.CharField(max_length=200)
    location    = models.CharField(max_length=200, null=True)
    address     = models.TextField(null=True)
    postcode    = models.CharField(max_length=10, null=True)
    region      = models.ForeignKey(Region, null=True)
    lat         = models.FloatField(null=True)
    long        = models.FloatField(null=True)
    description = models.TextField(null=True)
    active      = models.BooleanField()

    def __unicode__(self):
        return self.name