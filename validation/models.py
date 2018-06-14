# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

class Appliance(models.Model):
      name = models.CharField(u'Name', max_length = 50)
   
      def __unicode__(self):
	  return self.name


class ValidResult(models.Model):
      model = models.CharField(u'Model', max_length = 50)
      #date = models.CharField(u'Date', max_length = 50, default='2018-01-01')
      #start_date = models.DateField(default='2018-01-01', blank=True)
      #end_date = models.DateField(default='2018-01-01', blank=True)
      # validation value
      mse = models.DecimalField(max_digits=20, decimal_places=4)
      mabs = models.DecimalField(max_digits=20, decimal_places=4)
      energy = models.DecimalField(max_digits=4, decimal_places=4)
      acc = models.DecimalField(max_digits=4, decimal_places=4)
      precision = models.DecimalField(max_digits=4, decimal_places=4)
      recall = models.DecimalField(max_digits=4, decimal_places=4)
     
      # choice for learning method : supervised, semi-supervised and multi-task
      SUPER = 'SUPER'
      SEMI_SUPER = 'SEMi'
      MULTI = 'MULTI'
      LEARNING_TYPE = (
	(SUPER, 'Supervised Learning'), 
	(SEMI_SUPER, 'Semi-Supervised Learning'),
	(MULTI, 'Multi-Tasks Learning')
      )
      learniing_type = models.CharField(max_length = 30, choices = LEARNING_TYPE, default=SUPER)
     
      appliance = models.ForeignKey('Appliance', blank=True, null=True)

      def __unicode__(self):
	  return self.model

      
