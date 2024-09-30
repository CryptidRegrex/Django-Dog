from django.db import models

# Create your models here.

class Breed(models.Model):
    SIZES = {
        "Tiny",
        "Small",
        "Medium",
        "Large"
    }
    
    RATINGS = {
        1,
        2,
        3,
        4,
        5
    }
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5, choices=SIZES)
    friendliness = models.IntegerField(choices=RATINGS)
    trainability = models.IntegerField(choices=RATINGS)
    sheddingamount = models.IntegerField(choices=RATINGS)
    exerciseneeds = models.IntegerField(choices=RATINGS)
    
    def __str__(self):
        return self.name


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
    


