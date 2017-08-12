from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
	form = SubsForm(request.POST or None)
	if request.method == "POST":
		form = form.save()
	return render(request, 'index.html', locals())
