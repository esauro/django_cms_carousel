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


from cms.plugins.text.utils import plugin_tags_to_user_html

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

class CarouselTabInline(admin.StackedInline):
    model = CarouselTab
    form = CarouselTabForm
    
    if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
        from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
        widget =  TinyMCEEditor()
    else:
        widget =  WYMEditor()
    
    CarouselTabForm.declared_fields["content"] = CharField(widget=widget, required=False)
    form = CarouselTabForm
    extra = 1
        

class CMSCarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    name = "CarouselPlugin"
    #change_form_template = 'admin/includes/fieldset.html' 
    render_template = here("templates/plugins/carousel.html")
    inlines = [CarouselTabInline]
    
    class PluginMedia:
        js = ('https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js',
              '/static/js/jquery.easing.1.3.js',
              '/static/js/jquery.coda-slider-2.0.js',
              )
   
    
    def render(self, context, instance, placeholder):
        tabs = instance.carouseltab_set.all()
        context.update({
            'tabs':tabs,
            'object':instance,
            'placeholder':placeholder
        })
        return context
    

plugin_pool.register_plugin(CMSCarouselPlugin)

