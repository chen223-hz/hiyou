#coding:utf-8
import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from webapp.scenic.models import *
import datetime
import time
import random
import string
import json
import requests
from django.core.cache import cache
from django.shortcuts import render

domain = 'dev.api.doublecom.net'

aus_api_url = 'http://%s/api/aus' % domain
rosap_api_url = 'http://%s/api/wrtap' % domain
tz_api_url = 'http://%s/api/tz' % domain

def agent_mac(request):
  mac = request.GET.get('mac')
  data = get_aus_status([mac])
  objs = Dev.objects.get(macaddr=mac)
  da =[]
  if len(data['data']):
    timee = eval(data['data'][0])
    objs.time_dev = timee['uptime']
    if timee.has_key('version'):
      objs.version =timee['version']
    objs.online_time = timee['time']
    timee['time'] = ''
    tim = int(timee['uptime'])
    day = tim/(24*3600)
    shour = tim%(24*3600)/3600
    sminute = tim%(24*3600)%3600/60
    timee['uptime'] =str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'
    da.append(timee)
  else:
    objs.isonline =False
  objs.save()
  return HttpResponse(json.dumps(da))

def dev_reboot(request):
  mac = request.GET.get('mac')
  data = rosap_reboot(mac)
  return HttpResponse('ok')

def dev_set(request,pk,tx):
  mac = request.GET.get('mac')
  ssid= request.GET.get('ssid')
  obj = Scenic.objects.get(pk=pk)
  if tx=='ap':
    data = rosap_setssid(mac,ssid)
  objs = Dev.objects.get(macaddr=mac)
  objs.ssid = ssid
  objs.save()
  return HttpResponse('ok')

def probe(request):
  mac = request.GET.get('mac')
  data = get_tz_status([mac])
  objs = Dev.objects.get(macaddr=mac)
  da =[]
  if len(data['data']):
    timee = eval(data['data'][0])
    objs.online_time = timee['last']
    objs.time_dev = timee['first']
    timee['uptime'] = time_dev(objs) 
    da.append(timee)
  else:
    objs.isonline =False
  objs.save()
  return HttpResponse(json.dumps(da))

def aus_mac(request):
  mac = request.GET.get('mac')
  data = get_auss_status([mac])
  objs = Dev.objects.get(macaddr=mac)
  da =[]
  if len(data['data']):
    timee = eval(data['data'][0])
    objs.online_time = time.mktime(timee['time'].timetuple())
    objs.time_dev = timee['uptime'] 
    timee['time'] = ''
    da.append(timee)
  else:
    objs.isonline =False
  objs.save()
  return HttpResponse(json.dumps(da))

@csrf_exempt
def scenic(request,pk):
  obj = Scenic.objects.get(pk=pk)
  objs = obj.area_set.all().order_by('-num')
  data = []
  if len(objs)>=3:
    for ob in objs[:3]:
      temp = {}
      temp['name'] = ob.name
      temp['num'] = ob.num
      data.append(temp)
  if len(objs)==2:
    for ob in objs:
      temp = {}
      temp['name'] = ob.name
      temp['num'] = ob.num
      data.append(temp)
    data.append({'name':u'无','num':0})
  if len(objs)==1:
    data.append({'name':objs.first().name,'num':objs.first().num})
    data.append({'name':u'无','num':0})
    data.append({'name':u'无','num':0})
  if len(objs)==0:
    data.append({'name':u'无','num':0})
    data.append({'name':u'无','num':0})
    data.append({'name':u'无','num':0})
  _data = []
  key = str(obj.pk)+':*'
  _keys = cache.keys(key)
  if _keys:
    for _mac in _keys:
      _data.append(cache.get(_mac))
  data = {'data':_data,'num':data,'account':cache.get(str(pk)+'account')}
  return HttpResponse(json.dumps(data))

def time_dev(objs):
  tim = time.mktime(datetime.datetime.now().timetuple())-int(objs.online_time)
  day = tim/(24*3600)
  shour = tim%(24*3600)/3600
  sminute = tim%(24*3600)%3600/60
  return str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'

def call_api(url, data):
    r = requests.post(url, json.dumps(data))
    try:
      return json.loads(r.content)
    except Exception, e:
      return {'data':[]}

def get_aus_status(mac):
    ''' 获取设备状态，参数为mac地址列表'''
    data = {
        'action': 'getlist',
        'macaddr': mac
    }
    return call_api(rosap_api_url, data)


def rosap_reboot(mac):
    '''通知ap设备重启，参数mac地址'''
    data = {
        'action': 'reboot',
        'macaddr': mac
    }
    return call_api(rosap_api_url, data)

def rosap_setssid(mac,ssid):
    '''通知ap设备重启，参数mac地址'''
    data = {
        'action': 'set_wireless_ssid',
        'macaddr': mac,
        'ssid': ssid
    }
    return call_api(rosap_api_url, data)

def get_tz_clients(mac):
    ''' 获取探针设备状态，参数为mac地址列表'''
    data = {
        'action': 'clients',
        'macaddr': mac
    }
    return call_api(tz_api_url, data)

def get_tz_status(mac):
    ''' 获取探针设备状态，参数为mac地址列表'''
    data = {
        'action': 'getlist',
        'macaddr': mac
    }
    return call_api(tz_api_url, data)

def get_auss_status(mac):
    ''' 获取设备状态，参数为mac地址列表'''
    data = {
        'action': 'getlist',
        'macaddr': mac
    }
    return call_api(aus_api_url, data)

def map(request):
  return render(request, 'api/map.html')

@csrf_exempt
def add_map(request):
  if request.method == 'POST':
    lis = request.POST.getlist('lis')
    data =[]
    temp = {}
    latitud = []
    if lis:
      cache.set('latitude',lis,60*60*24)
      latitude = lis[0].split('A')
      for oo in latitude[:-1]:
        latitud.append(eval(oo))
    else:
      cache.set('latitude',[],60*60*24)
    data = {'latitude':latitud}
    return HttpResponse(json.dumps(data))

@csrf_exempt
def map_date(request):
  lis = cache.get('latitude')
  latitud = []
  if lis:
    latitude = lis[0].split('A')
    for oo in latitude[:-1]:
      latitud.append(eval(oo))
  data = {'latitude':latitud}
  return HttpResponse(json.dumps(data))

def line(request):
  lis = cache.get('latitude')
  latitud = []
  print lis
  if lis:
    latitude = lis[0].split('A')
    for oo in latitude[:-1]:
      latitud.append(eval(oo))
  data = {'latitude':latitud}
  return HttpResponse(json.dumps(data))
