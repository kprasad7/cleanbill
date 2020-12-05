from django import forms
from tech.models import MyData,ShopData
        
    
class ShopForm(forms.ModelForm):
    class Meta:
        model = MyData
        fields = ['phone']       

class hopForm(forms.ModelForm):
    class Meta:
        model = ShopData
        fields = ['name','content']       