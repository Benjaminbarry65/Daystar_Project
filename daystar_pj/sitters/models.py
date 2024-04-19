from django.db import models

# Create your models here.
class Sitter(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    dateAdmited = models.DateTimeField()
    status = models.IntegerField(default=0) 