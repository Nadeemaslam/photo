
import os, sys
from django.conf.urls import url,patterns
from photo import views
from albumsite import settings
from django.views.generic import  DetailView
from django.core.urlresolvers import reverse
from models import Image


urlpatterns=patterns('',
	url(r"^album/(?P<pk>\d+)$",views.album,name="album"),
	url(r'^image/(?P<pk>\d+)$', DetailView.as_view(model=Image,
    							template_name="photo/image.html")),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^upload/$',views.upload,name="upload"),
	
	url(r'',views.main),
	
	)