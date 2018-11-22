from django.contrib import admin
from beerapp.models import BeerBar

# Register your models here.
class AdminBeerBar(admin.ModelAdmin):
    list_display = ['bno','bname','color','bloc','alcholic']


admin.site.register(BeerBar,AdminBeerBar)

