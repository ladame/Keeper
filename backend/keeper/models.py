from django.db import models

# Create your models here.
class Keeper(models.Model):
    title = models.CharField("title", max_length=240)
    note = models.CharField("note", max_length = 720)

    def __str__(self):
        return self.name
    
    