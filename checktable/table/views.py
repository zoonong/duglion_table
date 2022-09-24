import imp
from django.shortcuts import render, redirect
from .models import Table
from menu.models import Menu

# Create your views here.

def showtables(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def create(request):
    new_table = Table()
    new_table.number = request.POST['number']
    new_table.save()
    return redirect('tables')