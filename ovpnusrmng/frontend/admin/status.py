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
from django.db.models import Q, Count, Sum

import datetime

from backend.usercontrol.models import User, Record

from login import isAdmin, illegalAccess

def status(request):
    if not isAdmin(request): return illegalAccess()

    rs = Record.objects.filter(DisconnTime__isnull = True)

    now = datetime.datetime.now()
    MonthStart = datetime.date(now.year, now.month, 1)
    TodayStart = datetime.date(now.year, now.month, now.day)

    return render_to_response("admin-status.html",
        {
            'pageName': 'status',
            'records': rs,
            'now': datetime.datetime.now(),
            'todaybandwidth': Record.objects.filter(ConnTime__gte = TodayStart).aggregate(Resource=Sum("BandwidthUp"))["Resource"] + Record.objects.filter(ConnTime__gte = TodayStart).aggregate(Resource=Sum("BandwidthDown"))["Resource"],
            'thismonthbandwidth': Record.objects.filter(ConnTime__gte = MonthStart).aggregate(Resource=Sum("BandwidthUp"))["Resource"] + Record.objects.filter(ConnTime__gte = MonthStart).aggregate(Resource=Sum("BandwidthDown"))["Resource"]
        },
        context_instance=RequestContext(request))
