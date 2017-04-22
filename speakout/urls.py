from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from convo.views import ConvoListView
from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ConvoListView.as_view(), name='home'),
    
    url(r'^convo/', include('convo.urls', namespace='convo')),
    url(r'^api/convo/', include('convo.api.urls', namespace='convo-api')),
    url(r'^', include('accounts.urls', namespace='profiles')),
]

if settings.DEBUG:
	urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
