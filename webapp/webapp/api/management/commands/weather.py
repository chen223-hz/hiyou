#coding:utf-8
# Last modified: 2016-08-19 16:04:34
# by zhangdi http://jondy.net/
from django.core.management.base import BaseCommand,CommandError 
from webapp.scenic.models import Dev,Scenic
from django.utils import timezone
from webapp.api.views import *
import datetime
import json
import time
import math
import requests
from django.core.cache import cache


class Command(BaseCommand):
  def handle(self, *args, **options):
    while True:
        for obj in Scenic.objects.filter(isdel=0):
            if obj.point_set.all().first():
                if obj.point_set.first().latitude:
                    lng,lat = eval(obj.point_set.first().latitude)
                    url = 'https://api.seniverse.com/v3/weather/now.json?key=nrja0f2hhtadrvq7&location=%s'%(str(lat)+':'+str(lng))
                    r = requests.get(url)
                    try:
                        cache.set(str(obj.pk)+'t',eval(r.content)['results'][0]['now'],30*60)
                        cache.set(str(obj.pk)+'time',eval(r.content)['results'][0]['last_update'],30*60)
                    except:
                        pass

        time.sleep(30*60)
  

