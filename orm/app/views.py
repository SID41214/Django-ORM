from django.shortcuts import render,redirect
from .forms import RatingForm,ProductOrderForm
from app.models import Restaurant,Sale,Rating
from django.db import transaction
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
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            # with transaction.atomic():
            order = form.save() 
        
            #server crash 
            # import sys
            # sys.exit(1)
            order.product.number_in_stock -= order.number_of_items
            order.product.save()
            return redirect('order-product')
        else:
            context={'form':form}
            return render(request,'order.html',context)
    form =ProductOrderForm()
    context= {
        'form':form,
    }
    return render(request,'order.html',context)
            
            
            
            