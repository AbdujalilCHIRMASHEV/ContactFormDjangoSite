from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.IntegerField()
    news = models.TextField(max_length=6000)

    def __str__(self):
        return self.name