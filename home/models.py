from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.subject
