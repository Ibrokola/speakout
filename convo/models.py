from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_content

# Create your models here.




class Convo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.CharField(max_length=200, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("convo:detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ['-timestamp']

	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Convo, self).clean(*args, **kwargs)