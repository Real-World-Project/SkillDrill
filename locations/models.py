from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200, null=True)
    cover = models.FileField(upload_to='skilldrill/static/img/location', default='img/location/kathmandu.jpeg')
    # services = models.ManyToManyField(Service, blank=True, related_name="services")
    #
    def __str__(self):
        return f"{self.id}. {self.location}"

class Services(models.Model):
    service = models.CharField(max_length=200)
    manager = models.CharField(max_length=100)
    charge = models.IntegerField()
    location = models.ManyToManyField(Location, blank=True, related_name="services")

    def __str__(self):
        return f"{self.service}: {self.charge}"
