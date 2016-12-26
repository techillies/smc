from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from restaurant.models import Restaurant

class RestaurantListView(ListView):
	model = Restaurant

class RestaurantDetailView(DetailView):
	model = Restaurant