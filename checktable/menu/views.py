from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu

# Create your views here.
def showmenus(request):
    menus = Menu.objects.all()
    count = menus.count()
    return render(request, 'menus.html', {'menus': menus, 'count':count})

def createmenu(request):
    new_menu = Menu()
    new_menu.name = request.POST['name']
    new_menu.price = request.POST['price']
    new_menu.save()
    return redirect('showmenus')

def updatemenu(request, id):
    update_menu = Menu.objects.get(id=id)
    update_menu.name = request.POST['name']
    update_menu.price = request.POST['price']
    update_menu.save()
    return redirect('showmenus')