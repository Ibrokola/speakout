from django.db.models import Q
from rest_framework import generics, permissions

from convo.models import Convo

from.pagination import StandardResultsPagination
from .serializers import ConvoModelSerializer



class ConvoCreateAPIView(generics.CreateAPIView):
	serializer_class = ConvoModelSerializer
	permission_class = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ConvoListAPIView(generics.ListAPIView):
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self, *args, **kwargs):
		qs = Convo.objects.all().order_by("-timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs