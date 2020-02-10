from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse

# Create your views here.

class EntryList(ListView):
	template_name = 'base.html'
	model = Post


	def get(self, request):
		posts = Post.objects.all()
		return HttpResponse(posts)
		

class EntryDetail(DetailView):
	template_name = 'detail.html'
	
	queryset = Post.objects.all()
