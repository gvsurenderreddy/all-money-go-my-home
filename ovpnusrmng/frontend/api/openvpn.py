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

from backend.usercontrol.login import try_login_openvpn
from backend.usercontrol.models import User, Record
from backend.log.user import connect, disconnect, update

import os, sys, datetime

def ovpn_connect():
    ''' creates an entry '''
    env_username = os.environ.get("common_name")
    if not env_username:
        env_username = os.environ.get("username")
    env_remote_ip = os.environ.get("trusted_ip")
    env_remote_port = os.environ.get("trusted_port")
    IP = "%s:%s" % (env_remote_ip, env_remote_port)
    connect(env_username, "VPN", IP)

def ovpn_disconnect():
    ''' edits an entry '''
    env_username = os.environ.get("common_name")
    if not env_username:
        env_username = os.environ.get("username")
    env_remote_ip = os.environ.get("trusted_ip")
    env_remote_port = os.environ.get("trusted_port")
    IP = "%s:%s" % (env_remote_ip, env_remote_port)
    env_bytes_recv = os.environ.get("bytes_received")
    env_bytes_sent = os.environ.get("bytes_sent")
    disconnect(env_username, "VPN", IP, env_bytes_sent, env_bytes_recv)

def ovpn_verify():
    ''' verification only '''
    env_username = os.environ.get("common_name")
    if not env_username:
        env_username = os.environ.get("username")
    env_password = os.environ.get("password")

    if try_login_openvpn(env_username, env_password):
        return 0
    else:
        return 1
