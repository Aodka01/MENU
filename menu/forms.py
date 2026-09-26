from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
        }
