from django.contrib import admin
from restaurant.models import *


class MenuImageInline(admin.TabularInline):
	model = Menu
	extra = 3

class GalleryImageInline(admin.TabularInline):
	model = Gallery
	extra = 3

class RestaurantAdmin(admin.ModelAdmin):
	change_list_filter_template = "admin/filter_listing.html"
	change_list_template = "admin/change_list_filter_sidebar.html"
	prepopulated_fields = {'name_slug':('full_name',),}
	list_filter = ("full_name","website")
	inlines = [MenuImageInline ,GalleryImageInline ,]

class MyModelAdmin(admin.ModelAdmin):
	def get_model_perms(self,request):
		return {}

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Cuisine,MyModelAdmin)
admin.site.register(Gallery,MyModelAdmin)
admin.site.register(Location,MyModelAdmin)
admin.site.register(RestaurantType,MyModelAdmin)
admin.site.register(Menu,MyModelAdmin)
