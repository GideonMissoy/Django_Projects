from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'