from django.forms.models import ModelForm
from models import CarouselTab
from django import forms

class CarouselTabForm(ModelForm):
    content = forms.CharField()

    class Meta:
        model = CarouselTab
        exclude = ('content','page', 'position', 'placeholder', 'language', 'plugin_type')
