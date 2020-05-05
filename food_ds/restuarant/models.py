from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=70)
    proprietor_name = models.CharField(max_length=70)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    address = models.CharField(default='Not added', max_length=100)
    district = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)




class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
    item_name = models.CharField(max_length=50)
    price = models.FloatField(
        validators=[MinValueValidator(1)])




class Element(models.Model):
    element_id = models.AutoField(primary_key=True)
    element_name = models.CharField(max_length=70)
    item = models.ManyToManyField(Item)




class ItemReview(models.Model):
    title = models.CharField(max_length=100, default='No Title')
    username = models.CharField(max_length=30)
    email = models.EmailField()
    rating = models.IntegerField(choices=list(enumerate(['', 'Disappointed', 'Not Promissing', 'OK', 'Good', 'Awesome'])))
    review = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)
