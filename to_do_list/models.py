from django.db import models




class ToDo(models.Model):
    task = models.CharField(max_length=100)
    units = models.IntegerField()
    