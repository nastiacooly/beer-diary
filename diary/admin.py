from django.contrib import admin


# Registering my models here.
from .models import BeerType, BeerReview

admin.site.register(BeerType)

# Define and register the admin class
@admin.register(BeerReview)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'beertype', 'rating', 'date')
    list_filter = ('creator', 'name', 'beertype', 'rating')