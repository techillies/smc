from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from restaurant.models import Restaurant


def index(request):
    a = Restaurant.objects.all()
    b = a[0]
    return HttpResponse(b.menu.all())


def second(request, count):
    return HttpResponse("Your count is " + count)
