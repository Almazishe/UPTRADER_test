from django.shortcuts import render

from .models import Menu

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus/menus.html', {'menus': menus})