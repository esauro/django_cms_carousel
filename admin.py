from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import CarouselPlugin, CarouselTab

#class CarouselTabInline(admin.StackedInline):
 #   model = CarouselTab
#    extra = 3

#class CarouselPluginAdmin(admin.ModelAdmin):
#    inlines = [CarouselTabInline]
#
#admin.site.register( CarouselTab,CarouselPluginAdmin)
