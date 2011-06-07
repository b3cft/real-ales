from django.db import models
from region.models import Region
    
class Brewery(models.Model):
    name        = models.CharField(max_length=200)
    location    = models.CharField(max_length=200, null=True, blank=True)
    address     = models.TextField(null=True, blank=True)
    postcode    = models.CharField(max_length=10, null=True, blank=True)
    region      = models.ForeignKey(Region, null=True, blank=True)
    lat         = models.FloatField(null=True, blank=True)
    long        = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website     = models.CharField(max_length=200,null=True, blank=True)
    email       = models.CharField(max_length=200,null=True, blank=True)
    phone       = models.CharField(max_length=20,null=True, blank=True)
    mobile      = models.CharField(max_length=20,null=True, blank=True)
    fax         = models.CharField(max_length=20,null=True, blank=True)
    active      = models.BooleanField()

    def __unicode__(self):
        return self.name