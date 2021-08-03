from django.db import models
from django.urls import reverse

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
    cover = models.FileField(upload_to='img/location/', default='img/location/lalitpur.jpeg')

    def __str__(self):
        return f"{self.id}. {self.location}"

    def get_absolute_url(self):
        return reverse('location_view', args=[str(self.id)])


class Category(models.Model):
    category = models.CharField(max_length=200)
    manager = models.CharField(max_length=100)
    # location = models.ManyToManyField(Location, blank=True, related_name="categories")

    def __str__(self):
        return self.category


class Services(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="rel_cat")
    title = models.CharField(max_length=200)
    charge = models.IntegerField()
    time = models.IntegerField(null=True)
    description = models.CharField(max_length=2000, null=True)
    professional = models.CharField(max_length=100)  # Todo: Many to Many
    location = models.ManyToManyField(Location, related_name="services")

    def __str__(self):
        return f"{self.title}: {self.charge}"
