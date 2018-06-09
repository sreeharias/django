from django.shortcuts import render
from django.views.generic import ListView
from.import models
# Create your views here.



class HomePageView(ListView):
	model = models.post
	template_name="blog/post_list.html"

