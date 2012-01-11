from django.db import models
from cms.models import CMSPlugin
from django.conf import settings
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _, get_language, ugettext

# Create your models here.

#class Carousel(models.Model):
#    name = models.CharField(_('Name'),max_length=255)
#    def __unicode__(self):
#        return self.name
class CarouselPlugin(CMSPlugin):
    name = models.CharField(_('Name'),max_length=100)
    #tabs = models.ManyToManyField(CarouselTab)
    #tabs = models.ForeignKey(CarouselTab)

class CarouselTab(models.Model):
    tab = models.ForeignKey(CarouselPlugin)
    image = models.ImageField(upload_to='plugins')
    titleOne = models.CharField(_('Title 1'),max_length=255)
    titleTwo = models.CharField(_('Title 2'),max_length=255,blank=True)
    titleThree = models.CharField(_('Title 3'),max_length=255,blank=True)
    titleFour = models.CharField(_('Title 4'),max_length=255,blank=True)
    content = models.TextField(_('Content'))
    #content = models.TextField(_('Content'),widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #content =tinymce_models.HTMLField()
    def __unicode__(self):
        return self.titleOne


