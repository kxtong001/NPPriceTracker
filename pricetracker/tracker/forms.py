from django import forms
from .models import Item, Itemprices
#working as intended
class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('url', )
#not working - plan to use url form to insert new price at the same time
class AddNewPrice(forms.ModelForm):
    class Meta:
        model= Itemprices
        fields =()        