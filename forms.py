from django.forms.models import ModelForm
from models import CarouselTab
from django import forms
from django.conf import settings

class CarouselTabForm(ModelForm):
    content = forms.CharField()
    
    fields = (('title','image'),'content')
    class Media:
        js = (
            settings.STATIC_URL+'/admin/js/jquery.min.js',
            settings.STATIC_URL+'/cms/js/libs/jquery.ui.core.js',
            settings.STATIC_URL+'/cms/js/libs/jquery.ui.sortable.js',
            settings.STATIC_URL+'/js/sortableTab.js',
        )

    class Meta:
        model = CarouselTab
        exclude = ('content','page', 'placeholder', 'language', 'plugin_type')
        fields = ('title','image','order','content')
