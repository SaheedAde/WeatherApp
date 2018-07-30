from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=30)

    #The string representation of the class
    def __str__(self):
        return self.name

    #Show plural city as cities instead of citys
    class Meta:
        verbose_name_plural = 'cities'
