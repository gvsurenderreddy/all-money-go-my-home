# -*- coding: utf8 -*-
# Copyright 2012 by multiple1902 <multiple1902@gmail.com>
# http://code.google.com/p/all-money-go-my-home/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#    
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader,Context, RequestContext

from backend.usercontrol.login import try_login

from forms import LoginForm, RegisterForm
from base import joinbase


def login(request):
    errmsg=""
    form = LoginForm()
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if try_login(Username=form['Username'].value(), Password=form['Password'].value()):
            request.session['Username'] = form['Username'].value()
            return HttpResponseRedirect('/user')
        else:
            errmsg = "Wrong login or password."
            form = LoginForm()
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
            errmsg = "Some fields should be corrected."
    c=joinbase({
            'form': form,
            'errmsg': errmsg,
    })
    return render_to_response("site-register.html",
        c,
        context_instance=RequestContext(request))
        

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')