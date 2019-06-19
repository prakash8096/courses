from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Email_Adress=models.EmailField()
    Message=models.TextField()

    def get_absolute_url(self):
        return reverse('info')
