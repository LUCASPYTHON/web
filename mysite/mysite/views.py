#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:47:49 2018

@author: code-room
"""
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
def  menu(request):
    food1 = {'name':'tomato-egg','price':60,'comment':'good!',
            'is_spicy':False}
    food2 = {'name':'garlic-pork','price':100,'comment':'popular',
            'is_spicy':True}
    foods=[food1,food2]
    return render_to_response('menu.html',locals())