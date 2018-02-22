#coding:utf-8
# Last modified: 2016-08-19 16:04:34
# by zhangdi http://jondy.net/
from django.core.management.base import BaseCommand,CommandError 
from webapp.scenic.models import Dev,Scenic,Area
from django.utils import timezone
from webapp.api.views import *
import datetime
import json
import time
import math
from django.core.cache import cache
import os  
import re   
import sys 
from collections import Counter
import requests

domain = 'dev.api.doublecom.net'

scenic_api_url = 'http://%s/api/scenic' % domain

# def worker(*args, **kwargs):
#   pk = args[0]
#   obj = Scenic.objects.get(pk=pk)

#   while True:
#     lng_str = []
#     objs = obj.dev_set.filter(dev_type='1',isonline=1)
#     if not objs:
#       break
#     obj.area_set.all().update(num = 0)
#     dataa = []
#     for ob in objs:
#       data = get_tz_clients(ob.macaddr)
#       cache.set(ob.macaddr,data['data'],30)
#       if len(data['data']):
#         for o in data['data']:
#           if o:
#             temp = {}
#             tempp = eval(o)
#             tempp['tanzmac'] = ob.macaddr 
#             temp[eval(o)['mac']] = tempp
#             dataa.append(temp)

#     #list相同key组合
#     dic = {}
#     for _ in dataa:
#         for k, v in _.items():
#             dic.setdefault(k, []).append(v)

#     #遍历终端共有的探针
#     coout = 0
#     for key ,value in dic.items():
#       if len(value) >= 3:
#         coout = coout +1
#         listt = []
#         latitude =[]
#         sorted_x = sorted(value, key=lambda value : value["signal"])
#         for oo in sorted_x[:3]:
#           objj = Dev.objects.get(macaddr=oo['tanzmac'])
#           if objj.latitude != '-':
#             tem = {}
#             tem['x'] = float(objj.latitude.split(',')[0])
#             tem['y'] = float(objj.latitude.split(',')[1])
#             tem['signal'] = oo['signal']
#             latitude.append(tem)
#         if len(latitude) == 3:
#           latitude_x = sorted(latitude, key=lambda latitude : latitude["x"])
#           #探针1
#           x1 = latitude_x[2]['x']
#           y1 = latitude_x[2]['y']
#           a = latitude_x[2]['signal']
#           #探针2
#           x2 = latitude_x[1]['x']
#           y2 = latitude_x[1]['y']
#           b = latitude_x[1]['signal'] 
#           #探针3
#           x3 = latitude_x[0]['x']
#           y3 = latitude_x[0]['y']
#           c = latitude_x[0]['signal']

#           #探针距离一米的信号值         
#           param = 52

#           #计算坐标点
#           a = pow(10,(abs(a)-param)/(10*2.4))/111000.0
#           b = pow(10,(abs(b)-param)/(10*2.4))/111000.0      
#           c = pow(10,(abs(c)-param)/(10*2.4))/111000.0
#           p = pow(x1,2)-pow(x3,2)+pow(y1,2)-pow(y3,2)+pow(c,2)-pow(a,2)
#           e = pow(x2,2)-pow(x3,2)+pow(y2,2)-pow(y3,2)+pow(c,2)-pow(b,2)
#           lat_y = (e/2*(x1-x3)-p/2*(x2-x3))/((y2-y3)*(x1-x3)-(y1-y3)*(x2-x3))
#           lng_x = (p/2-(y1-y3)*lat_y)/(x1-x3)

#           #面积为4平方的中心坐标
#           nu = 2
#           lat_nu = y1 -(((int((max([y1,y2,y3])-lat_y)*111000/nu)+1)*nu)-nu/2.0)/111000.0
#           lng_nu = x1 - (((int((x1-lng_x)*111000/nu)+1)*nu)-nu/2.0)/111000.0

#           #判断坐标是否在区域nei
#           for bj in obj.area_set.filter(zhu='0'):
#               latitud = []
#               if bj.latitude:
#                 latitude = eval(bj.latitude)
#                 for oo in latitude:
#                   latitud.append(oo)
#               if isInsidePolygon({'lat':lat_y,'lng':lng_x}, latitud):
#                 bj.num = bj.num +1
#                 bj.save()
#           lng_str.append(str(lng_nu)+','+str(lat_nu))
#     #统计每一个格子里的终端数      
#     da = []
#     cliant = dict(Counter(lng_str))
#     for key ,value in cliant.items():
#       tem = {}
#       tem['lng'] = key.split(',')[0]
#       tem['lat'] = key.split(',')[1]
#       tem['count'] = value
#       da.append(tem)
#     da = {'accoun':coout,'data':da}
#     obj.probe = da
#     obj.save()  
#     time.sleep(10)
  
def isInsidePolygon(p, poly):
  px = p['lng']
  py = p['lat']
  flag = False
  for i in range(len(poly)):
    if i==0: j=len(poly)-1
    else:
      if i==(len(poly)-1): j=i-1
      else: j=i-1
    sx = poly[i]['lng']
    sy = poly[i]['lat']
    tx = poly[j]['lng']
    ty = poly[j]['lat']
    if((sx == px and sy == py) or (tx == px and ty == py)):
      return True
    if((sy < py and ty >= py) or (sy >= py and ty < py)):
      x = sx + (py - sy) * (tx - sx) / (ty - sy)
      if x == px:return True
      if(x > px):
        if flag: flag = False
        else: flag = True
  return flag

def call_api(url, data):
    r = requests.post(url, json.dumps(data))
    try:
      return json.loads(r.content)
    except Exception, e:
      return {'data':[]}


def get_scenic(mac):
    ''' 获取终端地理位置，参数为mac的地理位置字典'''
    data = {
        'action': 'getlist',
        'macaddr': mac
    }
    return call_api(scenic_api_url, data)

class Command(BaseCommand):
  def handle(self, *args, **options):
    while True:
      lng_str = []
      obj = Scenic.objects.filter(isdel=0)
      for objs in obj:
        objs.area_set.all().update(num = 0)
        data = {}
        for _obj in objs.dev_set.filter(dev_type='1',isonline=1,isdel=0):
          #探针终端数据
          _oo = get_tz_clients(_obj.macaddr)
          cache.set(_obj.macaddr,_oo['data'],20)
          if _obj.latitude != '-':
            data[_obj.macaddr] = _obj.latitude.split(',')
        _data = get_scenic(data)

        #判断坐标是否在区域nei
        for latlng in _data['data']: 
          for _obj in objs.area_set.filter(zhu='0'):
              latitud = []
              if _obj.latitude:
                latitude = eval(_obj.latitude)
                for oo in latitude:
                  latitud.append(oo)
              if isInsidePolygon({'lat':latlng['lat'], 'lng':latlng['lng']} , latitud):
                _obj.num = _obj.num +1
                _obj.save()
          lng_str.append(str(latlng['lng']) + ',' + str(latlng['lat']) + ',' + latlng['mac'])
        
        #统计每一个格子里的终端数      
        #da = []
        cliant = dict(Counter(lng_str))
        for _key ,value in cliant.items():
          tem = {'lng':_key.split(',')[0], 'lat':_key.split(',')[1],'count':value}
          #da.append(tem)
          key = str(objs.pk)+ ':' + _key.split(',')[2]
          cache.set(key,tem,60*2)
        #da = {'accoun':len(_data['data']),'data':da}
        cache.set(str(objs.pk)+'account',len(_data['data']),60*2)
        #objs.probe = da
        #objs.save() 
        time.sleep(20)
