from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()
    def __str__(self):
        return self.name