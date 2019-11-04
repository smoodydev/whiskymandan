from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=140, blank=False)
    blurb = models.CharField(max_length=140, blank=False)
    bio = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.name

class Distiller(models.Model):
    name = models.CharField(max_length=140, blank=False)
    blurb = models.CharField(max_length=140, blank=False)
    bio = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.name

class WhiskeyType(models.Model):
    name = models.CharField(max_length=140, blank=False)
    bio = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return self.name

class Whiskey(models.Model):
    distiller = models.ForeignKey(Distiller, on_delete=models.CASCADE, related_name="distiller")
    name = models.CharField(max_length=140, blank=False)
    blurb = models.CharField(max_length=140, blank=False)
    bio = models.TextField(max_length=800, blank=True)

    whiskeyType = models.ForeignKey(WhiskeyType)
    strength = models.IntegerField(blank=True)

    reviews_num = models.IntegerField(default=0)
    reviews_score = models.IntegerField(default=0)

    @property
    def average_rating(self):
        if self.reviews_num < 1:
            return "Not Rated Yet"
        else:
            return self.reviews_score / self.reviews_num

    def __str__(self):
        return self.name