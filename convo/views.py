from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
								CreateView,
								DetailView, 
								DeleteView,
								ListView,
								UpdateView
								)
from django.urls import reverse_lazy, reverse 
from .forms import ConvoModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Convo


# Create

class ConvoCreateView(FormUserNeededMixin, CreateView):
	form_class = ConvoModelForm
	template_name = 'convo/create_view.html'
	# success_url = reverse_lazy("convo:detail")
	# login_url = '/admin/'

# Update
class ConvoUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Convo.objects.all()
	form_class = ConvoModelForm
	template_name = 'convo/update_view.html'
	# success_url = "/convo/"

class ConvoDeleteView(LoginRequiredMixin, DeleteView):
	model = Convo
	template_name = 'convo/delete_confirm.html'
	success_url = reverse_lazy('convo:list') #/convo/

# Delete

# List/Search

# Retreive
class ConvoDetailView(DetailView):
	# template_name = "detail_view.html"
	queryset = Convo.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	# 	obj = get_object_or_404(Convo, pk=pk)
	# 	return obj

class ConvoListView(ListView):
	# template_name = "list_view.html"
	# queryset = Convo.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Convo.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(ConvoListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = ConvoModelForm()
		context['create_url'] = reverse_lazy("convo:create")
		
		# context["another_list"] = Convo.objects.all()
		return(context)



# def convo_detail_view(request, id=1):
# 	obj = Convo.objects.get(id=id) # GET from database
# 	print(obj)
# 	context = {
# 		"object": obj,
# 	}
# 	return render(request, "detail_view.html", context)

# def convo_list_view(request):
# 	queryset = Convo.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj.content)
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "list_view.html", context)