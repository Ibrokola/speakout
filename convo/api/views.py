from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from convo.models import Convo

from.pagination import StandardResultsPagination
from .serializers import ConvoModelSerializer


class ReConvAPIView(APIView):
	permission_class = [permissions.IsAuthenticated]

	def get(self, request, pk, format=None):
		convo_qs = Convo.objects.filter(pk=pk)
		message = "Not allowed"
		if convo_qs.exists() and convo_qs.count() == 1:
			# if request.user.is_authenticated():
			new_convo = Convo.objects.reconv(request.user, convo_qs.first())
			if new_convo is not None:
				data = ConvoModelSerializer(new_convo).data
				return Response(data)
			message = "Cannot reconv the same convo in 1 day"
		return Response({"message": message}, status=400)


class ConvoCreateAPIView(generics.CreateAPIView):
	serializer_class = ConvoModelSerializer
	permission_class = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ConvoListAPIView(generics.ListAPIView):
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self, *args, **kwargs):
		im_following = self.request.user.profile.get_following() #returns none if requested user isn't there
		qs1 = Convo.objects.filter(user__in=im_following)
		qs2 = Convo.objects.filter(user=self.request.user)
		qs = (qs1 | qs2).distinct().order_by("-timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs