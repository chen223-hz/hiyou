#coding:utf-8
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.http import Http404
from webapp.account.models import User
from django.conf import settings
from webapp.utils.send_sms import send_sms0, send_sms1
import requests
import json
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator

def _get_wx_api(url):
  try:
    response = json.loads(requests.get(url,verify=False).content)
  except:
    try:
      response = json.loads(requests.get(url,verify=False).content)
    except:
      try:
        response = json.loads(requests.get(url,verify=False).content)
      except:
        response = {}
  return response

def fake_wxlogin2(request):
  code = request.GET.get('fake')
  if code:
    unid = 'fake'
    nickname = u'演示用户'
    headimgurl = 'http://cdn.doublecom.net/Cameo/img/avatar.jpg'
    suser = User.objects.filter(cellphone='13122627507')[0]
    request.session['unionid'] = unid
    request.session['nickname'] = nickname
    request.session['headimgurl'] = headimgurl
    suser.set_password(unid)
    suser.nickname = nickname
    suser.wechatUNID = unid
    suser.headimgurl = headimgurl
    suser.save()
    user = authenticate(username=suser.cellphone, password=suser.wechatUNID)
    login(request, user)
    return redirect('/headquar/')
  return render(request,'account/login.html')

def fake_wxlogin(request):
  '''doc'''
  url ='https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx43bb4143fa8c5b83&secret=e8d7900ee18c9463141d18d34f38b58e&code=%s&grant_type=authorization_code'
  # 获取用户信息
  url3 = 'https://api.weixin.qq.com/sns/userinfo?access_token=%(access_token)s&openid=%(openid)s&lang=zh_CN'

  code = request.GET.get('code')
  if code:
    url = url % code
    response = _get_wx_api(url)
    if response.has_key('errcode') and response["errcode"] == 40029:
      return redirect('/')
    # 没有access_token也跳回首页
    if not response.has_key('access_token'):
      return redirect('/')
    # todo: errcode 40003
    response =  _get_wx_api(url3 % response)
    unid = response.get('unionid')
    nickname = response.get('nickname')
    headimgurl = response.get('headimgurl')
    if not unid:
      # todo: log
      return redirect('/')
    '''
    微信接口:
    openid = response.get('openid')  #openid
    nickname = response.get('nickname')  #昵称
    sex = response.get('sex')  #性别
    province = response.get('province')  #省份
    city = response.get('city')  #城市
    country = response.get('country')  #国家
    headimgurl = response.get('headimgurl')  #头像url
    '''
    suser = User.objects.filter(cellphone='15313177798')[0]
    request.session['unionid'] = unid
    request.session['nickname'] = nickname
    request.session['headimgurl'] = headimgurl
    suser.set_password(str(unid))
    suser.nickname = nickname
    suser.wechatUNID = unid
    suser.headimgurl = headimgurl
    suser.save()
    user = authenticate(username=suser.cellphone, password=suser.wechatUNID)
    login(request, user)
    return redirect('/headquar/')
  return render(request,'account/login.html')

def wxlogin(request):
  '''doc'''
  url ='https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx43bb4143fa8c5b83&secret=e8d7900ee18c9463141d18d34f38b58e&code=%s&grant_type=authorization_code'
  # 获取用户信息
  url3 = 'https://api.weixin.qq.com/sns/userinfo?access_token=%(access_token)s&openid=%(openid)s&lang=zh_CN'

  code = request.GET.get('code')
  if code:
    url = url % code
    response = _get_wx_api(url)
    if response.has_key('errcode') and response["errcode"] == 40029:
      return redirect('/')
    # 没有access_token也跳回首页
    if not response.has_key('access_token'):
      return redirect('/')
    # todo: errcode 40003
    response =  _get_wx_api(url3 % response)
    unid = response.get('unionid')
    nickname = response.get('nickname')
    headimgurl = response.get('headimgurl')
    if not unid:
      # todo: log
      return redirect('/')
    '''
    微信接口:
    openid = response.get('openid')  #openid
    nickname = response.get('nickname')  #昵称
    sex = response.get('sex')  #性别
    province = response.get('province')  #省份
    city = response.get('city')  #城市
    country = response.get('country')  #国家
    headimgurl = response.get('headimgurl')  #头像url
    '''
    suser = User.objects.filter(wechatUNID=str(unid))
    request.session['unionid'] = unid
    request.session['nickname'] = nickname
    request.session['headimgurl'] = headimgurl
    if suser:
      suser.first().set_password(str(unid))
      suser.first().nickname = nickname
      suser.first().headimgurl = headimgurl
      suser.first().save()
      username = suser.first().cellphone
      password = suser.first().wechatUNID
      user = authenticate(username=username, password=password)
      if user is not None and suser.first().group.role == 0:
        login(request, user)
        return redirect('/headquar/')
      elif user is not None and suser.first().group.role == 1:
        login(request, user)
        return redirect('/agent/')
      elif user is not None:
        login(request, user)
        return redirect('/scenic/')
    else:
      return redirect('/phoneAuth/')
  else:
    #raise Http404()
    return render(request,'account/login.html')

def bangding(request):
  phone = request.GET.get('phone')
  unid = request.session.get('unionid', True)
  nickname = request.session.get('nickname',True)
  headimgurl = request.session.get('headimgurl') 

  if phone:
    sphone = User.objects.filter(cellphone=phone)
    if sphone:
      if not sphone.first().wechatUNID:
        code = request.GET.get('code')
        vcode = request.session.get('vcode',True)
        if code == vcode:
          sphone.first().wechatUNID = str(unid)
          sphone.first().username = phone
          sphone.first().headimgurl = headimgurl
          sphone.first().nickname = nickname
          sphone.first().set_password(str(unid))
          sphone.first().save()
          use = authenticate(username=phone, password=str(unid))
          if use is not None:
            if sphone.first().group.role== 0:
              login(request, use)
              return HttpResponse('1')
            elif sphone.first().group.role == 1:
              login(request, use)
              return HttpResponse('2')
            else:
              login(request, use)
              return HttpResponse('3')
        else:
          return HttpResponse('no')
      else:
        return HttpResponse('error2')
    else:
      return HttpResponse('error')
  return render(request,'account/bangding.html')

def sms_send(request):
  phone = request.GET.get('phone')
  vcode = ''.join(random.sample('123456789', 4))
  sphone = User.objects.filter(cellphone=phone)
  if sphone:
    if not sphone.first().wechatUNID and len(sphone)==1:
      send = send_sms0(phone,'多倍通',vcode,'30')
      print send
      request.session['vcode'] = vcode
      return HttpResponse('ok')
    elif sphone.first().wechatUNID and len(sphone)==1:
      return HttpResponse('noone')
  else:
    return HttpResponse('nophone')

