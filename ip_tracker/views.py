from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from ip_tracker.models import Network
from django.urls import reverse, reverse_lazy
from ip_tracker.forms import NetworkForm
from .filters import NetworkFilter

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')
	template = 'login.html'
	context = {}
	return render(request, template, {})


def logout_user(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home_view(request):
	template = 'list.html'
	obj = Network.objects.all()
	myFilter = NetworkFilter(request.GET, queryset=obj)
	obj = myFilter.qs
	context = {
    	'object': obj,
		'myFilter': myFilter
    }
	return render(request, "list.html", context)


@login_required(login_url='login')
def view_network(request):
	template = 'topology.html'
	return render(request, template, {})


@login_required(login_url='login')
def add_ip_address(request):
	form = NetworkForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('home'))
	context = {
		'form': form
	}
	return render(request, 'add_ip.html', context)


@login_required(login_url='login')
def view_details(request, pk):
	obj = Network.objects.get(id=pk)
	context = {
    	'object': obj
    }
	return render(request, "view.html", context)


@login_required(login_url='login')
def update_details(request, pk):
	template = 'update_details.html'
	obj = Network.objects.get(id=pk)
	form = NetworkForm(instance=obj)
	if request.method == "POST":
		form = NetworkForm(request.POST, instance=obj)
		if form.is_valid():
				form.save()
		return HttpResponseRedirect(reverse('home'))
	context = {
		'form': form
	}
	return render(request, template, context)


@login_required(login_url='login')
def delete_ip_address(request, pk):
	obj = Network.objects.get(id=pk)
	if request.method =="POST":
		obj.delete()
		return HttpResponseRedirect("/")
	context = {}
	return render(request, 'delete.html', {})



	
