from django.shortcuts import render
from .forms import RatingForm,ProductOrderForm
from app.models import Restaurant,Sale,Rating
# Create your views here.
def home(request):
    
    res =Restaurant.objects.all()    # pylint: disable=no-member
    context={
        'res':res,
    }
    # if request.method =='POST':
    #     form = RatingForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         return render(request,'home.html',{'form':form})
    # context ={'form':RatingForm()}
    return render(request,'home.html',context)
def order_product(request):
    form =ProductOrderForm()
    context= {
        'form':form,
    }
    return render(request,'order.html',context)