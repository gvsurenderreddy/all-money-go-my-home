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

from django.conf.urls.defaults import patterns, include, url

from login import login, logout
from status import status
from users import users_list, users_add, users_edit
from plans import plans_list, plans_add, plans_edit
from logs import logs_list

from api import kill

urlpatterns = patterns('',
    (r'^$', login),
    (r'^login$', login),
    
    (r'^status$', status),
    
    (r'^users$', users_list),
    (r'^users-add$', users_add),
    (r'^users-page-(\d+)$', users_list),
    (r'^users-edit-id-(\d+)$', users_edit),
    
    (r'^plans$', plans_list),
    (r'^plans-add$', plans_add),
    (r'^plans-edit-id-(\d+)', plans_edit),
    
    (r'^logs$', logs_list),

    (r'^api/kill/([a-zA-Z0-9]+)/([0-9:\.]+)', kill),
    #(r'^.*$', logout),
)
