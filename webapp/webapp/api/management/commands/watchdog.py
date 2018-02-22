#coding:utf-8
# Last modified: 2016-08-19 16:04:34
# by zhangdi http://jondy.net/
from django.core.management.base import BaseCommand,CommandError 
from webapp.scenic.models import *
from webapp.api.views import *
import datetime
import json
import time

class Command(BaseCommand):
  def handle(self, *args, **options):
    while True:
      server = []
      for i in range(3):
        obj = Dev.objects.filter(dev_type=str(i))
        server = obj.values_list('macaddr', flat=True)
        #ap调用接口  
        if i == 0:
          dat = get_aus_status(list(server))
          self.get_status(dat,server)
        elif i== 1:
          dat = get_tz_status(list(server)) #探针接口
          self.get_status(dat,server)
        else:
          dat = get_auss_status(list(server)) #认证服务器接口
          self.get_status(dat,server)
      time.sleep(30)

  def get_status(self,dat,server):
    aus = []
    for au in dat['data']:
      dev_aus = eval(au)
      aus.append(dev_aus['mac'].upper())
      ta = None
      try:
        ta = Dev.objects.get(macaddr=dev_aus['mac'].upper())
      except:
        pass

      #ap和认证服务器的时间
      if dev_aus.has_key('time'):
        ta.online_time = time.mktime(dev_aus['time'].timetuple())
        if time.mktime(dev_aus['time'].timetuple())<(int(time.time())-50):
          ta.isonline =False
        else:
          ta.isonline =True

      #探针的时间
      if dev_aus.has_key('last'):
        ta.online_time = dev_aus['last']
        if int(dev_aus['last'])<(int(time.time())-50):
          ta.isonline = False
        else:
          ta.isonline = True
        ta.time_dev = dev_aus["first"]

      #在线时间
      if dev_aus.has_key('uptime'):
        ta.time_dev = dev_aus['uptime']

      #版本
      if dev_aus.has_key('version'):
        ta.version =dev_aus['version']
        
      #AP ssid  
      if dev_aus.has_key('ssid1'):
        ta.ssid=dev_mac['ssid1']

      ta.save()
    for h in Dev.objects.filter(macaddr__in=server).exclude(macaddr__in=aus):
      h.isonline =False
      h.save()
