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

from forms import LoginForm

from settings import ADMINPASSWORD


def login(request):
    errmsg=""
    form = LoginForm()
    if request.method == 'POST': 
	form = LoginForm(request.POST)
	if ADMINPASSWORD==form['Password'].value():
	    request.session['Admin'] = True
	    return HttpResponseRedirect('/manage/status')
	else:
	    return illegalAccess
    return render_to_response("admin-login.html",
	{
	    'form': form,
	},
	context_instance=RequestContext(request))

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')
    
def isAdmin(request):
    try:
	return request.session['Admin']
    except:
	return False
	
def illegalAccess():
    return HttpResponseRedirect('http://www.people.com.cn/')