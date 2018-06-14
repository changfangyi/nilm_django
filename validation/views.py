# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    intro = 'Here is a App for Validation \nIncluding:\nMSE, MABS, ACC, Precision, Recall\n Model name and type'
    return HttpResponse(intro)
