from django.conf.urls import url, include

from django.views.generic.base import RedirectView
from .views import (
					UserDetailView,
					UserFollowView
					)

urlpatterns = [
	# url(r'^$', RedirectView.as_view(url='/')),
    # url(r'^search/$', ConvoListView.as_view(), name='list'), # /convo/
    # url(r'^create/$', ConvoCreateView.as_view(), name='create'), # /convo/create/
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'), # /api/convo/id/reconv/
    # url(r'^(?P<pk>\d+)/update/$', ConvoUpdateView.as_view(), name='update'), # /convo/update/
    # url(r'^(?P<pk>\d+)/delete/$', ConvoDeleteView.as_view(), name='delete'), # /convo/1/delete/
]