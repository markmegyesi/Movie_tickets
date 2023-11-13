from django.shortcuts import render
from django.views.generic import ListView
from .models import MovieModel


class HomeView(ListView):
    model = MovieModel
    template_name = 'shop/index.html'
    context_object_name = 'movies'

