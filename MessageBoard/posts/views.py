from django.shortcuts import render
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'