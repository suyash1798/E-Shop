from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text_var = 'This is my'
    return HttpResponse(text_var)
