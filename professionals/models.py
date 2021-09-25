from django.db import models
from locations.models import Services

# Create your models here.
class Professional(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    services = models.ManyToManyField(Services, related_name="prof_serv")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register(self):
        self.save()

    @staticmethod
    def get_professional_by_email(email):
        try:
            return Professional.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Professional.objects.filter(email = self.email):
            return True

        return False




