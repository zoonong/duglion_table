import imp
from django.shortcuts import render, redirect
from .models import *
from menu.models import Menu

# Create your views here.

def showtables(request):
    tables = Table.objects.all()
    menus = Menu.objects.all()
    return render(request, 'tables.html', {'tables': tables, 'menus':menus})

def create(request):
    new_table = Table()
    new_table.number = request.POST['number']
    new_table.save()
    return redirect('tables')

def update(request, id):
    update_table = Table.objects.get(id=id)
    if Menu.objects.count() > 8:
        total = 0
        menus = Menu.objects.all()
        update_table.person = int(request.POST['person'])
        total = total + update_table.person * menus[0].price
        update_table.menu1 = int(request.POST['menu1'])
        total = total + update_table.menu1 * menus[1].price
        update_table.menu2 = int(request.POST['menu2'])
        total = total + update_table.menu2 * menus[2].price
        update_table.menu3 = int(request.POST['menu3'])
        total = total + update_table.menu3 * menus[3].price
        update_table.menu4 = int(request.POST['menu4'])
        total = total + update_table.menu4 * menus[4].price
        update_table.drink1 = int(request.POST['drink1'])
        total = total + update_table.drink1 * menus[5].price
        update_table.drink2 = int(request.POST['drink2'])
        total = total + update_table.drink2 * menus[6].price
        update_table.drink3 = int(request.POST['drink3'])
        total = total + update_table.drink3 * menus[7].price
        update_table.drink4 = int(request.POST['drink4'])
        total = total + update_table.drink4 * menus[8].price
        if update_table.person > update_table.drink1:
            total = total - update_table.drink1 * menus[5].price
        else:
            total = total - update_table.person * menus[5].price
        update_table.total = total
        update_table.save()
        return redirect('tables')
    else:
        return redirect('tables')
    
def endtable(request, id):
    table = Table.objects.get(id=id)
    totalResult = Total.objects.all()
    if totalResult.count() == 0:
        new_total = Total()
        new_total.person = table.person
        new_total.menu1 = table.menu1
        new_total.menu2 = table.menu2
        new_total.menu3 = table.menu3
        new_total.menu4 = table.menu4
        new_total.drink1 = table.drink1
        new_total.drink2 = table.drink2
        new_total.drink3 = table.drink3
        new_total.drink4 = table.drink4
        new_total.total = table.total
        new_total.save()
    else:
        update_total = totalResult[0]
        update_total.person = update_total.person + table.person
        update_total.menu1 = update_total.menu1 + table.menu1
        update_total.menu2 = update_total.menu2 + table.menu2
        update_total.menu3 = update_total.menu3 + table.menu3
        update_total.menu4 = update_total.menu4 + table.menu4
        update_total.drink1 = update_total.drink1 + table.drink1
        update_total.drink2 = update_total.drink2 + table.drink2
        update_total.drink3 = update_total.drink3 + table.drink3
        update_total.drink4 = update_total.drink4 + table.drink4
        update_total.total = update_total.total + table.total
        update_total.save()
    
    new_Result = Result()
    new_Result.person = table.person
    new_Result.menu1 = table.menu1
    new_Result.menu2 = table.menu2
    new_Result.menu3 = table.menu3
    new_Result.menu4 = table.menu4
    new_Result.drink1 = table.drink1
    new_Result.drink2 = table.drink2
    new_Result.drink3 = table.drink3
    new_Result.drink4 = table.drink4
    new_Result.total = table.total
    new_Result.save()
        
    table.person = 0
    table.menu1 = 0
    table.menu2 = 0
    table.menu3 = 0
    table.menu4 = 0
    table.drink1 = 0
    table.drink2 = 0
    table.drink3 = 0
    table.drink4 = 0
    table.total = 0
    table.save()
    return redirect('tables')

def showresults(request):
    results = Result.objects.all()
    totals = Total.objects.all()
    menus = Menu.objects.all()
    return render(request, 'results.html', {'results': results, 'menus':menus, 'totals':totals})

def updateresult(request,id):
    update_result = Result.objects.get(id=id)
    totalResults = Total.objects.all()
    totalResult = totalResults[0]
    total = 0
    menus = Menu.objects.all()
    totalResult.person = totalResult.person - update_result.person
    update_result.person = int(request.POST['person'])
    total = total + update_result.person * menus[0].price
    totalResult.person = totalResult.person + update_result.person

    totalResult.menu1 = totalResult.menu1 - update_result.menu1
    update_result.menu1 = int(request.POST['menu1'])
    total = total + update_result.menu1 * menus[1].price
    totalResult.menu1 = totalResult.menu1 + update_result.menu1

    totalResult.menu2 = totalResult.menu2 - update_result.menu2
    update_result.menu2 = int(request.POST['menu2'])
    total = total + update_result.menu2 * menus[2].price
    totalResult.menu2 = totalResult.menu2 + update_result.menu2

    totalResult.menu3 = totalResult.menu3 - update_result.menu3
    update_result.menu3 = int(request.POST['menu3'])
    total = total + update_result.menu3 * menus[3].price
    totalResult.menu3 = totalResult.menu3 + update_result.menu3

    totalResult.menu4 = totalResult.menu4 - update_result.menu4
    update_result.menu4 = int(request.POST['menu4'])
    total = total + update_result.menu4 * menus[4].price
    totalResult.menu4 = totalResult.menu4 + update_result.menu4

    totalResult.drink1 = totalResult.drink1 - update_result.drink1
    update_result.drink1 = int(request.POST['drink1'])
    total = total + update_result.drink1 * menus[5].price
    totalResult.drink1 = totalResult.drink1 + update_result.drink1

    totalResult.drink2 = totalResult.drink2 - update_result.drink2
    update_result.drink2 = int(request.POST['drink2'])
    total = total + update_result.drink2 * menus[6].price
    totalResult.drink2 = totalResult.drink2 + update_result.drink2

    totalResult.drink3 = totalResult.drink3 - update_result.drink3
    update_result.drink3 = int(request.POST['drink3'])
    total = total + update_result.drink3 * menus[7].price
    totalResult.drink3 = totalResult.drink3 + update_result.drink3

    totalResult.drink4 = totalResult.drink4 - update_result.drink4
    update_result.drink4 = int(request.POST['drink4'])
    total = total + update_result.drink4 * menus[8].price
    totalResult.drink4 = totalResult.drink4 + update_result.drink4

    if update_result.person > update_result.drink1:
        total = total - update_result.drink1 * menus[5].price
    else:
        total = total - update_result.person * menus[5].price
    totalResult.total = totalResult.total - update_result.total
    update_result.total = total
    totalResult.total = totalResult.total + update_result.total
    update_result.save()
    totalResult.save()
    return redirect('showresults')

def deleteresult(request,id):
    delete_result = Result.objects.get(id=id)
    totalResults = Total.objects.all()
    totalResult = totalResults[0]
    totalResult.person = totalResult.person - delete_result.person
    totalResult.menu1 = totalResult.menu1 - delete_result.menu1
    totalResult.menu2 = totalResult.menu2 - delete_result.menu2
    totalResult.menu3 = totalResult.menu3 - delete_result.menu3
    totalResult.menu4 = totalResult.menu4 - delete_result.menu4
    totalResult.drink1 = totalResult.drink1 - delete_result.drink1
    totalResult.drink2 = totalResult.drink2 - delete_result.drink2
    totalResult.drink3 = totalResult.drink3 - delete_result.drink3
    totalResult.drink4 = totalResult.drink4 - delete_result.drink4
    totalResult.total = totalResult.total - delete_result.total
    delete_result.delete()
    totalResult.save()
    return redirect('showresults')
    