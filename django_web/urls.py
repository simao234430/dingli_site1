from django.conf.urls import url

from django_web.views import views06
from views import views, views01, views02, views03, views04, views05, views07, views08, \
    teacherdetail,teacher,article,articles,special,lab

urlpatterns = [
    url(r'^lab/(?P<special>[0-9]{1})', lab.index),
    url(r'^special/(?P<special>[0-9]{1})', special.index),
    url(r'^index01/(?P<category>[0-9]{1})', views01.index),
    url(r'^index02/(?P<category>[0-9]{1})', views02.index),
    url(r'^index03/(?P<category>[0-9]{1})', views03.index),
    url(r'^index04$', views04.index),
    url(r'^index05/(?P<category>[0-9]{1})', views05.index),
    url(r'^index06/(?P<category>[0-9]{1})', views06.index),
    url(r'^index07/(?P<category>[0-9]{1})', views07.index),
    url(r'^index08/(?P<category>[0-9]{1})', views08.index),
    url(r'^teacherdetail/(?P<id>[0-9]{1,3})', teacherdetail.index),
    url(r'^teacher/(?P<category>[a-zA-Z0-9]+)', teacher.index),
    url(r'^articles/(?P<category>[a-zA-Z0-9]+)', articles.index),
    url(r'^article/(?P<id>[0-9]{1,30})', article.index),
    url(r'^$', views.index),
]
handler404 = views.page_not_found

# handler404 = views.page_not_found
#handler500 = page_error