# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader,Context, RequestContext

from backend.usercontrol.models import User

from forms import LoginForm, RegisterForm
from base import joinbase


def login(request):
    errmsg=""
    form = LoginForm()
    if request.method == 'POST': 
	form = LoginForm(request.POST)
	try:
	    U=User.objects.get(Username=form['Username'].value(), Password=form['Password'].value())
	    request.session['Username'] = u.Username
	    return HttpResponseRedirect('/user')
	except User.DoesNotExist:
	    errmsg = "Wrong login or password."
    c=joinbase({
	    'form': form,
	    'errmsg': errmsg,
    })
    return render_to_response("site-login.html",
	c,
	context_instance=RequestContext(request))

def register(request):
    errmsg=""
    form = RegisterForm()
    if request.method == 'POST': 
	form = RegisterForm(request.POST)
        if form.is_valid():
	    u=form.save()
	    request.session['Username'] = u.Username
	    return HttpResponseRedirect('/user')
	else:
	    errmsg = "Invalid Info"
    c=joinbase({
	    'form': form,
	    'errmsg': errmsg,
    })
    return render_to_response("site-register.html",
	c,
	context_instance=RequestContext(request))