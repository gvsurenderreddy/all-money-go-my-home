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

from backend.usercontrol.models import Plan

from login import isAdmin, illegalAccess
from forms import PlanForm

def plans_list(request):
    if not isAdmin(request): return illegalAccess()
    
    plans = Plan.objects.all()
    
    return render_to_response("admin-plan-list.html",
        {
            'pageName': 'plans',
            'plans': plans,
        },
        context_instance=RequestContext(request))

def plans_edit(request, id="0"):
    if not isAdmin(request): return illegalAccess()
    
    try:
        plan = Plan.objects.get(id = id)
    except:
        return illegalAccess()
        
    save_success = False
    if request.method == 'POST': 
        form = PlanForm(request.POST, instance = plan)
        if form.is_valid():
            u=form.save()
            save_success = True
    else:
        form = PlanForm(instance = plan)
    return render_to_response("admin-plan-edit.html",
        {
            'pageName': 'plans',
            'plan': plan,
            'form': form,
            'save_success': save_success,
        },
        context_instance=RequestContext(request))

def plans_add(request):
    if not isAdmin(request): return illegalAccess()
    
    save_success = False
    if request.method == 'POST': 
        form = PlanForm(request.POST)
        if form.is_valid():
            u=form.save()
            save_success = True
            return HttpResponseRedirect('plans')
    else:
        form = PlanForm()
    return render_to_response("admin-plan-edit.html",
        {
            'pageName': 'plans',
            'form': form,
            'save_success': save_success,
        },
        context_instance=RequestContext(request))
