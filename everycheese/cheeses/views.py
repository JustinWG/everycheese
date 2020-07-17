
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Cheese
# Create your views here.

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese