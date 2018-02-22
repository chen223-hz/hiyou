#coding:utf-8
# Last modified: 2017-09-07 14:02:38
# by zhangdi http://jondy.net/
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.template import Template, Context, loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from .models import *
from .forms import *
import traceback
import sys
import json
from django.utils import timezone
import xlwt
import random
import requests
from .wechat_open_callback import WXDCrypt
import os
import datetime,time
from .testapi import *
from .tasks import *
from datetime import timedelta
from django.utils.timezone import now
from lxml import etree
from .wx import *
from webapp.manuf.manuf import * 
import os,base64
import StringIO

@csrf_exempt
def index(request,pk=0):
  obj = request.user
  objs = obj.group.scenic_set.first()
  if request.method == 'POST':
    tt = []
    ob = Scenic.objects.get(pk=pk)
    oo = ob.area_set.filter(zhu='1')
    if oo:
      if oo.first().latitude:
        latitude = eval(oo.first().latitude)
        for o in latitude:
          tt.append(o)
    data = {'tt':tt}
    return HttpResponse(json.dumps(data))
  return render(request,'scenic/index.html',{
    'obj':objs,
    'account':0
  })

def check_signature(signature, timestamp, nonce, token):
  L = [timestamp, nonce, token]
  L.sort()
  try:
    s = L[0] + L[1] + L[2]
  except:
    s = ''
  return hashlib.sha1(s).hexdigest() == signature

@csrf_exempt
def wechat(request):
  echostr = request.GET.get('echostr')
  openid = request.GET.get('openid')
  signature = request.GET.get('signature')
  timestamp = request.GET.get('timestamp')
  nonce = request.GET.get('nonce')
  token = 'hiyoushijie'
  return HttpResponse(echostr)


@csrf_exempt
def eventmessage(request,tx):
  r = request.body
  encodingAESKey = 'SMP0h6VMmWKwPVTdn9pj9oAM7XDvmT3HbjyaX3gpJVQ'+'='
  decrypt_test = WXDCrypt(encodingAESKey)
  xml = decrypt_test.decrypt(r)
  return HttpResponse('')


@csrf_exempt
def weixin_callback(request):
  signature = request.GET.get('signature')
  timestamp = request.GET.get('timestamp')
  nonce = request.GET.get('nonce')
  msg_sign = request.GET.get('msg_signature')
  #print >> sys.stderr, request.body
  token = 'haiyoushijie'
  encodingAESKey = 'SMP0h6VMmWKwPVTdn9pj9oAM7XDvmT3HbjyaX3gpJVQ'+'='
  decrypt_test = WXDCrypt(encodingAESKey)
  decrypt_test.appid = 'wxd9103590a61f46e0'
  decrypt_test.appsecret = '88f159fdeff76f0f04b05da6e98fd40c'
  (ticket ,val) = decrypt_test.get_ticket(request.body)
  if val == 'c':
    access_token = decrypt_test.get_access_token(ticket)
    pre_code = decrypt_test.get_pre_auth_code(access_token)
    try:
      with open(settings.CONFIG2) as infile:
        config = json.load(infile)
    except:
      print traceback.print_exc()
      return HttpResponse('success')
    config.setdefault('wechat', {})
    config['wechat']['ticket_value'] = ticket.strip()
    config['wechat']['access_token'] = access_token.strip()
    config['wechat']['pre_auth_code'] = pre_code.strip()
    with open(settings.CONFIG2, "w") as outfile:
      json.dump(config, outfile, indent=4)
    return HttpResponse('success')
  else:
    if ticket  == 'unauthorized':
      appid = decrypt_test.get_appid(request.body)
      obj = Scenic.objects.filter(authorizer_appid=appid).last()
      obj.authorizer_appid = ''
      obj.mendian_name = ''
      obj.save()
      return HttpResponse('success')


def wechat3pt(request):
  try:
    with open(settings.CONFIG2) as infile:
      config = json.load(infile)
    access_token = config.get("wechat",{}).get("access_token")
    ticket_value = config.get("wechat",{}).get("ticket_value")
    url = 'https://api.weixin.qq.com/cgi-bin/component/api_component_token?'+access_token
    data = {
        "component_appid":"wxd9103590a61f46e0" ,
        "component_appsecret": "88f159fdeff76f0f04b05da6e98fd40c", 
        "component_verify_ticket": ticket_value,
      }
    r = requests.post(url, json.dumps(data))
    access_token = eval(r.content)['component_access_token']
    config['wechat']['access_token'] = access_token.strip()
    url = 'https://api.weixin.qq.com/cgi-bin/component/api_create_preauthcode?component_access_token='+access_token
    data = {
        "component_appid":"wxd9103590a61f46e0" 
        }
    r =  requests.post(url, json.dumps(data))
    pre_auth_code = eval(r.content)['pre_auth_code']
    config['wechat']['pre_auth_code'] = pre_auth_code.strip()
    with open(settings.CONFIG2, "w") as outfile:
      json.dump(config, outfile, indent=4)
    if request.user.group.role == 0:
      if not Scenic.objects.filter(group=request.user.group):
        obj = Scenic.objects.create(group=request.user.group)
      else:
        obj = Scenic.objects.get(group=request.user.group)
        if not obj.mendian_name:
          obj.authorizer_appid = ''
          obj.isdel = False
          obj.save()
          return render_to_response('scenic/wechat3pt.html', {
            'var_pre_auth_code': config.get("wechat",{}).get("pre_auth_code"),
            }, context_instance=RequestContext(request))
        else:
          get_token(obj)
          datenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
          date = (datetime.datetime.now()+datetime.timedelta(-1)).strftime('%Y-%m-%d')
          url = 'https://api.weixin.qq.com/bizwifi/statistics/list?access_token='+obj.authorizer_access_token
          data = {
              "begin_date": date,
              "end_date": datenow,
              "shop_id":-1,
              }
          r = requests.post(url, json.dumps(data))
          people = eval(r.content)['data'][0]['total_fans']
          people2 = eval(r.content)['data'][0]['new_fans']
          return render_to_response('scenic/guanli.html', {
            'var_pre_auth_code': config.get("wechat",{}).get("pre_auth_code"),
            'people':people,
            'people2':people2,
            'head_img':obj.head_img,
            'nick_name':obj.nick_name,
            'mendian_name':obj.mendian_name,
            }, context_instance=RequestContext(request))
    else:
      obj = request.user.group.scenic_set.first()
      if not obj.mendian_name:
        obj.authorizer_appid = ''
        obj.isdel = False
        obj.save()
        return render_to_response('scenic/wechat3pt.html', {
          'var_pre_auth_code': config.get("wechat",{}).get("pre_auth_code"),
          }, context_instance=RequestContext(request))
      else:
        get_token(obj)
        datenow = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        date = (datetime.datetime.now()+datetime.timedelta(-1)).strftime('%Y-%m-%d')
        url = 'https://api.weixin.qq.com/bizwifi/statistics/list?access_token='+authorizer_access_token
        data = {
            "begin_date": date,
            "end_date": datenow,
            "shop_id":-1,
            }
        r = requests.post(url, json.dumps(data))
        people = eval(r.content)['data'][0]['total_fans']
        people2 = eval(r.content)['data'][0]['new_fans']
        return render_to_response('scenic/guanli.html', {
          'var_pre_auth_code': config.get("wechat",{}).get("pre_auth_code"),
          'people':people,
          'people2':people2,
          'head_img':obj.head_img,
          'nick_name':obj.nick_name,
          'mendian_name':obj.mendian_name,
          }, context_instance=RequestContext(request))
  except:
    return render_to_response('scenic/wechat3pt.html', {
      'var_pre_auth_code': config.get("wechat",{}).get("pre_auth_code"),
      }, context_instance=RequestContext(request))


def wechat3pt_success(request):
  auth_code = request.GET.get('auth_code', '')
  with open(settings.CONFIG2) as infile:
    config = json.load(infile)
  access_token = config.get("wechat",{}).get("access_token")
  url = 'https://api.weixin.qq.com/cgi-bin/component/api_query_auth?component_access_token=' + access_token
  data = {
      "component_appid": settings.COMPONENT_APPID,
      "authorization_code": auth_code,
    }
  r = requests.post(url, json.dumps(data))
  authorizer_appid = eval(r.content)['authorization_info']['authorizer_appid']
  authorizer_access_token = eval(r.content)['authorization_info']['authorizer_access_token']
  authorizer_refresh_token = eval(r.content)['authorization_info']['authorizer_refresh_token']
  if Scenic.objects.filter(authorizer_appid=authorizer_appid) and Scenic.objects.filter(authorizer_appid=authorizer_appid).last().isdel == True:
    messages.error(request,u'该公众号已绑定，请换公众号绑定')
    return redirect('/wechat/')
  else:
    if request.user.group.role == 0:
      if not Scenic.objects.filter(group=request.user.group):
        obj = Scenic.objects.create(group=request.user.group)
      else:
        obj = Scenic.objects.get(group=request.user.group)
    else:
      obj=request.user.group.scenic_set.first()
    obj.mendian_name = None
    obj.authorizer_appid =  authorizer_appid
    obj.authorizer_access_token = authorizer_access_token
    obj.authorizer_refresh_token = authorizer_refresh_token
    url = 'https://api.weixin.qq.com/cgi-bin/component/api_get_authorizer_info?component_access_token=' + access_token
    data = {
        "component_appid": settings.COMPONENT_APPID,
        "authorizer_appid": authorizer_appid,
      }
    r = requests.post(url, json.dumps(data))
    nick_name = eval(r.content)['authorizer_info']['nick_name']
    head_img = eval(r.content)['authorizer_info']['head_img']
    qrcode_url = eval(r.content)['authorizer_info']['qrcode_url']
    vv = head_img.replace('\\','')
    ee = qrcode_url.replace('\\','')
    obj.nick_name = nick_name
    obj.head_img = vv
    obj.qrcode_url = ee
    obj.isdel = True
    obj.save()
    func_info = eval(r.content)['authorization_info']['func_info']
    d = []
    for i in func_info:
      d.append(i['funcscope_category']['id'])
    return render_to_response('scenic/wechat3pt_success.html', {
        'head_img': vv,
        'nick_name':nick_name,
      }, context_instance=RequestContext(request))

def ifkaitong(request):
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj=request.user.group.scenic_set.first()
  url = 'https://api.weixin.qq.com/bizwifi/openplugin/token?access_token='+ obj.authorizer_access_token
  data = {
      "callback_url": "http://hiyou.doublecom.net/scenic/kaitong/",
      }
  r = requests.post(url, json.dumps(data))
  a = r.json()
  is_open = a['data']['is_open']
  if is_open == True:
    return redirect('/scenic/kaitong/')
  else:
    wifi_token = a['data']['wifi_token']
    #wifi_token = eval(r.content)['data']['wifi_token']
    return render_to_response('scenic/weikaitong.html', {
        'wifi_token': wifi_token,
        }, context_instance=RequestContext(request))

def mendianxinxi(request):
  #data = {
   #   "url": "http://hiyou.doublecom.net/static/img/dbcom.jpg"
    #}
#  r = requests.post(url, json.dumps(data))
#  r = requests.post(url, file=requests.get('url').content)
#  r = requests.post(url, file=open(user.img.path).read())
  return render(request,'scenic/xinjian.html')


def mendianxinxi2(request):
  name = request.GET.get('name')
  province = request.GET.get('province')
  city = request.GET.get('city')
  district = request.GET.get('district')
  street = request.GET.get('street')
  street_number = request.GET.get('street_number')
  lat = request.GET.get('lat')
  lng = request.GET.get('lng')
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj = request.user.group.scenic_set.first()
  access_token = obj.authorizer_access_token
  url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=' + access_token
  files = { 'media' : open(os.path.join('static','img','dbcom.jpg'))}
  r = requests.post(url,files=files)
  data = {
    "business": {
      "base_info":{
                "business_name": name.encode('utf-8'),
                "branch_name":"",
                "address": street.encode('utf-8') + street_number.encode('utf-8'),
                "telephone":"400-6866-288",
                "province":province.encode('utf-8'),
                "city": city.encode('utf-8'),
                "offset_type":1,
                "categories": ["其它,其它"],
                "longitude":lng.encode('utf-8'),
                "latitude":lat.encode('utf-8'),
                "district":district.encode('utf-8')
              }
    }
  }
  url = 'http://api.weixin.qq.com/cgi-bin/poi/addpoi?access_token='+ access_token
  r= requests.post(url, data=json.dumps(data, ensure_ascii=False, encoding="utf-8"))
  poi_id = eval(r.content)['poi_id']
  url = 'http://api.weixin.qq.com/cgi-bin/poi/getpoi?access_token='+access_token
  data = {
      "poi_id": poi_id,
    }
  r = requests.post(url, json.dumps(data))
  access_token = obj.authorizer_access_token
  url = 'https://api.weixin.qq.com/bizwifi/shop/list?access_token='+access_token
  data = {
  "pageindex": 1,   
  "pagesize":20
  }
  r = requests.post(url,data=json.dumps(data))
  shop_name = json.loads(r.content)
  shop_name = shop_name['data']['records']
  d = []
  g = {}
  for i in shop_name:
    g['shop_name']=i['shop_name']
    g['shop_id']=i['shop_id']
    d.append(g)
    g = {}
  return HttpResponse(json.dumps(d))

def kaitong(request):
  return render(request,'scenic/kaitong.html')

def weikaitong(request):
  return render(request,'scenic/weikaitong.html')

def set_success(request):
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=requauthorizer_refresh_tokenest.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj = request.user.group.scenic_set.first()
  if request.GET.get('d'):
    aa = json.loads(request.GET.get('d'))
  else:
    access_token = obj.authorizer_access_token
    url = 'https://api.weixin.qq.com/bizwifi/shop/list?access_token='+access_token
    data = {
        "pageindex": 1,   
        "pagesize":20
        }
    r = requests.post(url,data=json.dumps(data))
    shop_name = json.loads(r.content)
    shop_name = shop_name['data']['records']
    d = []
    g = {}
    for i in shop_name:
      g['shop_name']=i['shop_name']
      g['shop_id']=i['shop_id']
      d.append(g)
      g = {}
      aa = d
  return render(request,'scenic/set_success.html',{'shop_name':aa})

@csrf_exempt
def setting(request):
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
    access_token = obj.authorizer_access_token
    if request.method == 'POST':
      sid = request.POST.get('id')
      ssid = request.POST.get('ssid')
      name = request.POST.get('name')
      url = 'https://api.weixin.qq.com/bizwifi/apportal/register?access_token='+access_token
      data = {
          "shop_id": sid.encode('utf-8'),
          "ssid":  ssid.encode('utf-8')
          }
      r = requests.post(url, data=json.dumps(data, ensure_ascii=False, encoding="utf-8"))
      errcode = eval(r.content)['errcode']
      if errcode == 0:
        secretkey = eval(r.content)['data']['secretkey']
        obj.mendian_name = name
        obj.shop_id = sid
        obj.secretkey = secretkey
        obj.ssid = ssid
        obj.save()
        return HttpResponse(json.dumps(data))
      else:
        return HttpResponse('no')
    else:
      d = request.GET.get('d')
      sid = eval(d)['shop_id']
      ssid =eval(d)['ssid']
  else:
    obj = request.user.group.scenic_set.first()
    access_token = obj.authorizer_access_token
    if request.method == 'POST':
      sid = request.POST.get('id')
      ssid = request.POST.get('ssid')
      name = request.POST.get('name')
      url = 'https://api.weixin.qq.com/bizwifi/apportal/register?access_token='+access_token
      data = {
          "shop_id": sid.encode('utf-8'),
          "ssid":  ssid.encode('utf-8')
          }
      r = requests.post(url, data=json.dumps(data, ensure_ascii=False, encoding="utf-8"))
      errcode = eval(r.content)['errcode']
      if errcode == 0:
        secretkey = eval(r.content)['data']['secretkey']
        mac = obj.dev_set.filter(dev_type='2').first().macaddr
        obj.mendian_name = name
        obj.shop_id = sid
        obj.secretkey = secretkey
        obj.ssid = ssid
        obj.save()
        url = 'http://hiyou.doublecom.net/ausv/loginc/'
        wenjian = 'login.html'
        a = get_aus_update_file(url,wenjian,mac)
        url = 'http://hiyou.doublecom.net/ausv%s/login/'%obj.pk
        wenjian = '/phone/login.html'
        a = get_aus_update_file(url,wenjian,mac)
        url = 'http://hiyou.doublecom.net/ausv%s/alogin/'%obj.pk
        wenjian = '/phone/alogin.html'
        a = get_aus_update_file(url,wenjian,mac)
        url = 'http://hiyou.doublecom.net/ausvpc%s/login/'%obj.pk
        wenjian = '/pc/login.html'
        a = get_aus_update_file(url,wenjian,mac)
        url = 'http://hiyou.doublecom.net/ausvpc%s/alogin/'%obj.pk
        wenjian = '/pc/alogin.html'
        a = get_aus_update_file(url,wenjian,mac)
        url = 'http://hiyou.doublecom.net/ausv%s/rlogin/'%obj.pk
        wenjian = 'rlogin.html'
        #a = get_aus_update_file(url,wenjian,mac)
        return HttpResponse(json.dumps(data))
      else:
        return HttpResponse('no')
    else:
      d = request.GET.get('d')
      sid = eval(d)['shop_id']
      ssid =eval(d)['ssid']
  return render(request,'scenic/setting.html',{'sid':sid,'ssid':ssid})

@csrf_exempt
def shop_index(request):
  name = request.POST.get('name')
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj = request.user.group.scenic_set.first()
  access_token = obj.authorizer_access_token
  sid = obj.shop_id
  obj.shop_index = name
  obj.save()
  url = 'https://api.weixin.qq.com/bizwifi/homepage/set?access_token='+access_token
  data = {
      "shop_id": sid.encode('utf-8'),
      "template_id": 1,
      "struct": {
        "url": name.encode('utf-8')
        }
      }
  r = requests.post(url, data=json.dumps(data, ensure_ascii=False, encoding="utf-8"))
  url = 'https://api.weixin.qq.com/bizwifi/finishpage/set?access_token='+access_token
  data = {
      "shop_id": sid.encode('utf-8'),
      "finishpage_url": "http://hiyou.doublecom.net/scenic/change/"
      }
  r2 = requests.post(url, data=json.dumps(data, ensure_ascii=False, encoding="utf-8"))
  if r.json()['errcode'] == 0 and r2.json()['errcode'] == 0:
    messages.success(request, u'成功绑定页面')
  else:
    messages.error(request,u'绑定失败')
  return redirect('/wechat/')

@csrf_exempt
def temlist(request):
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj = request.user.group.scenic_set.first()
  access_token = obj.authorizer_access_token
  url = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token='+access_token
  r = requests.post(url)
  return HttpResponse(json.dumps(eval(r.content)['template_list'], ensure_ascii=False, encoding="utf-8"))

@csrf_exempt
def tembind(request):
  template_id = request.POST.get('type')
  data = request.POST.get('name')
  if request.user.group.role == 0:
    if not Scenic.objects.filter(group=request.user.group):
      obj = Scenic.objects.create(group=request.user.group)
    else:
      obj = Scenic.objects.get(group=request.user.group)
  else:
    obj = request.user.group.scenic_set.first()
  obj.template_id = template_id
  obj.data = data
  obj.save()
  messages.success(request, u'成功绑定页面')
  return redirect('/wechat/')

@csrf_exempt
def changeurl(request):
  extend = request.GET.get('extend')
  authorizer_appid = extend[17:35]
  ip = extend[52:]
  openId = request.GET.get('openId')
  timestamp = request.GET.get('timestamp')
  key = '%s:%s' % (openId, timestamp)
  page = cache.get(key)
  if not page:
    obj = Scenic.objects.filter(authorizer_appid=authorizer_appid).last()
    try:
      access_token = obj.authorizer_access_token
    except:
      get_token(obj)
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s'%(access_token)
    a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    data = {
        "touser":openId,
        "template_id":obj.template_id,
        "data":{
          "first":{
            "value":"您好，欢迎您成功登录Hi游免费WiFi",
            "color":"#173177"
            },
          "time":{
            "value":a,
            "color":"#173177"
            },
          "ip":{
            "value":ip,
            "color":"#173177"
            },
          "reason":{
            "value":obj.data,
            "color":"#173177"
            }
          }
        }
    r1 = requests.post(url, json.dumps(data))
    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN'%(access_token,openId)
    r = requests.get(url)
    subscribe = eval(r.content).get('subscribe', 0)
    if subscribe == 0:
      url = "/nogz/%s/"%(obj.authorizer_appid,)
    else:
      url = obj.shop_index
    cache.set(key,r1.content, 30)
    useragent = request.META['HTTP_USER_AGENT']
    return render(request,'scenic/change.html',{'url':url})
  else:
    return HttpResponse('')

def nogz(request,authorizer_appid=0):
  obj = Scenic.objects.filter(authorizer_appid=authorizer_appid).last()
  try:
    access_token = obj.authorizer_access_token
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s'%(access_token)
    data = {
        "expire_seconds":300,
        "action_name":"QR_LIMIT_SCENE",
        "action_info":{"scene": {"scene_id": 123}}
        }
    r = requests.post(url,data=json.dumps(data))
    ticket = eval(r.content)['ticket']
  except:
    get_token(obj)
    access_token = obj.authorizer_access_token
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s'%(access_token)
    data = {
        "expire_seconds":300,
        "action_name":"QR_LIMIT_SCENE",
        "action_info":{"scene": {"scene_id": 123}}
        }
    r = requests.post(url,data=json.dumps(data))
    ticket = eval(r.content)['ticket']
  url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket='+ticket
  r = requests.get(url)
  picture = r.content
  filename = os.path.join(settings.BASE_DIR, 'static/images',obj.authorizer_appid+'.jpg')
  local=open(filename,'wb+')
  local.write(picture)
  local.close()
  return render(request,'scenic/nogz.html',{'url':'/static/images'+'/'+obj.authorizer_appid+'.jpg'})

def rlogin(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if not obj.agent_id:
    obj = Group.objects.get(role=0).scenic_set.first()
  else:
    if not obj.mendian_name:
      obj = Group.objects.get(role=0).scenic_set.first()
  mac = Scenic.objects.get(pk=pk).dev_set.filter(dev_type='2').first().macaddr
  return render(request,'scenic/rlogin.html',{'obj':obj,'mac':mac})

def portal(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if not obj.agent_id:
    obj = Group.objects.get(role=0).scenic_set.first()
  else:
    if not obj.mendian_name:
      obj = Group.objects.get(role=0).scenic_set.first()
  mac = Scenic.objects.get(pk=pk).dev_set.filter(dev_type='2').first().macaddr
  return render(request,'scenic/choosephone2.html',{'obj':obj,'mac':mac})

def check(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if not obj.agent_id:
    obj = Group.objects.get(role=0).scenic_set.first()
  else:
    if not obj.mendian_name:
      obj = Group.objects.get(role=0).scenic_set.first()
  return render(request,'scenic/choosephone.html',{'obj':obj})

def loginc(request):
  return render(request,'scenic/login.html')

def check2(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if not obj.agent_id:
    obj = Group.objects.get(role=0).scenic_set.first()
  else:
    if not obj.mendian_name:
      obj = Group.objects.get(role=0).scenic_set.first()
  return render(request,'scenic/choosepc.html',{'obj':obj})

def connect(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  if not obj.agent_id:
    obj = Group.objects.get(role=0).scenic_set.first()
  else:
    if not obj.mendian_name:
      obj = Group.objects.get(role=0).scenic_set.first()
  return render(request,'scenic/choosepc2.html',{'obj':obj})

@csrf_exempt
def wxwifirz(request):
  extend = request.GET.get('extend')
  mac = extend[:17]
  openId = request.GET.get('openId')
  tid = request.GET.get('tid')
  authorizer_appid = extend[17:35]
  obj = Scenic.objects.filter(authorizer_appid=authorizer_appid).last()
  mm = extend[35:52]
  time1 = datetime.datetime.now()
  try:
    access_token = obj.authorizer_access_token
    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN'%(access_token,openId)
    r = requests.get(url)
    subscribe = eval(r.content)['subscribe']
  except:
    get_token(obj)
    access_token = obj.authorizer_access_token
    url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN'%(access_token,openId)
    r = requests.get(url)
    subscribe = eval(r.content)['subscribe']
  kick.apply_async((subscribe,mac,mm),eta=datetime.datetime.now() - timedelta(hours=8) + timedelta(seconds=180))
  return HttpResponse('')

def dev(request,tx=None):
  search = request.GET.get('search')
  obj = request.user
  objs = obj.group.scenic_set.first() 
  ob = objs and objs.dev_set.all() or []
  dev_off = 0
  if tx:
    ob = objs.dev_set.filter(isonline=0)
    dev_off = 1
  if search:
    ob = objs.dev_set.filter(macaddr__contains=search)
  return render(request,'scenic/dev.html',{
      'objs':ob,
      'search':search,
      'of':dev_off,
      'pk':objs.pk,
      'dev': {
          'link': '/scenic/dev/',
          'bgcolor': 'blue',
          'title':objs.dev_set.all().count(),
          'label': u'设备总数',
          'img': '/static/img/content-no.png',
          },
      'dev_off': {
          'link': '/scenic/off/dev/',
          'bgcolor': 'red',
          'title':objs.dev_set.filter(isonline=0).count(),
          'label': u'离线设备总数',
          'img': '/static/img/content.png',
          },
      })

def export(request,pk=0,off=0):
  response = HttpResponse(content_type='application/vnd.ms-excel')  
  response['Content-Disposition'] = 'attachment;filename=scenic_dev.xls'  
  wb = xlwt.Workbook(encoding = 'utf-8')  
  sheet = wb.add_sheet(u'设备')      
  sheet.write(0,0, u'设备MAC')
  sheet.write(0,1, u'所属景区')
  sheet.write(0,2, u'经纬度') 
  sheet.write(0,3, u'设备类型')
  sheet.write(0,4, u'在线状态')
  sheet.write(0,5, u'创建日期')        
  row = 1 
  search = request.GET.get('search')
  obj = Scenic.objects.get(pk=pk)
  objs = obj.dev_set.all()
  if int(off):
    objs = obj.dev_set.filter(isonline=0)
  if search and search != 'None':
    objs = objs.filter(macaddr__contains=search)
  if not objs:
    messages.error(request, u'导出失败！导出的无内容!')
    return redirect('/scenic/dev/')
  for usa in objs:  
    sheet.write(row,0, usa.macaddr)
    if usa.region_dev:
      sheet.write(row,1, usa.region_dev.name)
    else:
      sheet.write(row,1, '-')
    sheet.write(row,2, usa.latitude) 
    sheet.write(row,3, usa.get_type())
    if usa.online_time: 
      sheet.write(row,4, usa.get_time())
    else:
      sheet.write(row,4,'-')
    sheet.write(row,5, usa.pub_date.strftime('%Y-%m-%d %X')) 
    row=row + 1  
  output = StringIO.StringIO()  
  wb.save(output)  
  output.seek(0)  
  response.write(output.getvalue())  
  return response 

def num(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  num = request.POST.get('num')
  if request.method == 'POST':
    obj.num = int(num)
    obj.save()
  return redirect('/scenic/')

def details(request,scenic_pk=0,pk=0):
  obj = Dev.objects.get(pk=pk)
  objs = Scenic.objects.get(pk=scenic_pk).region_set.all()
  if request.method=='POST':
    region = request.POST.get('region')
    if region:
      ob = Region.objects.get(pk=int(region))
    else:
      ob = None
    obj.region_dev=ob
    obj.save()
    messages.success(request, u'修改成功!')
  return render(request,'scenic/dev_details.html',{
  'obj':obj,
  'pk':scenic_pk,
  'objs':objs
  })

def region_modify(request,sc_pk=0,pk=0):
  name = request.POST.get('name')
  if Scenic.objects.get(pk=sc_pk).region_set.filter(name=name):
    messages.error(request, u'修改失败！此区域名已存在!')
    return redirect('/agent/'+sc_pk+'/'+pk+'/agent_map/')
  else:
    obj = Region.objects.get(pk=pk)
    obj.name = name
    obj.save()
    messages.success(request, u'修改成功!')
    return redirect('/agent/'+sc_pk+'/'+pk+'/agent_map/')

def region_del(request,sc_pk=0,pk=0):
  obj = Region.objects.get(pk=pk)
  if obj.dev_set.all().count():
    messages.error(request, u'删除失败！先删除此区域关联的设备!')
    return redirect('/agent/'+sc_pk+'/'+pk+'/agent_map/')
  else:
    obj.delete()
    messages.success(request, u'删除成功!')
  return redirect('/agent/'+sc_pk+'/region/')

@csrf_exempt
def real_time(request):
  mac = request.POST.get('mac')
  data = []
  if not mac:
    mac = []
  else:
    mac = eval(mac)
  obj = Dev.objects.filter(macaddr__in=mac)
  try:
    for objs in obj:
      temp = {}
      temp['mac'] = objs.macaddr
      temp['uptime'] = str(objs.get_time())
      temp['online'] = str(objs.isonline)
      data.append(temp)
    data = {'data':data}
  except:
    data = {'data':data}
  return HttpResponse(json.dumps(data))

@csrf_exempt
def text(request):
    obj = request.user.group.scenic_set.first()
    objs = Text.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        num = request.POST.get('num')
        direct = request.POST.get('direct')
        time = request.POST.get('time')
        if time:
            objss = Text.objects.get(pk=time)
            objss.name = name
            objss.num = num
            objss.direct= direct
            objss.save()
        else:
            Text.objects.create(num=num,name=name,direct=direct,scenic_text=obj)
        return redirect('/scenic/text/')
    return render(request,'scenic/text.html',{'objs':objs})


def text_del(request,pk=0):
    obj = Text.objects.get(pk=pk)
    obj.delete()
    return redirect('/scenic/text/')


def text_content(request,pk=0):
    obj = Text.objects.get(pk=pk)
    objs = obj.textcontent_set.all()
    return render(request,'scenic/text_content.html',{'obj':obj,'objs':objs})


@csrf_exempt
def content_add(request,pk=0):
    obj = Text.objects.get(pk=pk)
    if request.method == 'POST':
        num = request.POST.get('num')
        title = request.POST.get('title')
        img = request.FILES.get('imgfile',None)
        text = request.POST.get('text')
        objs = TextContent.objects.create(num=num,title=title,image=img,text=text,scenic_text=obj)
        return redirect('/scenic/'+pk+'/text_content/')
    return render(request,'scenic/content_add.html',{'pk':pk})

@csrf_exempt
def content_edit(request,pk=0):
    obj = TextContent.objects.get(pk=pk)
    if request.method == 'POST':
        num = request.POST.get('num')
        title = request.POST.get('title')
        img = request.FILES.get('imgfile',None)
        text = request.POST.get('text')
        obj.num = num
        obj.title = title
        if img:
            obj.image = img
        obj.text = text
        obj.save()
        return redirect('/scenic/'+str(obj.scenic_text.pk)+'/text_content/')
    return render(request,'scenic/content_edit.html',{'obj':obj})

def content_del(request,pk=0):
    obj = TextContent.objects.get(pk=pk)
    obj.delete()
    return redirect('/scenic/'+str(obj.scenic_text.pk)+'/text_content/')

@csrf_exempt
def probe(request):
  if request.method == 'POST':
    obj = request.user
    objs = obj.group.scenic_set.first()
    ob = objs.dev_set.filter(dev_type='1')
    p = MacParser()
    data = []
    try:
      for o in ob:
        da = cache.get(o.macaddr)
        if da:
          for oo in da:
            temp = {}
            temp['mac'] = o.macaddr
            temp['macc'] = eval(oo)['mac']
            temp['signal'] = eval(oo)['signal']
            ty = p.get_manuf(eval(oo)['mac'])
            comment = p.get_comment(eval(oo)['mac'])
            if not comment:
              comment = 'null'
            if  ty:
              if 'HuaweiTe' in ty: temp['type'] = u'华为'
              elif 'OppoDigi' in ty or 'OPPO' in comment:
                temp['type'] = 'OPPO'
              elif 'VivoMobi' in ty or 'vivo' in comment:
                temp['type'] = 'vivo'
              elif 'XiaomiCo' in ty or 'XiaomiEl' in ty:
                temp['type'] = u'小米'
              elif 'SamsungE' in ty: temp['type'] = u'三星'
              elif 'Zte' in ty: temp['type'] = u'中兴'
              elif 'Apple' in ty: temp['type'] = u'苹果'
              else: temp['type'] = p.get_manuf(eval(oo)['mac'])
            else: temp['type'] = '-'
            temp['time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(eval(oo)['time']))
            data.append(temp)
    except:
      pass
    return HttpResponse(json.dumps(data))
  return render(request,'scenic/probe.html')

@csrf_exempt
def tclient(request):
  obj = request.user
  objs = obj.group.scenic_set.first()
  if request.method == 'POST':
    data = []
    page = request.POST.get('page')
    mac = request.POST.get('mac')
    typ = request.POST.get('type')
    da = request.POST.get('date')
    ob = objs.client_set.all()
    obo = None
    try:
      if mac or typ or da:
        ob = objs.client_set.filter(mac__contains=mac,
          typee__contains=typ,endtime__contains=da)
      if int(page) == 1:
        obo = ob[:10]
      else:
        obo = ob[(int(page)-1)*10:int(page)*10]
      for oo in obo:
        temp = {}
        temp['mac'] = oo.mac
        temp['tanzmac'] = oo.tanz.mac
        temp['endtime'] = str(oo.endtime)[:19]
        temp['type'] = oo.typee
        temp['statrtime'] = str(oo.statrtime)[:19]
        temp['num'] = oo.num
        data.append(temp)
      data = {'data':data,'count':ob.count()}
      return HttpResponse(json.dumps(data))
    except:
      return HttpResponse(json.dumps({'data':[],'count':1}))
  return render(request,'scenic/tan_table.html')

def tanz(request):
  obj = request.user
  objs = obj.group.scenic_set.first()
  obj = objs.tanz_set.all()
  return render(request,'scenic/tanz.html',{
  'obj':obj
  }) 

@csrf_exempt
def commodity(request):
  if request.method == 'POST':
    pk = request.POST.get('pk')
    data = request.POST.get('data')
    choose = request.POST.get('choose')
    obj = Scenic.objects.filter(pk=pk).first()
    if choose:
      if choose == '1':
        objs = Commodity.objects.filter(name__contains=data,scenic=obj,grounding=1)
      elif choose == '2':
        oobj = Commodity_Group.objects.filter(name__contains=data,scenic=obj).first()
        ob = Commodity.objects.filter(scenic=obj,grounding=1)
        objs = []
        for o in ob:
          for p in json.loads(o.group):
            try:
              if int(p) == oobj.pk:
                objs.append(o)
            except:
              pass
      elif choose == '3':
        objs = Commodity.objects.filter(name__contains=data,scenic=obj,grounding=0)
      elif choose == '4':
        oobj = Commodity_Group.objects.filter(name__contains=data,scenic=obj).first()
        ob = Commodity.objects.filter(scenic=obj,grounding=0)
        objs = []
        for o in ob:
          for p in json.loads(o.group):
            if int(p) == oobj.pk:
              objs.append(o)
      arr = []
      for o in objs:
        data = {}
        if choose == '1' or choose == '2':
          data['grounding'] = 1
        elif choose == '3' or choose == '4':
          data['grounding'] = 0
        data['name'] = o.name
        data['group'] = ''
        for q in json.loads(o.group):
          qq = Commodity_Group.objects.get(pk=q)
          data['group'] = data['group']+','+qq.name
        data['group'] = data['group'][1:]
        data['price'] = o.price
        data['stock'] = o.stock
        data['sales'] = o.sales
        data['date'] = str(o.date)[:19]
        data['operate'] = o.pk
        arr.append(data)
    else:
      objs = Commodity_Group.objects.filter(name__contains=data,scenic=obj)
      arr = []
      for o in objs:
        data = {}
        data['name'] = o.name
        data['date'] = str(o.date)[:19]
        data['gr'] = o.grounding
        data['operate'] = o.pk
        arr.append(data)
    return HttpResponse(json.dumps(arr))
  obj = Commodity.objects.all()
  pk = request.user.group.scenic_set.first().pk
  return render(request,'scenic/commodity.html',{'obj':obj,'pk':pk})

def commodity_ajax(request,pk=0):
  obj = Scenic.objects.get(pk=pk)
  objs = obj.commodity_set.all()
  objss = obj.commodity_group_set.all()
  arr = []
  for o in objs:
    data = {}
    data['grounding'] = o.grounding
    data['name'] = o.name
    data['group'] = ''
    for q in json.loads(o.group):
      qq = Commodity_Group.objects.get(pk=q)
      data['group'] = data['group']+','+qq.name
    data['group'] = data['group'][1:]
    data['price'] = o.price
    data['stock'] = o.stock
    data['sales'] = o.sales
    data['date'] = str(o.date)[:19]
    data['operate'] = o.pk
    arr.append(data)
  for o in objss :
    data = {}
    data['name'] = o.name
    data['date'] = str(o.date)[:19]
    data['gr'] = o.grounding
    data['operate'] = o.pk
    arr.append(data)
  return HttpResponse(json.dumps(arr))


def order(request):
  return render(request,'scenic/order.html',{})

def add_sales(request,pk=0,tx=0):
  return render(request,'scenic/add_sales.html',{'pk':pk,'tx':tx})

@csrf_exempt
def add_sales_ajax(request,pk=0,tx=0):
  obj = Scenic.objects.get(pk=pk)
  if request.method == 'POST':
    name = request.POST.get('name')
    group = request.POST.get('group')
    price = request.POST.get('price')
    price_old = request.POST.get('price_old')
    stock = request.POST.get('stock')
    grounding = request.POST.get('grounding')
    image = request.POST.get('image')
    content = request.POST.get('content')
    if tx == 0:
      Commodity.objects.create(name=name,price=price,stock=stock,group=group,scenic=obj,grounding=grounding,price_old=price_old,content=content,image=image)
    else:
      objs = Commodity.objects.filter(pk=tx).first()
      objs.name = name
      objs.group = group
      objs.price = price
      objs.stock = stock
      objs.grounding = grounding
      objs.price_old = price_old
      objs.content = content
      objs.image = image
      objs.save()
    group = json.loads(group)
    if grounding == '1':
      for o in group:
        ob = Commodity_Group.objects.get(pk=o)
        ob.grounding = ob.grounding + 1
        ob.save()
    return HttpResponse('success')
  else:
    objs = obj.commodity_group_set.all()
    data = []
    for o in objs:
      arr = {}
      arr['name'] = o.name
      arr['pk'] = o.pk
      data.append(arr)
    if tx == 0:
      return HttpResponse(json.dumps(data))
    else:
      objs = Commodity.objects.filter(pk=tx).first()
      arr = {}
      arr['name'] = objs.name
      arr['group'] = objs.group
      arr['price'] = objs.price
      arr['stock'] = objs.stock
      arr['grounding'] = objs.grounding
      arr['price_old'] = objs.price_old
      arr['content'] = objs.content
      arr['image'] = objs.image
      arr['lis'] = data
    return HttpResponse(json.dumps(arr))


@csrf_exempt
def down_sales_ajax(request):
  if request.method == 'POST':
    if request.POST.get('pk'):
      pk = request.POST.get('pk')
      obj = Commodity.objects.filter(pk=pk).first()
      obj.grounding = 0
      obj.save()
      for o in json.loads(obj.group):
        ob = Commodity_Group.objects.get(pk=o)
        ob.grounding = ob.grounding - 1
        ob.save()
    elif request.POST.get('id'):
      pk = json.loads(request.POST.get('id'))
      for o in pk:
        obj = Commodity.objects.filter(pk=o).first()
        obj.grounding = 0
        obj.save()
        for p in json.loads(obj.group):
          ob = Commodity_Group.objects.get(pk=p)
          ob.grounding = ob.grounding - 1
          ob.save()
    return HttpResponse('success')

@csrf_exempt
def up_sales_ajax(request):
  if request.method == 'POST':
    if request.POST.get('pk'):
      pk = request.POST.get('pk')
      obj = Commodity.objects.filter(pk=pk).first()
      obj.grounding = 1
      obj.save()
      for o in json.loads(obj.group):
        ob = Commodity_Group.objects.get(pk=o)
        ob.grounding = ob.grounding + 1
        ob.save()
    elif request.POST.get('id'):
      pk = json.loads(request.POST.get('id'))
      for o in pk:
        obj = Commodity.objects.filter(pk=o).first()
        obj.grounding = 1
        obj.save()
        for p in json.loads(obj.group):
          ob = Commodity_Group.objects.get(pk=p)
          ob.grounding = ob.grounding + 1
          ob.save()
    return HttpResponse('success')

@csrf_exempt
def delete_sales_ajax(request):
  if request.method == 'POST':
    if request.POST.get('pk'):
      pk = request.POST.get('pk')
      obj = Commodity.objects.filter(pk=pk).first()
      obj.delete()
    elif request.POST.get('id'):
      pk = json.loads(request.POST.get('id'))
      for o in pk:
        obj = Commodity.objects.filter(pk=o).first()
        obj.delete()
    return HttpResponse('success')

@csrf_exempt
def add_group_ajax(request,pk=0):
  if request.method == 'POST':
    if request.POST.get('pk'):
      pk = request.POST.get('pk')
      name = request.POST.get('data')
      obj = Commodity_Group.objects.filter(pk=pk).first()
      obj.name = name
      obj.save()
    else:
      name = request.POST.get('data')
      obj = Scenic.objects.filter(pk=pk).first()
      Commodity_Group.objects.create(name=name,scenic=obj,grounding=0)
    return HttpResponse('success')

@csrf_exempt
def del_group_ajax(request,tx=0):
  if request.method == 'POST':
    pk = request.POST.get('pk')
    obj = Scenic.objects.get(pk=tx)
    objs = Commodity.objects.filter(scenic=obj)
    ob = Commodity_Group.objects.filter(pk=pk).first()
    for o in objs:
      for p in json.loads(o.group):
        if int(p) == ob.pk:
          lis = json.loads(o.group)
          lis.remove(p)
          o.group = json.dumps(lis)
          o.save()
    ob.delete()
    return HttpResponse('success')