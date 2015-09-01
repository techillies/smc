from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from restaurant.models import Restaurant


def base(request):
    return render_to_response("index.html")


def index(request):
    buff = Restaurant.objects.all()
    return render_to_response("restaurants.html", {"restaurants":buff},)

def fetch_restaurant(request,slug):
    buff = Restaurant.objects.get(name_slug=slug)
    menu = buff.menu.all()
    return render_to_response("restaurant.html", {"restaurant":buff,"menu_set":menu},)
