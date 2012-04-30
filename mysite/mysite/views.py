from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def homepage(request):
    return render_to_response('homepage.html', {'is_logged_in': False, 'username' : 'mefallit', "item_list" : [ {'item_name': "Lorem ipsum", 'username' : 'mefallit', 'is_logged_in': False, 'userId' : "123789", 'entry_list' : [ { "round": "1", "text" : "laylaylay", "eUserName" : "mefallit", "date" : "11.02.2012", "eUserId" : "123789"}, { "round": "2", "text" : "olalala", "eUserName" : "baturay", "date" : "11.04.2012", "eUserId" : "12345"}]},
{'item_name': "Dolor sit amet", 'username' : 'mefallit', 'is_logged_in': False, 'userId' : "123789", 'entry_list' : [ { "round": "1", "text" : "laylaylay", "eUserName" : "mefallit", "date" : "11.02.2012", "eUserId" : "123789"}, { "round": "2", "text" : "olalala", "eUserName" : "baturay", "date" : "11.04.2012", "eUserId" : "12345"}]},
{'item_name': "Naber", 'username' : 'mefallit', 'is_logged_in': False, 'userId' : "123789", 'entry_list' : [{ "round": "1", "text" : "laylaylay", "eUserName" : "mefallit", "date" : "11.02.2012", "eUserId" : "123789"}, { "round": "2", "text" : "olalala", "eUserName" : "baturay", "date" : "11.04.2012", "eUserId" : "12345"}]}]})

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('a.html', {'current_date': now})

def login(request):
    return render_to_response('homepage.html', {'is_logged_in': True, 'username' : 'mefallit'})

def item(request):
    return render_to_response('homepage.html', {'is_logged_in': True, 'username' : 'mefallit', "item_list" : [ {'item_name': "Lorem ipsum", 'username' : 'mefallit', 'is_logged_in': False, 'userId' : "123789", 'entry_list' : [ { "round": "1", "text" : "laylaylay", "eUserName" : "mefallit", "date" : "11.02.2012", "eUserId" : "123789"}, { "round": "2", "text" : "olalala", "eUserName" : "baturay", "date" : "11.04.2012", "eUserId" : "12345"}]}]})


def register(request):
    return render_to_response('register.html', {'is_logged_in': False})
