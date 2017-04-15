from django import forms

from .models import Convo

class ConvoModelForm(forms.ModelForm):
	class Meta:
		model = Convo
		fields = [
			# "user",
			"content"
		]

	# def clean_content(self, *args, **kwargs):
	# 	content = self.cleaned_data.get("content")
	# 	if content == "abc":
	# 		raise forms.ValidationError("Cannot be ABC")
	# 	return content 