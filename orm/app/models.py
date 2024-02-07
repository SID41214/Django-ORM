

# Create your models here.
from datetime import date
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    
    
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN ='IN','Indian'
        CHINESE ='CH','Chinese'
        ITALIAN = 'IT','Italian'
        GREEK ='GR','Greek'
        MEXICAN ='MX','Mexican'
        FASTFOOD = 'FF','Fast Food'
        OTHER ='OT','Other'
        
    name =models.CharField(max_length=100)
    website =models.URLField(default='')
    date_opened = models.DateTimeField()
    latitude =models.FloatField()
    longitude =models.FloatField()
    restaurant=models.CharField(max_length=2,choices=TypeChoices.choices)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    rating =models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    
    def __str__(self):
        return f"Rating : {self.rating}"
    
    
class Sale(models.Model):
    restaurant =models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True,related_name='sales')
    income = models.DecimalField(max_digits=8,decimal_places=2)
    datetime = models.DateTimeField()
    