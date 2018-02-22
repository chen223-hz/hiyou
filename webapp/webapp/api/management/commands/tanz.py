#coding:utf-8
# Last modified: 2016-08-19 16:04:34
# by zhangdi http://jondy.net/
from django.core.management.base import BaseCommand,CommandError 
from webapp.scenic.models import Dev,Scenic,Tanz,Client
from django.utils import timezone
from webapp.api.views import *
import datetime
import json
import time
import math
import requests
from django.core.cache import cache
from collections import Counter
from webapp.manuf.manuf import * 
import gc
class Command(BaseCommand):
  def handle(self, *args, **options):
    p = MacParser()
    try:
        today = datetime.datetime.today()
        yesterday = (today + datetime.timedelta(-1)).strftime('%Y%m%d')
        filename = '/home/www/hiyoutest/logs/tanz.log.' + yesterday + '.log'
        data = []
        listt = []
        for chunk in self.read_in_chunks(filename):
            for line in chunk:
                temp = {}
                try:
                    listt.append(eval(line)['macaddr'])
                    temp[eval(line)['mac']] = eval(line)
                    data.append(temp)
                except:
                    pass

        tanz = dict(Counter(listt))
        tquerysetlist = []
        for oo in Scenic.objects.all():
            objs = oo.dev_set.filter(dev_type='1',isonline=1)
            for ob in objs:
                temp = 0
                if tanz.has_key(ob.macaddr.lower()):
                    temp = tanz[ob.macaddr.lower()]
                tquerysetlist.append(Tanz(num=temp,mac=ob.macaddr,scenic=oo,create=yesterday))
        Tanz.objects.bulk_create(tquerysetlist)

        dic = {}
        for _ in data:
            for k, v in _.items():
                dic.setdefault(k, []).append(v)

        querysetlist=[]
        # print datetime.datetime.now(),len(dic)
        for key ,value in dic.items():
            sorted_x = sorted(value, key=lambda value : value['time'])
            #print sorted_x[0] 
            objs = Tanz.objects.filter(mac=sorted_x[0]['macaddr'].upper(),create=yesterday)
            if objs:
            	obj = objs[0] 
            maxxx = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(sorted_x[-1]['time']))
            minnn = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(sorted_x[0]['time']))
            maxx =datetime.datetime.strptime(maxxx, "%Y-%m-%d %H:%M:%S")
            minn =datetime.datetime.strptime(minnn, "%Y-%m-%d %H:%M:%S")

            #终端类型
            typ = self.mac_type(p,key)
            querysetlist.append(Client(tanz=obj,mac=key,num=len(value),endtime=maxx,
                statrtime=minn,typee=typ,scenic=obj.scenic))
        Client.objects.bulk_create(querysetlist)
        gc.collect()
    except Exception, e:
        gc.collect()
        print e

  def read_in_chunks(self,filePath, chunk_size=1024*1024*50):
    try:
        with open(filePath) as infile:
            while True:
                chunk_data = infile.read(chunk_size)
                if not chunk_data:
                    break
                yield chunk_data.split('\n')
    except:
        yield []

  def mac_type(self,p,key):
    typ = ''
    ty = p.get_manuf(key)
    comment = p.get_comment(key)
    if not comment: comment = 'null'
    if  ty:
        if 'HuaweiTe' in ty: typ = u'华为'
        elif 'OppoDigi' in ty or 'OPPO' in comment:
            typ = 'OPPO'
        elif 'VivoMobi' in ty or 'vivo' in comment:
            typ = 'vivo'
        elif 'XiaomiCo' in ty or 'XiaomiEl' in ty:
        	typ = u'小米'
        elif 'SamsungE' in ty: typ = u'三星'
        elif 'Zte' in ty: typ = u'中兴'
        elif 'Apple' in ty: typ = u'苹果'
        else: typ = ty
    return typ
