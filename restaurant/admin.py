from django.contrib import admin
from restaurant.models import *

class RestaurantAdmin(admin.ModelAdmin):
	prepopulated_fields = {'name_slug':('full_name',),}

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Cuisine)
admin.site.register(Location)
