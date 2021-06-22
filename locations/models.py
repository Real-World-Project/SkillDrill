from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=200, null=True)
    # services = models.ManyToManyField(Service, blank=True, related_name="services")
    #
    def __str__(self):
        return f"{self.id}. {self.location}"
