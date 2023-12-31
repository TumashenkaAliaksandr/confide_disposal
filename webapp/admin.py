from django.contrib import admin
from .models import *


class DisposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'is_main')

admin.site.register(Disposal, DisposalAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'is_main')

admin.site.register(Slider, SliderAdmin)
