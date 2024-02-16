from django import forms
from app.models import Rating,Order

class  RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant','user','rating')
 
 
class ProductStockException(Exception):
    pass        
class ProductOrderForm(forms.ModelForm):
    class Meta:
        model =  Order
        fields = ('product','number_of_items')
        
    def save(self, commit=True):
        order = super().save(commit=False)
        if order.product.number_in_stock < order.number_of_items :
            raise ProductStockException(f"Not enough stock for this product : {order.product}")
        if commit:
            order.save()
        return order
    