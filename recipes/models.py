from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.TextField()
    description=models.TextField()
    cuisine=models.TextField()
    ingredients=models.TextField()
    directions=models.TextField()
    image=models.TextField()

    def __str__(self):
        return self.name
