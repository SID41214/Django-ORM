from django.shortcuts import render
from .forms import RatingForm

# Create your views here.
def home(request):
    if request.method =='POST':
        form = RatingForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request,'home.html',{'form':form})
    context ={'form':RatingForm()}
    return render(request,'home.html',context)