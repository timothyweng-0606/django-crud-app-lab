from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('dog-detail', kwargs={'dog_id': self.id})
    

class Vaccine(models.Model):
    date = models.DateField('Vaccincation Date')
    vaccine = models.TextField(max_length=250)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  # ForeignKey to Dog


    def __str__(self):
        return f"{self.vaccine} on {self.date}"