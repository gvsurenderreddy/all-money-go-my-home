# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.template import loader,Context

from settings import SITENAME, SITEMOTTO

def homepage(request):
    t=loader.get_template("site-homepage.html")
    c=Context({
	    'SITENAME': SITENAME,
	    'SITEMOTTO': SITEMOTTO,
	})
    return HttpResponse(t.render(c))
