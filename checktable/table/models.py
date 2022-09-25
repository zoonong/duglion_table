from django.db import models

# Create your models here.
class Table(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=False)
    person = models.IntegerField(default=0)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    drink1 = models.IntegerField(default=0)
    drink2 = models.IntegerField(default=0)
    drink3 = models.IntegerField(default=0)
    drink4 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.IntegerField(default=0)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    drink1 = models.IntegerField(default=0)
    drink2 = models.IntegerField(default=0)
    drink3 = models.IntegerField(default=0)
    drink4 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)    

class Total(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.IntegerField(default=0)
    menu1 = models.IntegerField(default=0)
    menu2 = models.IntegerField(default=0)
    menu3 = models.IntegerField(default=0)
    menu4 = models.IntegerField(default=0)
    drink1 = models.IntegerField(default=0)
    drink2 = models.IntegerField(default=0)
    drink3 = models.IntegerField(default=0)
    drink4 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)  