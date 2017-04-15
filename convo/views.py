from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import ConvoModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Convo


# Create

class ConvoCreateView(FormUserNeededMixin, CreateView):
	form_class = ConvoModelForm
	template_name = 'convo/create_view.html'
	success_url = "/convo/create/"
	# login_url = '/admin/'

# Update
class ConvoUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	form_class = ConvoModelForm
	queryset = Convo.objects.all()
	template_name = 'convo/update_view.html'
	success_url = "/convo/"



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
	queryset = Convo.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ConvoListView, self).get_context_data(*args, **kwargs)
		
		context["another_list"] = Convo.objects.all()
		
		print(context)
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