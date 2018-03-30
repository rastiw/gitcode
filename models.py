from django.db import models


from __future__ import unicode_literals
from django.forms import ModelForm
from random import randint
import random,string

# Create your models here.


class Options(models.Model):
	OptionChoices =(
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
	)	
		
	Option = models.CharField(max_length=2, blank=True, null=True,choices = OptionChoices)
	Description = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return u'%s \n %s '% (self.Option, self.Description)

class Indexes(models.Model):
	
	Index = models.ManyToManyField('Key',blank=True)	
	V = models.IntegerField(blank=True, null=True)
	Name = models.CharField(max_length=50, blank=True, null=True)
    Ns = models.CharField(max_length=50,  blank=True, null=True)
	def __unicode__(self):
		return u'%s \n %s '% (self.Index)
		


class Key(models.Model):
	
		
	Id = models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		return u'%s \n %s '% (self.Id)
		
