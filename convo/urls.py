from django.conf.urls import url
from .views import (ConvoCreateView, 
					ConvoListView, 
					ConvoDetailView,
					ConvoUpdateView)

urlpatterns = [
    url(r'^$', ConvoListView.as_view(), name='list'), # /convo/
    url(r'^create/$', ConvoCreateView.as_view(), name='create'), # /convo/create/
    url(r'^(?P<pk>\d+)/$', ConvoDetailView.as_view(), name='detail'), # /convo/1/
    url(r'^(?P<pk>\d+)/update/$', ConvoUpdateView.as_view(), name='update'), # /convo/update/
]