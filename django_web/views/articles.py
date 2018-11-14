# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ..models import TeacherInfo,TeacherCategory,ArticleCategory,Article
# Create your views here.
category_map = {
    "hot":"新闻热点",
}

show_category_map = {
    "hot":"新闻热点",
}

def index(request,category):
    # teacher = TeacherInfo.objects.get(id=0)
    # context = {'teacher': teacher}
    temp = category_map.get(category, None)
    show_categor = show_category_map.get(category, None)

    if temp == None:
        return render(request, '404.html')
    else:
        list = ArticleCategory.objects.get(category=category_map.get(category, None)).article.all()
        for e in list:
            print (e.id)
        return render(request, 'articles1.html', {'list': list,'category': show_categor})
    # teacher.id = teacher.id + 1
    # teacher.save()



