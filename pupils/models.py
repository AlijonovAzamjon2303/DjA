from django.db import models

# Create your models here.
class Pupil(models.Model):
    name = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.fam}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)

    def __str__(self):
        return self.name