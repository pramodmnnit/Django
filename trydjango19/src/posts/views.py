from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import post
from .forms import PostForm
def create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context_data = {
		"form": form
	}
	return render(request,"create.html",context_data)

def list(request):
	
	query_set = post.objects.all();
	context_data = {"object_all": query_set,"title":"List"}
	return render(request,"index.html",context_data)

def detail(request,id=None):
	instance = get_object_or_404(post,id=id)
	context_data = {"title" : instance.title,"instance" : instance}
	return render(request,"details.html",context_data)

def delete(request):
	return HttpResponse("delete")

def update(request,id=None):
	instance = get_object_or_404(post,id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context_data = {"title" : instance.title,"instance" : instance,"form":form}
	return render(request,"create.html",context_data)

# Create your views here.
