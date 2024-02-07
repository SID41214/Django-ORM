from django.contrib.auth.models import User
from app.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    res = Restaurant.objects.first()
    print(res.name)
    res.name = 'New restaurant italian restaurant'
    res.save()
    
    # user = User.objects.first()
    # res = Restaurant.objects.first()   # pylint: disable=no-member
    # rating = Rating.objects.create(user=user,restaurant=res,rating=9) 
    # rating.full_clean()
    # rating.save()