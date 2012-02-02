# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader,Context, RequestContext

from backend.usercontrol.models import User

from forms import LoginForm, RegisterForm
from base import joinbase


def login(request):
    if request.method == 'POST': 
	form = LoginForm(request.POST)
	# set session
	try:
	    U=User.objects.get(Username=form['Username'].value(), Password=form['Password'].value())
	    request.session['Username'] = u.Username
	    return HttpResponseRedirect('/user')
	except User.DoesNotExist:
	    return HttpResponse("Not Exist")
    else:
	form = LoginForm()
	c=joinbase({
		'form': form
	})
	return render_to_response("site-login.html",
	    c,
	    context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST': 
	form = RegisterForm(request.POST)
        if form.is_valid():
	    u=form.save()
	    request.session['Username'] = u.Username
	    return HttpResponseRedirect('/user')
	else:
	    return HttpResponse("Invalid")
    else:
	form = RegisterForm()
	c=joinbase({
		'form': form
	})
	return render_to_response("site-register.html",
	    c,
	    context_instance=RequestContext(request))