#!/usr/bin/env python2
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

import sys

from frontend.api.openvpn import ovpn_connect, ovpn_verify

if len(sys.argv)<2:
    exit(126)

action = sys.argv[1]

action_table = { 
    'connect': ovpn_connect,
    'verify':  ovpn_verify,
        
    }

if action not in action_table:
    exit(125)

exit(action_table[action]())