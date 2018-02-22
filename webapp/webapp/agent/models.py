#coding:utf-8
# Last modified: 2016-06-27 13:01:26
# by zhangdi http://jondy.net/
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
import datetime
import json
from webapp.account.models import *

class Agent(models.Model):
  name =models.CharField(u'代理商名称', max_length=512,blank=True, null=True)
  username =models.CharField(u'手机账号', max_length=512,blank=True, null=True)
  isdel = models.BooleanField(default=False)
  pub_date = models.DateTimeField(auto_now_add=True, editable = True)
  update_time = models.DateTimeField(auto_now=True, null=True)
  latitude = models.CharField(max_length=512, null=True,blank=True, default='-')
  gaent = models.ForeignKey(Group,null=True)

  class Meta:
    ordering = ['-id']

