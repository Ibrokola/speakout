from django.contrib import admin

# Register your models here.
from .forms import ConvoModelForm
from .models import Convo




class ConvoModelAdmin(admin.ModelAdmin):
	form = ConvoModelForm	

	# class Meta:
	# 	model = Convo
		

admin.site.register(Convo, ConvoModelAdmin)