from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
					ReConvView,
					ConvoCreateView, 
					ConvoDeleteView,
					ConvoDetailView,
					ConvoListView, 
					ConvoUpdateView
					)

urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search/$', ConvoListView.as_view(), name='list'), # /convo/
    url(r'^create/$', ConvoCreateView.as_view(), name='create'), # /convo/create/
    url(r'^(?P<pk>\d+)/$', ConvoDetailView.as_view(), name='detail'), # /convo/1/
    url(r'^(?P<pk>\d+)/reconv/$', ReConvView.as_view(), name='reconv'), # /convo/1/
    url(r'^(?P<pk>\d+)/update/$', ConvoUpdateView.as_view(), name='update'), # /convo/update/
    url(r'^(?P<pk>\d+)/delete/$', ConvoDeleteView.as_view(), name='delete'), # /convo/1/delete/
]