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

# many many thanks to 
# https://github.com/zakx/openvpn-mgmt-webinterface/blob/master/openvpn_update.py

from backend.usercontrol.models import User, Record

import mgmtlib

def ovpn_update(Service):
    tn = mgmtlib.connect(Service)
    status = mgmtlib.get_status(tn)
    mgmtlib.quit(tn)
    status = mgmtlib.parse_status(status)
    print status['users']

    for u in status['users']:
        if u[0] == "UNDEF":
            continue # not yet connected

        try:
            user = User.objects.get(Username=u[0])
        except User.DoesNotExist:
            print "user does not exist"
            continue

        r = Record.objects.get(IP = u[1])
        r.BandwidthUp = int(u[3])
        r.BandwidthDown = int(u[4])
        try:
            r.save()
            print "done with user %s" % user.username
        except:
            print "couldn't save connection"
            continue
        
        # check bandwidth limits
        if user.Resource() > user.Plan.Bandwidth() and user.Plan.Bandwidth() > -1:
            tn = mgmtlib.connect()
            mgmtlib.send(tn, "kill %s" % u[1])
            mgmtlib.quit(tn)
            print "killed user %s for bandwidth usage" % user
