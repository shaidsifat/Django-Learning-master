from django.shortcuts import render

# Create your views here.

from Blog.models import Blog

from django.views.generic import ListView

class Blogview(ListView):

    
    #queryset = Blog.objects.get(Id=1)
    model = Blog
    template_name = 'Home/index.html'




