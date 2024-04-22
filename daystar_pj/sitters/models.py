from django.db import models

# Create your models here.
class Sitter(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=25)
    dateAdmited = models.DateTimeField()
    contact = models.CharField(max_length=25)
    status = models.BooleanField(default=False) 