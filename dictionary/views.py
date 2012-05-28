from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from models import Item,User

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        items = Item.objects.filter(itemTitle__icontains=q)
        return render_to_response('includes/search_results.html',
            {'items': items, 'query': q})
    else:
        return render_to_response('homepage.html', {'error': True})


def login(request):
	c = {}
	c.update(csrf(request))
	m = User.get_object(username__exact=request.POST['username'])
	if m.password == request.POST['password']:
	        request.session['member_id'] = m.id
	        return render_to_response('homepage.html', {'is_logged_in': True}, c)
	else:
        	return HttpResponse("Your username and password didn't match.")

