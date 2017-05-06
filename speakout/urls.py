from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from hashtags.api.views import TagConvoAPIView
from hashtags.views import HashTagView
from convo.api.views import SearchConvoAPIView
from convo.views import ConvoListView
from .views import home, SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ConvoListView.as_view(), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^convo/', include('convo.urls', namespace='convo')),
    url(r'^api/tags/(?P<hashtag>.*)/$', TagConvoAPIView.as_view(), name='tag-convo-api'),
    url(r'^api/search/$', SearchConvoAPIView.as_view(), name='search-api'),
    url(r'^api/convo/', include('convo.api.urls', namespace='convo-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^', include('accounts.urls', namespace='profiles')),
]

if settings.DEBUG:
	urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))