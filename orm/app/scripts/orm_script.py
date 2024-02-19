from django.contrib.auth.models import User
from app.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models import OuterRef,Subquery
def run():
    # pass
    res=Restaurant.objects.filter(restaurant__in=['IT','GR'])
    sales = Sale.objects.filter(restaurant__in=Subquery(res.values('pk')))
    print(sales)    
    staff, created = Staff.objects.get_or_create(name='John Wick')
    res = Restaurant.objects.first()
    
    # StaffRestaurant.objects.create(
    #     staff=staff,restaurant= res,salary=20000
    # )
    
  
    # res = Restaurant.objects.get(pk=6)
    # print(res.staff_set.all())
    # staff, created = Staff.objects.get_or_create(name='John Wick')
    # staff.restaurants.set(Restaurant.objects.all()[:5])
    # print(staff.restaurants.count())
    
    # print(staff.name)
    # print(staff.restaurants.add(Restaurant.objects.first())) # pylint: disable=no-member
    # print(staff.restaurants.all())
    # print(staff.restaurants.count())


    #print(staff)
    #print(type(staff.restaurants))
    
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