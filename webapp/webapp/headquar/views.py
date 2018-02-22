#coding:utf-8
# Last modified: 2017-07-11 10:10:56
# by zhangdi http://jondy.net/
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .models import *
from .forms import *
from django.contrib import messages
import traceback
import json
from django.utils import timezone
from django.template import RequestContext
from webapp.agent.models import *
from webapp.scenic.models import *
from webapp.account.models import *
import xlwt
import StringIO
import datetime

def index(request):
  if Dev.objects.all().count():
    reat = Dev.objects.filter(isonline=1).count()/float(Dev.objects.all().count())
  else:
    reat = 0
  return render(request,'headquar/index.html',{
    'dev': {
            'link': '/headquar/dev/',
            'bgcolor': 'blue',
            'title':Dev.objects.all().count(),
            'label': u'设备总数',
            'img': '/static/img/content-no.png',
        },
    'agent': {
            'link': '/headquar/agent/',
            'bgcolor': 'green',
            'title':Agent.objects.all().count(),
            'label': u'代理商总数',
            'img': '/static/img/agent-sum.png',
        },
    'scenic': {
            'link': '#',
            'bgcolor': 'red',
            'title':Scenic.objects.all().count(),
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

def agent(request,tx=0):
  search = request.GET.get('search')
  month = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
  new_agent = 0
  new_list = []
  new = 0
  obj = Agent.objects.all()
  for o in obj:
    new_month = datetime.date(o.pub_date.year,o.pub_date.month,o.pub_date.day)
    if new_month >= month:
      new_list.append(o)
      new_agent +=1
  if tx:
    obj = new_list
    new = 1
  if search:
    obj = Agent.objects.filter(name__contains=search)
  return render(request,'headquar/agent.html',{
  	'obj':obj,
    'new':new,
    'search':search,
    'agent': {
      'link': '/headquar/agent/',
      'bgcolor': 'blue',
      'title':Agent.objects.all().count(),
      'label': u'代理商总数',
      'img': '/static/img/agent-sum.png',
    },
    'new_agent': {
      'link': '/headquar/new/agent/',
      'bgcolor': 'red',
      'title':new_agent,
      'label': u'本月新增代理商总数',
      'img': '/static/img/agent-add.png',
    },
  	})

def dev(request,tx=0):
  search = request.GET.get('search')
  obj = Dev.objects.all()
  dev_off = 0
  if tx:
    obj = Dev.objects.filter(isonline=0)
    dev_off = 1
  if search:
    obj = Dev.objects.filter(macaddr__contains=search)
  return render(request,'headquar/dev.html',{
    'obj':obj,
    'off':dev_off,
    'search':search,
    'dev': {
      'link': '/headquar/dev/',
      'bgcolor': 'blue',
      'title':Dev.objects.all().count(),
      'label': u'设备总数',
      'img': '/static/img/content-no.png',
    },
    'dev_off': {
      'link': '/headquar/off/dev/',
      'bgcolor': 'red',
      'title': Dev.objects.filter(isonline=0).count(),
      'label': u'离线设备总数',
      'img': '/static/img/content.png',
    },
    })


def add_agent(request,pk=0):
  if not pk:
    if request.method == 'POST':
      cellphone = request.POST.get('cellphone')
      name = request.POST.get('name')
      #p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
      #if not p.match(cellphone):
      if not name:
        messages.error(request, u'保存失败!名称不能为空!')
        return redirect('/headquar/agent/')
      if len(cellphone)!=11:
        messages.error(request, u'保存失败!手机账号不是11位数字!')
        return redirect('/headquar/agent/')
      if User.objects.filter(cellphone=cellphone):
        messages.error(request, u'保存失败!手机账户已存在!')
        return redirect('/headquar/agent/')
      if len(name) >96:
        messages.error(request, u'保存失败!代理商名超过32个字!')
        return redirect('/headquar/agent/')
      if Agent.objects.filter(name=name):
        messages.error(request, u'保存失败!代理商名已存在!')
        return redirect('/headquar/agent/')
      obj = Group.objects.filter(name=name)
      if not obj:
        obj = Group.objects.create(name=name,role=1)
      else:
        obj = obj.first()
      u = Agent.objects.create(name=name,gaent=obj)
      User.objects.create(cellphone=cellphone,group=obj)
      messages.success(request, u'保存成功!')
  else:
    obj = Agent.objects.get(pk=pk)
    if request.method == 'POST':
      name = request.POST.get('name')
      if not name:
        messages.error(request, u'保存失败!名称不能为空!')
        return redirect('/headquar/agent/')
      if len(name) >96:
        messages.error(request, u'保存失败!代理商名超过32个字!')
      if Agent.objects.filter(name=name):
        messages.error(request, u'保存失败!代理商名已存在!')
      else:
        obj.name = name
        obj.save()
        messages.success(request, u'修改成功!')
  return redirect('/headquar/agent/')

def agent_del(request,pk):
  obj = Agent.objects.get(pk=pk)
  if obj.dev_set.all().count()!=0:
    messages.error(request, u'删除失败！先删除关联的设备!')
    return redirect('/headquar/agent/')
  for o in obj.scenic_set.all():
    o.group.user_set.all().delete()
    o.region_set.all().delete()
    o.group.delete()
    o.delete()
  obj.gaent.user_set.all().delete()
  obj.gaent.delete()
  obj.delete()
  return redirect('/headquar/agent/')

def agent_user(request,pk=0):
  obj = Agent.objects.get(pk=pk).gaent.user_set.all()
  return render_to_response('headquar/agent_user.html', {
      'obj': obj,
      'pk':pk
    }, context_instance=RequestContext(request))

def agent_username(request,pk=0):
  obj = Agent.objects.get(pk=pk)
  if request.method == 'POST':
    cellphone = request.POST.get('cellphone')
    #p=re.compile('^0\d{2,3}\d{7,8}$|^1[3578]\d{9}$|^147\d{8}')
    #if not p.match(cellphone):
    if len(cellphone)!=11:
      messages.error(request, u'保存失败!手机账号不是11位数字!')
      return redirect('/headquar/'+pk+'/user/')
    if User.objects.filter(cellphone=cellphone):
      messages.error(request, u'保存失败!手机账户已存在!')
      return redirect('/headquar/'+pk+'/user/')
    User.objects.create(cellphone=cellphone,group=obj.gaent)
    messages.success(request, u'保存成功!')
  return redirect('/headquar/'+pk+'/user/')

def user_del(request,agent=0,pk=0):
  obj = User.objects.get(pk=pk)
  obj.delete()
  return redirect('/headquar/'+agent+'/user/')

def export(request,pk):
  response = HttpResponse(content_type='application/vnd.ms-excel')  
  response['Content-Disposition'] = 'attachment;filename=dev.xls'  
  wb = xlwt.Workbook(encoding = 'utf-8')  
  sheet = wb.add_sheet(u'设备')      
  sheet.write(0,0, u'设备MAC')
  sheet.write(0,1, u'代理商名字')
  sheet.write(0,2, u'所属景区')
  sheet.write(0,3, u'经纬度') 
  sheet.write(0,4, u'设备类型')
  sheet.write(0,5, u'在线状态')
  sheet.write(0,6, u'创建日期')        
  row = 1 
  obj = Dev.objects.all()
  ts = request.GET.get('search')
  if int(pk):
    obj = Dev.objects.filter(isonline=0)
  if ts and ts != 'None':
    obj = Dev.objects.filter(macaddr__contains=ts)
  if not obj:
    messages.error(request, u'导出失败！导出的无内容!')
    return redirect('/headquar/dev/')
  for usa in obj:  
    sheet.write(row,0, usa.macaddr)
    if usa.agent_dev:
      sheet.write(row,1, usa.agent_dev.name)
    else:
      sheet.write(row,1, '-')
    if usa.scenic_dev:
      sheet.write(row,2, usa.scenic_dev.name)
    else:
      sheet.write(row,2, '-') 
    sheet.write(row,3, usa.latitude) 
    sheet.write(row,4, usa.get_type())
    if usa.online_time: 
      sheet.write(row,5, usa.get_time())
    else:
      sheet.write(row,5, '-')  
    sheet.write(row,6,usa.pub_date.strftime('%Y-%m-%d %X')) 
    row=row + 1  
  output = StringIO.StringIO()  
  wb.save(output)  
  output.seek(0)  
  response.write(output.getvalue())  
  return response 

def agent_export(request,pk):
  response = HttpResponse(content_type='application/vnd.ms-excel')  
  response['Content-Disposition'] = 'attachment;filename=agent.xls'  
  wb = xlwt.Workbook(encoding = 'utf-8')  
  sheet = wb.add_sheet(u'代理商')      
  sheet.write(0,0, u'代理商名字')
  sheet.write(0,1, u'景区数量')
  sheet.write(0,2, u'账号数量') 
  sheet.write(0,3, u'设备数量')
  sheet.write(0,4, u'创建日期')        
  row = 1 
  ts = request.GET.get('search','')
  obj = Agent.objects.all()
  if int(pk):
    month = datetime.date(datetime.date.today().year,datetime.date.today().month,1)
    new_list = []
    for o in obj:
      new_month = datetime.date(o.pub_date.year,o.pub_date.month,o.pub_date.day)
      if new_month >= month:
        new_list.append(o)
    obj = new_list
  if ts and ts !='None':
    obj = Agent.objects.filter(name__contains=ts)
  if not obj:
    messages.error(request, u'导出失败！导出的无内容!')
    return redirect('/headquar/agent/')
  for usa in obj:  
    sheet.write(row,0, usa.name)
    sheet.write(row,1, usa.scenic_set.all().count()) 
    sheet.write(row,2, usa.gaent.user_set.all().count())   
    sheet.write(row,3, usa.dev_set.all().count()) 
    sheet.write(row,4, usa.pub_date.strftime('%Y-%m-%d %X')) 
    row=row + 1  
  output = StringIO.StringIO()  
  wb.save(output)  
  output.seek(0)  
  response.write(output.getvalue())  
  return response

def scenic_manage(request):
    obj = Facilities.objects.all()
    search = request.GET.get('search')
    if search:
        obj = Facilities.objects.filter(name=search)
    return render(request,'headquar/scenic.html',{
        'obj':obj,
        })


@csrf_exempt
def scenic_add(request):
    obj = Fenlei.objects.all()
    if request.method=='POST':
        point = request.POST.get('type')
        leixing = request.POST.get('leixing')
        map_icon = request.FILES.get('map_icon',None)
        list_icon = request.FILES.get('list_icon',None)
        obj = Facilities.objects.create(name=point,map_icon=map_icon,list_icon=list_icon,leixing=leixing)
        obj.get_img()
        return redirect('/headquar/scenic/')
    return render(request,'headquar/scenic_add.html',{'obj':obj,})

@csrf_exempt
def scenic_edit(request,pk):
    obj = Facilities.objects.get(pk=pk)
    obj2 = Fenlei.objects.all()
    if request.method=='POST':
        point = request.POST.get('type')
        leixing = request.POST.get('leixing')
        map_icon = request.FILES.get('map_icon',None)
        list_icon = request.FILES.get('list_icon',None)
        obj = Facilities.objects.get(pk=pk)
        obj.name = point
        obj.leixing = leixing
        obj.map_icon = map_icon
        obj.list_icon = list_icon
        obj.save()
        obj.get_img()
        return redirect('/headquar/scenic/')
    return render(request,'headquar/scenic_edit.html',{
        'obj':obj,
        'obj2':obj2,
        })

def scenic_delete(request,pk):
    obj = Facilities.objects.get(pk=pk)
    obj.delete()
    return redirect('/headquar/scenic/')
