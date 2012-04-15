from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def homepage(request):
    return render_to_response('homepage.html', {'is_logged_in': True, 'username' : 'mefallit'})

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('a.html', {'current_date': now})

def login(request):
    return render_to_response('homepage.html', {'is_logged_in': True , 'username' : 'mefallit'})

