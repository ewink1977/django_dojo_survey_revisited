from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    print('RANDOM WORD APP INDEX REQUESTED')
    random_gibberish = get_random_string(length=14)
    context = {
        'gibberish' : random_gibberish
    } 
    return render(request, 'index.html', context)

