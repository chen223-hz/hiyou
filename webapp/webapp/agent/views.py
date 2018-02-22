#coding:utf-8
# Last modified: 2017-07-10 11:11:27
# by zhangdi http://jondy.net/
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .models import *
from .forms import *
from webapp.scenic.models import *
from webapp.account.models import *
from django.template import RequestContext
import traceback
import json
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import SESSION_KEY, HASH_SESSION_KEY 
import xlwt
import StringIO
import csv
import codecs
from webapp.scenic.wechat_open_callback import WXDCrypt
import requests
import time
import random
import string
import xmltodict
from django.core.cache import cache
from webapp.scenic.testapi import *
import os

@csrf_exempt
def sceneImgUpload(request):
    if request.method == 'POST':  
        callback = request.GET.get('CKEditorFuncNum')
        try: 
            path = "uploads/ckeditorimg/" + time.strftime("%Y%m%d%H%M%S",time.localtime())
            #path = os.path.dirname(path)
            #os.path.exists(path)
            #os.path.mkdirs(path)
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            for chunk in f.chunks():  
                des_origin_f.write(chunk)  
            des_origin_f.close()  
        except Exception, e:  
            print e  
        res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"  
        return HttpResponse(res)  


def index(request):
  obj = request.user
  objs = obj.group.agent_set.first()
  if objs.dev_set.all().count():
    reat = objs.dev_set.filter(isonline=1).count()/float(objs.dev_set.all().count())
  else:
    reat = 0
  account = 0
  for o in objs.scenic_set.all():
    account += o.group.user_set.all().count()
  return render(request,'agent/index.html',{
    'dev': {
          'link': '/agent/dev/',
          'bgcolor': 'blue',
          'title':objs.dev_set.all().count(),
          'label': u'设备总数',
          'img': '/static/img/content-no.png',
      },
    'account': {
          'link': '#',
          'bgcolor': 'red',
          'title':account,
          'label': u'账号总数',
          'img': '/static/img/id.png',
      },
    'scenic': {
          'link': '/agent/agent/',
          'bgcolor': 'green',
          'title':objs.scenic_set.all().count(),
          'label': u'景区总数',
          'img': '/static/img/scenic-count.png',
      },
    'dev_on': {
          'link': '#',
          'bgcolor': 'yellow',
          'title': str(int(reat*100))+'%',
          'label': u'设备在线率',
          'img': '/static/img/circle.png',
      },
  })

def agent(request,tx=None):
  obj = request.user
  objs = obj.group.agent_set.first()
  o = objs.scenic_set.all()
  new = 0
  month = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
  new_agent = 0
  new_list = []
  account = o.count()
  for oo in o:
    new_month = datetime.date(oo.pub_date.year,oo.pub_date.month,oo.pub_date.day)
    if new_month >= month:
      new_list.append(oo.pk)
      new_agent +=1
  if tx:
    o = Scenic.objects.filter(pk__in=new_list)
    new = 1
  search = request.GET.get('search')
  if search:
    o = objs.scenic_set.filter(name__contains=search)
  objss = Area.objects.filter(name='-')
  for obj in objss:
      obj.delete()
  objss = Point.objects.filter(name='-')
  for obj in objss:
      obj.delete()
  return render(request,'agent/agent.html',{
  	'objs':o,
    'new':new,
  	'pk':objs.pk,
    'search':search,
    'scenic': {
      'link': '/agent/agent/',
      'bgcolor': 'blue',
      'title':account,
      'label': u'景区总数',
      'img': '/static/img/scenic-count.png',
    },
    'new_scenic': {
      'link': '/agent/new/agent/',
      'bgcolor': 'red',
      'title':new_agent,
      'label': u'本月新增景区总数',
      'img': '/static/img/scenic-add.png',
    },
  })

def dev(request,tx=None):
  obj = request.user
  objs = obj.group.agent_set.first()
  ob = objs.dev_set.all()
  dev_off = 0
  if tx:
    ob = objs.dev_set.filter(isonline=0)
    dev_off = 1
  search = request.GET.get('search')
  if search:
    ob = objs.dev_set.filter(macaddr__contains=search)
  return render(request,'agent/dev.html',{
    'objs':ob,
    'off':dev_off,
    'pk':objs.pk,
    'search':search,
    'dev_off':objs.dev_set.filter(isonline=0).count(),
    'dev': {
      'link': '/agent/dev/',
      'bgcolor': 'blue',
      'title':objs.dev_set.all().count(),
      'label': u'设备总数',
      'img': '/static/img/content-no.png',
    },
    'dev_off': {
      'link': '/agent/off/dev/',
      'bgcolor': 'red',
      'title':objs.dev_set.filter(isonline=0).count(),
      'label': u'离线设备总数',
      'img': '/static/img/content.png',
    },
})

def scenic_add(request,agent=0,pk=0):
  if not pk:
    objss = Agent.objects.get(pk=agent)
    if request.method == 'POST':
      cellphone = request.POST.get('cellphone')
      name = request.POST.get('name')
      #p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
      #if not p.match(cellphone):
      if not name:
        messages.error(request, u'保存失败!名称不能为空!')
        return redirect('/agent/agent/')
      if len(cellphone)!=11:
        messages.error(request, u'保存失败!手机账号不是11位数字!')
        return redirect('/agent/agent/')
      if User.objects.filter(cellphone=cellphone):
        messages.error(request, u'保存失败!手机账户已存在!')
        return redirect('/agent/agent/')
      if len(name) >96:
        messages.error(request, u'保存失败!景区名超过32个字!')
        return redirect('/agent/agent/')
      if Scenic.objects.filter(name=name):
        messages.error(request, u'保存失败!景区名已存在!')
        return redirect('/agent/agent/')
      obj = Group.objects.get(pk=objss.gaent.pk)
      objs = obj.children.all()
      if objs:
        ob = objs.filter(name=name)
        if ob:
          o = ob.first()
        else:
          o = Group.objects.create(role=2,name=name,parent=obj)
      else:
        o = Group.objects.create(role=2,name=name,parent=obj)
      u = Scenic.objects.create(name=name,group=o,agent=objss)
      User.objects.create(cellphone=cellphone,group=o)
  else:
    obj = Scenic.objects.get(pk=pk)
    if request.method == 'POST':
      name = request.POST.get('name')
      if not name:
        messages.error(request, u'保存失败!名称不能为空!')
        return redirect('/agent/agent/')
      if len(name) >96:
        messages.error(request, u'保存失败!景区名超过32个字!')
      if Scenic.objects.filter(name=name):
        messages.error(request, u'保存失败!景区名已存在!')
      else:
        obj.name = name
        obj.save()
        messages.success(request, u'保存成功!')
  return redirect('/agent/agent/')
 
def scenic_setting(request,pk=0):
  u = Scenic.objects.get(pk=pk)
  mac = u.dev_set.filter(dev_type='2').first().macaddr
  u.mendian_name = ''
  u.authorizer_appid = Group.objects.get(role=0).scenic_set.first().authorizer_appid
  u.save()
  url = 'http://hiyou.doublecom.net/ausv/loginc/'
  wenjian = 'login.html'
  a = get_aus_update_file(url,wenjian,mac)
  url = 'http://hiyou.doublecom.net/ausv%s/login/'%u.pk
  wenjian = '/phone/login.html'
  a = get_aus_update_file(url,wenjian,mac)
  url = 'http://hiyou.doublecom.net/ausv%s/alogin/'%u.pk
  wenjian = '/phone/alogin.html'
  a = get_aus_update_file(url,wenjian,mac)
  url = 'http://hiyou.doublecom.net/ausvpc%s/login/'%u.pk
  wenjian = '/pc/login.html'
  a = get_aus_update_file(url,wenjian,mac)
  url = 'http://hiyou.doublecom.net/ausvpc%s/alogin/'%u.pk
  wenjian = '/pc/alogin.html'
  a = get_aus_update_file(url,wenjian,mac)
  url = 'http://hiyou.doublecom.net/ausv%s/rlogin/'%u.pk
  wenjian = 'rlogin.html'
  a = get_aus_update_file(url,wenjian,mac)
  messages.success(request,u'设置成功!')
  return redirect('/agent/agent/')

def scenic_user(request,pk=0):
  obj = Scenic.objects.get(pk=pk).group.user_set.all()
  return render_to_response('agent/scenic_user.html', {
      'obj': obj,
      'pk':pk
    }, context_instance=RequestContext(request))

def scenic_username(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if request.method == 'POST':
    cellphone = request.POST.get('cellphone')
    #p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    #if not p.match(cellphone):
    if len(cellphone)!=11:
      messages.error(request, u'保存失败!手机账号不是11位数字!')
      return redirect('/agent/'+pk+'/user/') 
    if User.objects.filter(cellphone=cellphone):
      messages.error(request, u'保存失败!手机账户已存在!')
      return redirect('/agent/'+pk+'/user/') 
    User.objects.create(cellphone=cellphone,group=obj.group)
    messages.success(request, u'保存成功!')
  return redirect('/agent/'+pk+'/user/')	

def user_del(request,agent=0,pk=0):
  obj = User.objects.get(pk=pk)
  obj.delete()
  return redirect('/agent/'+agent+'/user/')

def scenic_del(request,pk):
  obj = Scenic.objects.get(pk=pk)
  if obj.dev_set.all().count()!=0:
    messages.error(request, u'删除失败！先删除关联的设备!')
    return redirect('/agent/agent/')
  obj.region_set.all().delete()
  obj.group.user_set.all().delete()
  obj.delete()
  return redirect('/agent/agent/')

@csrf_exempt
def dev_add(request, pk=0, op=0):
  obj = Agent.objects.get(pk=pk)
  if request.method=='POST':
    data =[]
    temp = {}
    if int(op):
      p = Scenic.objects.get(pk=op)
      for o in p.region_set.all():
        temp['name'] = o.name
        temp['pk'] = o.pk
        data.append(temp)
        temp = {}
    data = {'data':data}
    return HttpResponse(json.dumps(data))
  return render(request,'agent/dev_add.html', {
      'obj': obj,
      'pk':pk,
    })
  
@csrf_exempt
def region(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  objs = Facilities.objects.all()
  objss = obj.point_set.all()
  obja = obj.area_set.all()
  objq = obj.area_set.filter(zhu=True)
  if request.method =='POST':
      marker = request.POST.getlist('marker[]')
      marker = [float(item) for item in marker]
      val = request.POST.get('type')
      ba = request.POST.get('ba')
      name = request.POST.get('name')
      objs = Facilities.objects.get(pk=val)
      objss = Point.objects.get(pk=ba)
      objss.latitude = marker
      objss.facilities_point = objs
      objss.name = name
      objss.save()
      objs.get_img()
      return HttpResponse(str(objs.map_icon))
  return render_to_response('agent/region.html', {
      'obj': obj,
      'objs':objs,
      'objss':objss,
      'obja':obja,
      'objq':objq,
    }, context_instance=RequestContext(request))


@csrf_exempt
def label(request,pk=0):
    obj = Scenic.objects.get(pk=pk)
    if request.method == 'POST':
        obj = Point.objects.create(scenic_point=obj)
        return HttpResponse(obj.pk)

@csrf_exempt
def dellabel(request,pk=0):
    obj = Scenic.objects.get(pk=pk)
    if request.method == 'POST':
        ba = request.POST.get('ba')
        objss = Point.objects.get(pk=ba)
        objss.delete()
        return HttpResponse('')

@csrf_exempt
def area(request,pk=0):
    obj = Scenic.objects.get(pk=pk)
    objs = obj.area_set.all()
    if request.method =='POST':
        marker = request.POST.get('marker')
        val = request.POST.get('type')
        ba = request.POST.get('ba')
        name = request.POST.get('name')
        objs = Area.objects.get(pk=ba)
        objss = Area.objects.filter(zhu="1")
        if val == "1" and not objss:
            objs.zhu = True
            objs.name = name
            objs.latitude = marker
            objs.save()
            return HttpResponse('ok')
        if val == "1" and objss:
            return HttpResponse('error')
        else:
            objs.name = name
            objs.latitude = marker
            objs.save()
    return HttpResponse('')

@csrf_exempt
def arealabel(request,pk=0):
    obj = Scenic.objects.get(pk=pk)
    if request.method == 'POST':
        obj = Area.objects.create(scenic_area=obj)
    return HttpResponse(obj.pk)

@csrf_exempt
def delarea(request,pk=0):
    if request.method == 'POST':
        ba = request.POST.get('ba')
        obj = Area.objects.get(pk=ba)
        obj.delete()
        obj = Area.objects.filter(zhu=True)
        if obj:
            return HttpResponse('1')
        else:
            return HttpResponse('0')

@csrf_exempt
def area_manage(request,pk=0):
    obj = Point.objects.get(pk=pk)
    objs = obj.scenic_point
    if request.method == 'POST':
        img = request.FILES.get('imgfile',None)
        video = request.FILES.get('videofile',None)
        text = request.POST.get('text')
        if img:
            obj.image = img
        if video:
            obj.video = video
        if text:
            obj.text = text
        obj.save()
        return redirect('/agent/'+str(objs.pk)+'/region/')
    return render_to_response('agent/point_add.html', {
        'obj':obj,
        'objs':objs,
        'pk':pk,
  }, context_instance=RequestContext(request))


@csrf_exempt
def point_name(request,pk=0):
    if request.method =='POST':
        ba = request.POST.get('ba')
        obj = Point.objects.get(pk=ba)
        if obj.facilities_point:
            data = []
            temp = {}
            temp['pk'] = obj.facilities_point.pk
            temp['name'] = obj.name
            data.append(temp)
            data = {'data':data}
            return HttpResponse(json.dumps(data))
        data = []
        temp = {}
        temp['pk'] = 'gg'
        data.append(temp)
        data = {'data':data}
        return HttpResponse(json.dumps(data))

def save_dev(request,pk=0):
  objs = Agent.objects.get(pk=pk)
  if request.method=='GET':
    data =[]
    temp = {}
    tx = request.GET.get('id')
    oo = Scenic.objects.get(pk=int(tx))
    for p in oo.region_set.all():
      temp['name'] = p.name
      temp['pk'] = p.pk
      data.append(temp)
      temp = {}
    data = {'data':data}
    return HttpResponse(json.dumps(data))
  else:
    mac = request.POST.get('mac').upper()
    typ = request.POST.get('type')
    region = request.POST.get('region')
    scenic = request.POST.get('scenic')
    remarks = request.POST.get('remarks')
    if not mac:
      messages.error(request, u'MAC不能为空!')
      return redirect('/agent/'+pk+'/dev_add/')
    if Dev.objects.filter(macaddr=mac):
      messages.error(request, u'保存失败！设备已存在!')
      return redirect('/agent/'+pk+'/dev_add/')
    if int(scenic):
      ob = Scenic.objects.get(pk=int(scenic))
    else:
      ob = None
    if int(region):
      o = Region.objects.get(pk=int(region))
    else:
      o = None
    obj = Dev.objects.create(macaddr=mac,
      dev_type=typ,scenic_dev=ob,region_dev=o,
      agent_dev=objs,remarks=remarks)
  return redirect('/agent/dev/')	

def export(request,pk=0,off=0):
  response = HttpResponse(content_type='application/vnd.ms-excel')  
  response['Content-Disposition'] = 'attachment;filename=agent_dev.xls'  
  wb = xlwt.Workbook(encoding = 'utf-8')  
  sheet = wb.add_sheet(u'设备')      
  sheet.write(0,0, u'设备MAC')
  sheet.write(0,1, u'所属景区')
  sheet.write(0,2, u'所属区域')
  sheet.write(0,3, u'经纬度') 
  sheet.write(0,4, u'设备类型')
  sheet.write(0,5, u'在线状态')
  sheet.write(0,6, u'创建日期')        
  row = 1 
  ts = request.GET.get('search')
  obj = Agent.objects.get(pk=pk)
  objs = obj.dev_set.all()
  if int(off):
    objs = obj.dev_set.filter(isonline=0)
  if ts and ts != 'None':
    objs = obj.dev_set.filter(macaddr__contains=ts)
  if not objs:
    messages.error(request, u'导出失败！导出的无内容!')
    return redirect('/agent/dev/')
  for usa in objs:  
    sheet.write(row,0, usa.macaddr)
    if usa.scenic_dev:
      sheet.write(row,1, usa.scenic_dev.name)
    else:
      sheet.write(row,1, '-')
    if usa.region_dev:
      sheet.write(row,2, usa.region_dev.name)
    else:
      sheet.write(row,2, '-')  
    sheet.write(row,3, usa.latitude)
    sheet.write(row,4, usa.get_type())
    if usa.online_time: 
      sheet.write(row,5, usa.get_time())
    else:
      sheet.write(row,5, '-')
    sheet.write(row,6, usa.pub_date.strftime('%Y-%m-%d %X')) 
    row=row + 1  
  output = StringIO.StringIO()  
  wb.save(output)  
  output.seek(0)  
  response.write(output.getvalue())  
  return response 

def scenic_export(request,pk=0,new=0):
  response = HttpResponse(content_type='application/vnd.ms-excel')  
  response['Content-Disposition'] = 'attachment;filename=scenic.xls'  
  wb = xlwt.Workbook(encoding = 'utf-8')  
  sheet = wb.add_sheet(u'景区')      
  sheet.write(0,0, u'景区名字')
  sheet.write(0,1, u'区域数量')
  sheet.write(0,2, u'账号数量') 
  sheet.write(0,3, u'设备数量')
  sheet.write(0,4, u'创建日期')        
  row = 1 
  ts = request.GET.get('search')
  obj = Agent.objects.get(pk=pk)
  objs = obj.scenic_set.all()
  if int(new):
    month = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
    new_list = []
    for oo in objs:
      new_month = datetime.date(oo.pub_date.year,oo.pub_date.month,oo.pub_date.day)
      if new_month >= month:
        new_list.append(oo)
    objs = new_list
  if ts and ts != 'None':
    objs = obj.scenic_set.filter(name__contains=ts)
  if not obj:
    messages.error(request, u'导出失败！导出的无内容!')
    return redirect('/agent/agent/')
  for usa in objs:  
    sheet.write(row,0, usa.name)
    sheet.write(row,1, usa.region_set.all().count()) 
    sheet.write(row,2, usa.group.user_set.all().count())   
    sheet.write(row,3, usa.dev_set.all().count()) 
    sheet.write(row,4, usa.pub_date.strftime('%Y-%m-%d %X')) 
    row=row + 1  
  output = StringIO.StringIO()  
  wb.save(output)  
  output.seek(0)  
  response.write(output.getvalue())  
  return response 

@csrf_exempt
def dev_import(request,pk=0):
  if request.method=='POST':
    name = request.FILES['file'].name
    if 'csv' not in name:
      return HttpResponse('no')
    filename= '/tmp/file_name%s.csv' % os.getpid()
    print filename
    of = open(filename, 'wb')
    for chunk in request.FILES['file'].chunks():
      of.write(chunk)
    of.close()
    file = open(filename, 'r')
    f = file.readlines()
    f.sort()
    oldline=''
    k=1
    for newline in f:
      c = newline.split(',')
      if (c[0]==oldline)and(k!=1):
        os.remove(filename)
        return HttpResponse(c[0])
      else:
        oldline=c[0]
        k+=1
    objs = Agent.objects.get(pk=pk)
    obj = objs.dev_set.all()
    i=0
    for x in f:
      i+=1
      if i>1000:
        os.remove(filename)
        return HttpResponse('100')
      p = x.split(',')
      t = isMac(p[0])
      o = is_type(p[1])
      if not t or not o:
        os.remove(filename)
        return HttpResponse(i)
      for b in obj:
        if p[0] == b.macaddr:
          os.remove(filename)
          return HttpResponse(p[0])
    for j in f:
      b = j.split(',')
      if b[1] in ['AP\r\n','ap\r\n','Ap\r\n','aP\r\n','AP\r\n','ap\n','Ap\r\n','aP\r\n']:
        typ = 0
      else:
        typ = 1 
      oo = b[0].upper()
      Dev.objects.create(macaddr=oo,dev_type=typ,agent_dev=objs)
    f.close()
    os.remove(filename)
    return HttpResponse('ok')
  return render_to_response('agent/import.html', {
    'pk':pk
  }, context_instance=RequestContext(request))

def dev_edit(request,pk=0,dev_pk=0):
  o = Dev.objects.get(pk=dev_pk)
  obj = Agent.objects.get(pk=pk)
  objs =None
  if o.scenic_dev:
    objs = o.scenic_dev.region_set.all()
  if request.method == 'POST':
    typ = request.POST.get('type')
    region = request.POST.get('region')
    scenic = request.POST.get('scenic')
    remarks = request.POST.get('remarks')
    if int(scenic):
      ob = Scenic.objects.get(pk=int(scenic))
    else:
      ob = None
    if int(region):
      p = Region.objects.get(pk=int(region))
    else:
      p = None
    o.dev_type = typ
    o.scenic_dev = ob
    o.region_dev = p
    o.remarks = remarks
    o.save()
    return redirect('/agent/dev/')
  return render_to_response('agent/dev_edit.html', {
    'pk':pk,
    'o': o,
    'obj':obj,
    'objs':objs
  }, context_instance=RequestContext(request))

def dev_del(request,pk):
  obj = Dev.objects.get(pk=pk)
  obj.delete()
  return redirect('/agent/dev/')

def isMac(addr):
  #if isinstance(addr, unicode): return False
  if not addr: return False
  if not re.match(r'^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$',addr):
    return False
  return True

def is_type(tx):
  if not tx: return False
  if tx in ['\xcc\xbd\xd5\xeb\n','\xcc\xbd\xd5\xeb\r\n']:
    return True
  if tx  in ['AP\r\n','ap\r\n','Ap\r\n','aP\r\n','AP\r\n','ap\n','Ap\r\n','aP\r\n']:
    return True
  else:
    return False

@csrf_exempt
def agent_map(request,pk=0,re_pk=0):
  obj = Scenic.objects.get(pk=pk)
  objs = Region.objects.get(pk=re_pk)
  if request.method == 'POST':
    lis = request.POST.getlist('lis')
    data =[]
    temp = {}
    latitud = []
    if lis[0]:
      objs.latitude = lis
      objs.save()
      latitude = lis[0].split('A')
      for oo in latitude[:-1]:
        latitud.append(eval(oo))
    else:
      if objs.latitude:
        latitude = eval(objs.latitude)[0].split('A')
        for oo in latitude[:-1]:
          latitud.append(eval(oo))
    for ob in obj.region_set.all():
      temp['name'] = ob.name
      temp['pk'] = ob.pk
      data.append(temp)
      temp = {}
    data = {'data':data,'latitude':latitud}
    return HttpResponse(json.dumps(data))
  return render_to_response('agent/agent_map.html', {
      'obj': obj,
      'objs':objs,
      'pk':re_pk
    }, context_instance=RequestContext(request))

@csrf_exempt
def scenic_map(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  lng = ''
  lat = ''
  if obj.latitude:
    latitude = eval(obj.latitude)[0].split('A')
    for oo in latitude[:-1]:
      lng = lng +str(eval(oo)['lng'])+','+str(eval(oo)['lat'])+';'
      lat = 'lat'
  else:
    for oob in obj.region_set.all():
      if oob.latitude:
        latitude = eval(oob.latitude)[0].split('A')
        for oo in latitude[:-1]:
          lng = lng +str(eval(oo)['lng'])+','+str(eval(oo)['lat'])+';'
  if request.method == 'POST':
    lis = request.POST.getlist('lis')
    name =  request.POST.get('name')
    data =[]
    temp = {}
    if name:
      if obj.region_set.filter(name=name):
        return HttpResponse(json.dumps({'dat':'No'}))
      else:
        if not len(lis):
          lis = None
        objs = Region.objects.create(name=name,latitude=lis,scenic_region=obj)
        data = {'dat':objs.pk}
        return HttpResponse(json.dumps(data))
    else:
      return HttpResponse(json.dumps({'dat':'none'}))
  return render_to_response('agent/add_map.html', {
      'pk':pk,
      'obj':obj,
      'lng':lng,
      'lat':lat,
    }, context_instance=RequestContext(request))  

def su(request,agent_pk=0, pk=0,tx=None):  
  user = User.objects.get(pk=pk)
  if not user.wechatUNID:
    messages.error(request, u'此号还没有开通!')
    if tx=='agent':
      return redirect('/headquar/'+agent_pk+'/user/')
    else:
      return redirect('/agent/'+agent_pk+'/user/')
  request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
  session_auth_hash = user.get_session_auth_hash() 
  request.session[HASH_SESSION_KEY] = session_auth_hash 
  return redirect('/'+tx+'/')

@csrf_exempt
def scenic_mapp(request,pk):
  objs = Scenic.objects.get(pk=pk)
  obj = objs.area_set.filter(zhu='1')
  if request.method == 'POST':
    lis = request.POST.get('lis')
    data =[]
    temp = {}
    latitud = []
    print 'list:',lis
    if eval(lis):
      if obj:
        obj.first().latitude = lis
        print 'lis:',lis
        obj.first().save()
      else:
        Area.objects.create(name=objs.name,zhu='1',latitude=eval(lis),scenic_area=objs)
      for oo in eval(lis):
        latitud.append(oo)
    else:
      print 'obj'
      if obj:
        if obj.first().latitude:
          print obj.first().latitude
          latitude = eval(obj.first().latitude)
          for oo in latitude:
            print 'latitud:',oo
            latitud.append(oo)
    data = {'latitude':latitud}
    return HttpResponse(json.dumps(data))
  return render_to_response('agent/scenic_map.html', {
      'obj': obj,
      'pk':pk
    }, context_instance=RequestContext(request))  

def scenic_d(request,pk):
  objs = Scenic.objects.get(pk=pk)
  obj = objs.area_set.filter(zhu='1').delete()
  return redirect('/agent/'+pk+'/scenic_map/')


def location(request):
  mac = request.GET.get('mac')
  app_id = 'wx0c569c12f6127bc0'
  secret = 'e5bd86f68b6eb6eb647db507ae16d11b'
  url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(app_id,secret)
  r = json.loads(requests.get(url).content)
  access_token= r['access_token']
  url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi'%access_token
  r = json.loads(requests.get(url).content)
  ticket = r['ticket']
  sign = Sign(ticket, 'http://hiyou.doublecom.net/location/?mac='+mac)
  
  return render(request,'agent/location.html',{
    'sign':sign.sign(),
    'mac':mac
    })  


def check_signature(signature, timestamp, nonce, token):
  L = [timestamp, nonce, token]
  L.sort()
  try:
    s = L[0] + L[1] + L[2]
  except:
    s = ''
  return hashlib.sha1(s).hexdigest() == signature

class Sign:
  def __init__(self, jsapi_ticket, url):
    self.ret = {
        'nonceStr': self.__create_nonce_str(),
        'jsapi_ticket': jsapi_ticket,
        'timestamp': self.__create_timestamp(),
        'url': url
    }

  def __create_nonce_str(self):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

  def __create_timestamp(self):
    return int(time.time())

  def sign(self):
    string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
    print string
    self.ret['signature'] = hashlib.sha1(string).hexdigest()
    return self.ret


@csrf_exempt
def wechat(request):
  echostr = request.GET.get('echostr')
  signature = request.GET.get('signature')
  timestamp = request.GET.get('timestamp')
  nonce = request.GET.get('nonce')
  openid = request.GET.get('openid')
  token = 'hiyoushijie'
  app_id = 'wx0c569c12f6127bc0'
  secret = 'e5bd86f68b6eb6eb647db507ae16d11b'
  url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'%(app_id,secret)
  r = json.loads(requests.get(url).content)
  access_token= r['access_token']
  ur = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s"%access_token
  data = {
     "button":[
      {
           "name":"caidan",
           "sub_button":[
           {  
               "type":"view",
               "name":"ding_dev",
               "url":"http://hiyou.doublecom.net/mac/"
            },
          ]
      }]
  }
  r = requests.post(ur, json.dumps(data))
  if not check_signature(signature, timestamp, nonce, token):
    return HttpResponse('ZnVjayB5b3Uh')
  if check_signature(signature, timestamp, token, openid):
    return True
  # 这是公众平台接入认证
  if echostr:
    return HttpResponse(echostr)

def coordinate(request):
  lat = request.GET.get('lat').encode("utf-8") 
  lng = request.GET.get('lng').encode("utf-8") 
  mac = request.GET.get('mac')
  return render(request,'agent/coordinate.html',{
    'lng':float(lng),
    'lat':float(lat),
    'mac':mac
    })

@csrf_exempt
def macc(request):
  r=request.body
  convertedDict = xmltodict.parse(r);
  jsonStr = json.dumps(convertedDict);
  url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx65423a2f6908bc55&secret=3aad35233c0a762172f38b8f1d92630f'
  response = requests.get(url).content
  access_token = eval(response)['access_token']
  ul = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=%s'%access_token
  data = {
      "touser": eval(jsonStr)['xml']['openid'],
      "template_id": "0LDiwV_T8K1rndofUEaLJw1yiQHUJb0KkrdiMNhB6Rg",       
      "form_id": cache.get('prepay_id'),
      "page": "pages/myticket/myticket",
      "data": {
          "keyword1": {
              "value": eval(jsonStr)['xml']['time_end'], 
              "color": "#173177"
          },
          "keyword2": {
              "value": u"成人票", 
              "color": "#173177"
          }, 
          "keyword3": {
              "value": str(int(eval(jsonStr)['xml']["total_fee"])/100.0)+'元', 
              "color": "#173177"
          }, 
          "keyword4": {
              "value": eval(jsonStr)['xml']["out_trade_no"], 
              "color": "#173177"
          }
      },
      "emphasis_keyword": "keyword3.DATA" 
    }
  r = requests.post(ul, json.dumps(data)).content
  print r
  return HttpResponse('SUCCESS')

@csrf_exempt
def mac(request):
  if request.method=='POST':
    mac = request.POST.get('mac')
    if Dev.objects.filter(macaddr=mac):
      return HttpResponse('ok')
    else:
      return HttpResponse('no')
  else:
    return render(request,'agent/mac.html')

def mac_location(request):
  lng = request.GET.get('lng')
  lat = request.GET.get('lat')
  mac = request.GET.get('mac')
  obj = Dev.objects.filter(macaddr=mac)
  if obj:
    obj.first().latitude=str(lng)+','+str(lat)
    obj.first().save()
    messages.success(request, u'保存成功!')
    return redirect('/mac/')

def dev_latiude(request,pk,tx):
  obj = Dev.objects.get(pk=pk)
  if obj.latitude =='-':
    messages.error(request, u'没有坐标!')
    return redirect('/'+tx+'/dev/')
  else:
    return render(request,tx+'/dev_latiude.html',{
      'obj':obj,
    })

@csrf_exempt
def pay(request):
  code = request.GET.get('code')
  moy = request.GET.get('amount')
  ur = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx65423a2f6908bc55&secret=3aad35233c0a762172f38b8f1d92630f&js_code=%s&grant_type=authorization_code'%code
  response = json.loads(requests.get(ur).content)
  data = {'appid' :'wx65423a2f6908bc55','body' : 'test','mch_id' :'1442784802'}
  data['notify_url']  = 'https://hiyoutest.doublecom.net/macc/'
  data['out_trade_no']  = time.strftime("%Y%m%d%H%M%s", time.localtime())+str(random.randint(0, 100))
  data['spbill_create_ip']  = request.META['HTTP_X_FORWARDED_FOR']
  data['total_fee']  = int(float(moy)*100)
  data['trade_type']  = 'JSAPI'
  data['openid'] = response['openid']
  sign = Sign(data)
  tt = sign.sign()
  data = tt
  url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
  xml = []
  for k in sorted(data.keys()):
    v = data.get(k)
    if k == 'detail' and not v.startswith('<![CDATA['):
      v = '<![CDATA[{}]]>'.format(v)
    xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
  temp = '<xml>{}</xml>'.format(''.join(xml))
  r = requests.post(url, data=temp).content
  convertedDict = xmltodict.parse(r);
  jsonStr = json.dumps(convertedDict);
  prepay_id = 'prepay_id='+eval(jsonStr)['xml']['prepay_id']
  cache.set('prepay_id',eval(jsonStr)['xml']['prepay_id'],60*20)
  print "---",prepay_id
  da = {'appId':'wx65423a2f6908bc55','timeStamp':str(int(time.time())),'package':prepay_id,'signType':'MD5'}
  sin = Sign(da)
  return HttpResponse(json.dumps(sin.sign()))

class Sign:
  def __init__(self,data):
    self.ret = data
    if len(data)==4:
      self.ret['nonceStr']=self.__create_nonce_str()
    else:
      self.ret['nonce_str']=self.__create_nonce_str()

  def __create_nonce_str(self):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

  def __create_timestamp(self):
    return int(time.time())

  def sign(self):
    st = '&'.join(['%s=%s' % (key, self.ret[key]) for key in sorted(self.ret)])+'&key=192006250b4c09247ec02edce69f6a2d'
    if len(self.ret)==5:
      self.ret['paySign'] = hashlib.md5(st.encode('utf-8')).hexdigest().upper()
    else:
      self.ret['sign'] = hashlib.md5(st.encode('utf-8')).hexdigest().upper()
    return self.ret

@csrf_exempt
def dev_lng(request,pk=0):
  lng = request.POST.get('lng')
  obj = Dev.objects.get(pk=pk)
  obj.latitude = lng
  obj.save()
  return HttpResponse('ok')