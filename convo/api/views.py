from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from convo.models import Convo

from.pagination import StandardResultsPagination
from .serializers import ConvoModelSerializer


class LikeToggleAPIView(APIView):
	permission_class = [permissions.IsAuthenticated]

	def get(self, request, pk, format=None):
		convo_qs = Convo.objects.filter(pk=pk)
		message = "Not allowed"
		if request.user.is_authenticated():
			is_liked = Convo.objects.like_toggle(request.user, convo_qs.first())
			return Response({'liked': is_liked})
		return Response({"message": message}, status=400)


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
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ConvoDetailAPIView(generics.ListAPIView):
	queryset = Convo.objects.all()
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination
	permission_classes = [permissions.AllowAny]

	def get_queryset(self, *args, **kwargs):
		convo_id = self.kwargs.get("pk")
		qs = Convo.objects.filter(pk=convo_id)
		if qs.exists() and qs.count() == 1:
			parent_obj = qs.first()
			qs1 = parent_obj.get_children()
			qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
		return qs.order_by("-parent_id_null", "-timestamp")

class SearchConvoAPIView(generics.ListAPIView):
	queryset = Convo.objects.all().order_by("-timestamp")
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination

	def get_serializer_context(self, *args, **kwargs):
		context = super(SearchConvoAPIView, self).get_serializer_context(*args, **kwargs)
		context['request'] = self.request
		return context

	def get_queryset(self, *args, **kwargs):
		qs = self.queryset
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs


class ConvoListAPIView(generics.ListAPIView):
	serializer_class = ConvoModelSerializer
	pagination_class = StandardResultsPagination

	def get_serializer_context(self, *args, **kwargs):
		context = super(ConvoListAPIView, self).get_serializer_context(*args, **kwargs)
		context['request'] = self.request
		return context 
		
		
	def get_queryset(self, *args, **kwargs):
		requested_user = self.kwargs.get("username")
		if requested_user:
			qs = Convo.objects.filter(user__username=requested_user).order_by("-timestamp")
		else:

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