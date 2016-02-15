from django.conf.urls import url
from . import views

app_name='tc_demo'
urlpatterns=[
    url(r'^$',views.index,name='index'),
	url(r'^getfile/$',views.getfile,name='getfile'),
	url(r'^getresult/$',views.getresult,name='getresult'),
]
