from django.db import models
from cms.models import CMSPlugin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, get_language, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from django_cms_carousel.settings import *


class CarouselPlugin(CMSPlugin):
    name    = models.CharField(_('Name'),max_length=100)
    jslib   = models.CharField(_('Plugin to use'),choices=JSLIB_CHOICES,max_length=100)
    speed   = models.IntegerField(_('Transition speed'),default=1000)
    timeout = models.IntegerField(_('Pause duration'),default=2000)
   
class CarouselTab(models.Model):
    tab = models.ForeignKey(CarouselPlugin)
    image = models.ImageField(upload_to='plugins')
    title = models.CharField(_('Title'),max_length=255)
    content = models.TextField(_('Content'))
    
    order = models.IntegerField(blank = True, null = True)
  
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title


