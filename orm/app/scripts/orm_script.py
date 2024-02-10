from django.contrib.auth.models import User
from app.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    
    print(Restaurant.objects.count())
    print(Rating.objects.count())
    print(Sale.objects.count())
    # res=Restaurant.objects.first()
    # s.restaurant=res
    # s.income=12
    # s.datetime=timezone.now()
    # s.save()
    #user=User.objects.first()
    #res=Restaurant.objects.first()
    #rating=Rating.objects.create(user=user, restaurant=res,rating=5)
    #rating.full_clean()
    #rating.save()
    
    
    #res=Restaurant.objects.first()
    # print(res.pk)
    # print(res.ratings.all())    
    #print(res.delete())
#     res=Restaurant.objects.filter(name__startswith='M')
#     print(res)
#     print(res.update(
#         date_opened=timezone.now() -timezone.timedelta(days=365),
#         website='http://test.com'
#     )
# )
    
    
    
    
    
    # user = User.objects.first()
    # res = Restaurant.objects.first()   # pylint: disable=no-member
    # rating = Rating.objects.create(user=user,restaurant=res,rating=9) 
    # rating.full_clean()
    # rating.save()