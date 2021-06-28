from django.db import models

# Create your models here.

# Services Category
CATEGORY_CHOICES = (
    ('Painter','Painter'),
    ('Repair Appliances','Repair Appliances'),
    ('Home Spa','Home Spa'),
    ('Disinfecter','Disinfecter'),
    ('Photographer','Photographer'),
    ('Chemical Guy','Chemical Guy'),
    ('Trainer','Trainer'),
    ('Child Care','Child Care'),
    ('Beauty','Beauty')
)

class Location(models.Model):
    location = models.CharField(max_length=200, null=True)
    # cover = models.FileField(upload_to='skilldrill/static/img/location', default='img/location/kathmandu.jpeg')

    def __str__(self):
        return f"{self.id}. {self.location}"


class Services(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, null=True, max_length=30)
    title = models.CharField(max_length=200)
    charge = models.IntegerField()
    time = models.IntegerField(null=True)
    description = models.CharField(max_length=2000, null=True)
    manager = models.CharField(max_length=100)
    location = models.ManyToManyField(
        Location, blank=True, related_name="services")

    def __str__(self):
        return f"{self.title}: {self.charge}"
