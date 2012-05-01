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
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from backend.usercontrol.models import User

from login import isAdmin, illegalAccess
from forms import SearchUserForm, UserAddForm, UserForm

from settings import User_Pagesize
    
def users_list(request, page="1"):
    if not isAdmin(request): return illegalAccess()
    
    if request.POST.get("AnyField", None):
        q = User.objects.filter(Username__contains = request.POST.get("AnyField", None)) \
          | User.objects.filter(Comment__contains  = request.POST.get("AnyField", None)) \
          | User.objects.filter(Email__contains    = request.POST.get("AnyField", None)) \
          | User.objects.filter(Contact__contains  = request.POST.get("AnyField", None))
    else:
        q = User.objects.all()
        
    lst = Paginator(q, User_Pagesize)
    try:
        users = lst.page(page)
    except PageNotAnInteger:
        users = lst.page(1)
    except EmptyPage:
        users = lst.page(lst.num_pages)
    
    searchUserForm = SearchUserForm()
    
    return render_to_response("admin-user-list.html",
        {
            'pageName': 'users',
            'users': users,
            'userSearchForm': searchUserForm,
        },
        context_instance=RequestContext(request))

def users_edit(request, id="0"):
    if not isAdmin(request): return illegalAccess()
    
    try:
        user = User.objects.get(id = id)
    except:
        return illegalAccess()
        
    save_success = False
    if request.method == 'POST': 
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            u=form.save()
            save_success = True
    else:
        form = UserForm(instance = user)
    return render_to_response("admin-user-edit.html",
        {
            'pageName': 'users',
            'user': user,
            'form': form,
            'save_success': save_success,
        },
        context_instance=RequestContext(request))

def users_add(request):
    if not isAdmin(request): return illegalAccess()
    
    save_success = False
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            u=form.save()
            save_success = True
            return HttpResponseRedirect('users')
    else:
        form = UserForm()
    return render_to_response("admin-user-edit.html",
        {
            'pageName': 'users',
            'form': form,
            'save_success': save_success,
        },
        context_instance=RequestContext(request))
