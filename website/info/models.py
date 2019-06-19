from django.db import models

from django.urls import reverse


class Ganesh(models.Model):
    Name = models.CharField(max_length=20)
    Comment=models.TextField()







    def __str__(self):
     return self.Name



    def get_absolute_url(self):
        return reverse('info')

