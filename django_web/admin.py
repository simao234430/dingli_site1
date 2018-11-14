# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

import sys;

reload(sys);
sys.setdefaultencoding("utf8")

admin.site.register(Article)
admin.site.register(TeacherInfo)
admin.site.register(TeacherCategory, TeacherCategoryAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
# Register your models here.
