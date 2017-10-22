# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse 
from django.shortcuts import render
from .models import Employee, Grade 
from django.template import loader 

# Create your views here.

def index(request):
   # return HttpResponse("Hello World, this is my first Django page")
    employee_list = Employee.objects.order_by('id')[:5]
    #template = loader.get_template('firstapp/index.html')
    context = {
        'roles_list': employee_list,
    }
    return render(request, 'firstapp/index.html', context)
    #return HttpResponse(template.render(context, request))  

def details(request, name):
    det = Employee.objects.filter(first_name=name)
    for a in det:
        b = a.role
    return HttpResponse("%s is working as %s" %(name, b))

def test(request, name):
    listing = Employee.objects.filter(first_name = name)
    output = ', '.join([a.last_name for a in listing])
    return HttpResponse("Last name is %s" % output)


