"""checktable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu.views import *
from table.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showtables, name="tables"),
    path('createtable/', create, name="createtable"),
    path('update/<int:id>', update, name="update"),
    path('endtable/<int:id>', endtable, name="endtable"),
    path('menus/', showmenus, name="showmenus"),
    path('createmenu/', createmenu, name="createmenu"),
    path('updatemenu/<int:id>', updatemenu, name="updatemenu"),
    path('showresults/', showresults, name="showresults"),
    path('updateresult/<int:id>', updateresult, name="updateresult"),
    path('deleteresult/<int:id>', deleteresult, name="deleteresult"),
    path('accounts/',include('allauth.urls')),
]
