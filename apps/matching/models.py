from django.db import models

class AlbumImage(models.Model):
    image = models.ImageField()
