# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from validation.models import Appliance, ValidResult

admin.site.register(Appliance)
admin.site.register(ValidResult) 
