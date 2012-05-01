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

from django import forms
from django.db import models
from django.contrib import admin

import datetime

class User(models.Model):
    Username = models.CharField(max_length = 100, unique = True)
    Password = models.CharField(max_length = 20)
    Email = models.EmailField()
    Plan = models.ForeignKey("Plan", null = True, blank = True)
    Contact = models.CharField(max_length = 200, blank = True)
    Comment = models.CharField(max_length = 200, blank = True)
    Credit = models.IntegerField(default = 0)		# in CNY
    Banned = models.BooleanField(default = False)

    def __unicode__(self):
        return self.Username
        
    def Resource(self):                                 # in bytes
        ax = 0
        rs = Records.objects.filter(User = self) # TODO: Only this accounting period (month)
        for itemx in rs:
            ax += itemx.Bandwidth()
        return ax
        
admin.site.register(User)
        
class Plan(models.Model):
    Title = models.CharField(max_length = 100,unique = True)
    Bandwidth = models.BigIntegerField()
    Connection = models.IntegerField()
    Hidden = models.BooleanField()

    def __unicode__(self):
        return self.Title
        
admin.site.register(Plan)
        
class Record(models.Model):
    User = models.ForeignKey('User')
    Service = models.CharField(max_length = 20)
    ConnTime = models.DateTimeField(auto_now_add = True)
    DisconnTime = models.DateTimeField(null = True, blank = True)
    IP = models.CharField(max_length = 39) 	# IPAddressField doesn't support IPv6 Addresses
    BandwidthUp = models.BigIntegerField(null = True, blank = True)
    BandwidthDown = models.BigIntegerField(null = True, blank = True)
    
    def Duration(self):
        if self.DisconnTime:
            return self.DisconnTime - self.ConnTime
        return datetime.datetime.now() - self.ConnTime
    
    def Bandwidth(self):
        return self.BandwidthUp + self.BandwidthDown
    
admin.site.register(Record)
