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

import datetime

from login import isAdmin, illegalAccess

from backend.openvpn.kill import kill as ovpn_kill

from backend.usercontrol.models import Record

def kill(request, Service, IP):
    if not isAdmin(request): return illegalAccess()

    ovpn_kill(IP, Service)
    
    r = Record.objects.filter(IP = IP, DisconnTime__isnull = True)[0]
    r.DisconnTime = datetime.datetime.now()
    r.save()
    return HttpResponseRedirect('/manage/status')
