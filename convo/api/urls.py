from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
			LikeToggleAPIView,
			ReConvAPIView,
			ConvoCreateAPIView,
			ConvoListAPIView,
			ConvoDetailAPIView,
			)

urlpatterns = [
	# url(r'^$', RedirectView.as_view(url='/')),
    url(r'^$', ConvoListAPIView.as_view(), name='list'), # api/convo/
    url(r'^create/$', ConvoCreateAPIView.as_view(), name='create'), # /convo/create/
    url(r'^(?P<pk>\d+)/$', ConvoDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like'),
    url(r'^(?P<pk>\d+)/reconv/$', ReConvAPIView.as_view(), name='reconv'),
 #    url(r'^(?P<pk>\d+)/$', ConvoDetailView.as_view(), name='detail'), # /convo/1/
 #    url(r'^(?P<pk>\d+)/update/$', ConvoUpdateView.as_view(), name='update'), # /convo/update/
 #    url(r'^(?P<pk>\d+)/delete/$', ConvoDeleteView.as_view(), name='delete'), # /convo/1/delete/
]