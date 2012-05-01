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

from backend.usercontrol.models import User, Record, Plan
import datetime

def connect(Username, Service, RemoteIP):
    user = User.objects.get(Username = Username)
    r = Record(User = user, 
            Service = Service,
            IP = RemoteIP,
            BandwidthUp = 0,
            BandwidthDown = 0,
            )
    r.save()

def disconnect(Username, Service, RemoteIP, BytesTx, BytesRx):
    user = User.objects.get(Username = Username)
    r = Record.objects.get(User = user, Service = Service, IP = RemoteIP)
    r.BandwidthUp = BytesRx
    r.BandwidthDown = BytesTx
    r.DisconnTime = datetime.datetime.now()
    r.save()

def update(User, RemoteIP, BytesTx, BytesRx):
    user = User.objects.get(Username = Username)
    r = Record.objects.get(User = user, Service = Service, IP = RemoteIP)
    r.BandwidthUp = BytesRx
    r.BandwidthDown = BytesTx
    r.save()
