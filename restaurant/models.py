from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from geoposition.fields import GeopositionField

class Cuisine(models.Model):
	cuisine_name = models.CharField(max_length=200)
	cuisine_slug = models.SlugField(null=True)

	def __unicode__(self):
		return self.cuisine_name


class Location(models.Model):
	location_name = models.CharField(max_length=200)
	location_slug = models.SlugField(null=True)

	def __unicode__(self):
		return self.location_name


class RestaurantType(models.Model):
	restaurant_type = models.CharField(max_length=200)

	def __unicode__(self):
		return self.restaurant_type



class Restaurant(models.Model):
	full_name=models.CharField(max_length=200, null=False)
	full_address=models.CharField(max_length=255, null=False)
	contact=models.IntegerField(null=False )
	website=models.CharField(max_length=200, blank=True, null=True)
	name_slug = models.SlugField(primary_key=True)
	opening_hours = models.CharField(max_length=50, blank=True, null=True)
	additional_info = models.CharField(max_length=200, blank=True, null=True)
	history = models.TextField(null=True)
	cover_photo = models.ImageField(upload_to = settings.MEDIA_ROOT, null=True)
	geolocation = GeopositionField()
	# Boolean Fields

	serves_alcohol=models.BooleanField(default=False)
	non_veg=models.BooleanField(default=False)
	parking=models.BooleanField(default=True)
	air_conditioned=models.BooleanField(default=False)
	out_seating=models.BooleanField(default=False)
	delivery=models.BooleanField(default=False)
	reservation=models.BooleanField(default=False)
	catering = models.BooleanField(default=False)
	cost_for_two = models.IntegerField(null=True)

	# Relational Fields

	cuisines = models.ManyToManyField(Cuisine)
	location = models.ManyToManyField(Location)
	rest_type = models.ManyToManyField(RestaurantType)

	def __unicode__(self):
		return self.full_name


class Menu(models.Model):
	menu_name = models.ForeignKey(Restaurant, related_name='menu')
	menu_image = models.ImageField(upload_to=settings.MEDIA_ROOT)

	def __unicode__(self):
		return self.menu_image.name


class Gallery(models.Model):
	restaurant_photo_name= models.ForeignKey(Restaurant, related_name='gallery')
	restaurant_photo = models.ImageField(upload_to=settings.MEDIA_ROOT)

	def __unicode__(self):
		return self.restaurant_photo.name

