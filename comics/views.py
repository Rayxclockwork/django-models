from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class EntryList(ListView):
	template_name = 'home.html'

class EntryDetail(DetailView):
	template_name = 'detail.html'
