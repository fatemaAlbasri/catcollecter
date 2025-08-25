from django.db import models
from django.urls import reverse

from datetime import date
from django.contrib.auth.models import User


# Create your models here.

MEALS = (
    ('B','Breakefast'),
    ('L','Lunch'),
    ('D','Dinner'),
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk':self.id})
    


class Cat(models.Model):
    name = models.CharField(max_length=100) # input  text box
    breed = models.CharField(max_length=100) # input  text box
    description = models.TextField(max_length=250) # input  text area
    age = models.IntegerField() # input number
    image = models.ImageField(upload_to='main_app/static/uploads/', default="") # default that mean not required
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default= MEALS[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # if delete the cat the meals should be deleted 

    def __str__(self):
        return f"{self.cat.name} {self.get_meal_display()} on {self.date}"
