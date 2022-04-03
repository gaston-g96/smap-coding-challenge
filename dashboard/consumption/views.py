# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from numpy import average

# from dashboard.consumption import models
from .models import Consumption, User
# Create your views here.
user_data=User.objects.all()
consumption_data =Consumption.objects.all()

def get_total_consumption():
    total=0
    for u in consumption_data:
        total += u.consumption   
    return total

def get_all_users():
    all_users = len(User.objects.all())
    return all_users

def get_average_consumption(total_consumption, all_users):
    average = total_consumption/all_users
    return average    
    

def summary(request):
    # Get Total Consumption Data...
    total_consumption=get_total_consumption()
    # Get Count of All users...
    all_users =  get_all_users()
    # Get Average Consumption...
    average_consumption = get_average_consumption(total_consumption,all_users)
    
    context = {
        'total_users': f"TOTAL USERS:{all_users}",
        'total_consumption': f"TOTAL CONSUMPTION:{total_consumption}",
        'average_consumption': f"AVERAGE CONSUMPTION:{average_consumption}",
        'user_data':user_data,
        
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
