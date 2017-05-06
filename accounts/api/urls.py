from django.conf.urls import url

from django.views.generic.base import RedirectView
from convo.api.views import (
			ConvoListAPIView,
			)

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/convo/$', ConvoListAPIView.as_view(), name='list'), #api/convo/
]