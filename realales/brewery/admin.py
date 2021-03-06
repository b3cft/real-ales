from django.contrib import admin
from brewery.models import Brewery
from beer.models import Beer

class BeersInline(admin.TabularInline):
    model = Beer
    extra = 3

class BrewerysAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Location', {'fields': ['address', 'postcode', 'lat', 'long'], 'classes': ['collapse']}),
        ('Region', {'fields': ['location', 'region'], 'classes': ['collapse']}),
    ]
    list_display   = ('name', 'active', 'region','location')
    list_filter    = ['active', 'region']
    search_fields  = ['name', 'location']
    inlines        = [BeersInline]

admin.site.register(Brewery, BrewerysAdmin)
