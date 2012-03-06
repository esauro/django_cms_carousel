from django.db import models
from cms.models import CMSPlugin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, get_language, ugettext
from mptt.models import MPTTModel, TreeForeignKey

class CarouselPlugin(CMSPlugin):
    name = models.CharField(_('Name'),max_length=100)

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


