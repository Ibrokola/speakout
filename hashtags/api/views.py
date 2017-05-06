from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from convo.models import Convo

from convo.api.pagination import StandardResultsPagination
from convo.api.serializers import ConvoModelSerializer

from hashtags.models import HashTag


class TagConvoAPIView(generics.ListAPIView):
	queryset = Convo.objects.all().order_by("-timestamp")
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination

	def get_serializer_context(self, *args, **kwargs):
		context = super(TagConvoAPIView, self).get_serializer_context(*args, **kwargs)
		context['request'] = self.request
		return context

	def get_queryset(self, *args, **kwargs):
		hashtag = self.kwargs.get("hashtag")
		hashtag_obj = None
		try:
			hashtag_obj = HashTag.objects.get_or_create(tag=hashtag)[0]
		except:
			pass

		if hashtag_obj:
			qs = hashtag_obj.get_convo()
			query = self.request.GET.get("q", None)
			if query is not None:
				qs = qs.filter(
						Q(content__icontains=query) |
						Q(user__username__icontains=query)
						)
			return qs
		return None