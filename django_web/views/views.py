# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime
# Create your views here.
def index(request):
    context = {}
    list = ["a", "b", "c", "d"]
    for i in list:
        print i
    return render(request, 'index1.html', {'list': list})

def page_not_found(request):
    return render_to_response('404.html')