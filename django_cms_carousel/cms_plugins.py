# cms_plugins.py
from django.contrib import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import CarouselPlugin, CarouselTab

import os
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from forms import CarouselTabForm
from cms.plugins.text.settings import USE_TINYMCE
from django.conf import settings
from django.forms.fields import CharField
from django_cms_carousel.settings import *

from cms.plugins.text.utils import plugin_tags_to_user_html

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

class CarouselTabInline(admin.StackedInline):
    model = CarouselTab
    
    if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
        from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
        widget =  TinyMCEEditor()
    else:
        widget =  WYMEditor()
    
    CarouselTabForm.declared_fields["content"] = CharField(widget=widget, required=False)
    form = CarouselTabForm
    extra = 0

class CMSCarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    name = "Carousel Plugin"
    render_template = here("plugins/"+JSLIB_CHOICES[0][0]+".html")
    inlines = [CarouselTabInline]
    
    def render(self, context, instance, placeholder):
        if instance and instance.jslib:
            self.render_template ="plugins/"+instance.jslib+".html"
        
        
        tabs = instance.carouseltab_set.all()
        context.update({
            'tabs':tabs,
            'object':instance,
            'placeholder':placeholder
        })
        return context
    

plugin_pool.register_plugin(CMSCarouselPlugin)

