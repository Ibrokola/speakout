from django.utils.timesince import timesince 
from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from convo.models import Convo


class ConvoModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	class Meta:
		model = Convo
		fields = [
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',

		]

	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y | %I:%M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago"