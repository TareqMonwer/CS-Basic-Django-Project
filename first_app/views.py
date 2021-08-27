from random import choice
from django.shortcuts import render

def index_view(request):
    fruits = ['Mango', 'Orange', 'BlueBerry']
    selected_fruit = choice(fruits)
    context = {
        'fruit': selected_fruit,
    }
    return render(request, "index.html", context)