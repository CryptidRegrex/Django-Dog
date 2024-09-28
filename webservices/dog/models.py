from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.ForeignKey(Breed,
                               on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Breed(models.Model):
    SIZES = {
        "Tiny",
        "Small",
        "Medium",
        "Large"
    }
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5, choices=SIZES)
    friendliness = "test"
    trainability
    sheddingamount
    exerciseneeds
