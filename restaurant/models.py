from django.db import models
from django.template.defaultfilters import slugify

class Cuisine(models.Model):
	cuisine_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.cuisine_name


class Location(models.Model):
	location_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.location_name

class Restaurant(models.Model):
	full_name=models.CharField(max_length=200, null=False, primary_key=True)
	full_address=models.CharField(max_length=255, null=False)
	contact=models.IntegerField(max_length=20, null=False )
	website=models.CharField(max_length=200, blank=True, null=True)
	name_slug = models.SlugField()
	opening_hours = models.CharField(max_length=50, blank=True, null=True)
	additional_info = models.CharField(max_length=200, blank=True, null=True)
	history = models.TextField(null=True)

	# Boolean Fields

	serves_alcohol=models.BooleanField(default=False)
	non_veg=models.BooleanField(default=False)
	parking=models.BooleanField(default=True)
	air_conditioned=models.BooleanField(default=False)
	out_seating=models.BooleanField(default=False)
	delivery=models.BooleanField(default=False)
	reservation=models.BooleanField(default=False)
	catering = models.BooleanField(default=False)

	# Relational Fields

	cuisines = models.ManyToManyField(Cuisine)
	location = models.ManyToManyField(Location)

	def __unicode__(self):
		return self.full_name
