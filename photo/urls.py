from django.conf.urls import url,patterns
from photo import views
from albumsite import settings
from django.views.generic import  DetailView
from models import Image

urlpatterns=patterns('',
	url(r'^image/(?P<pk>\d+)$', DetailView.as_view(model=Image,
    							template_name="photo/image.html")),
	url(r'',views.main),
	
	)