from django import forms
from app.models import Rating,Order

class  RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant','user','rating')
        
class ProductOrderForm(forms.ModelForm):
    class Meta:
        model =  Order
        fields = ('product','number_of_items')
    