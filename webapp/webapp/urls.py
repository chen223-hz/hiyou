#coding:utf-8
# Last modified: 2018-01-11 09:09:53
# by zhangdi http://jondy.net/
"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webapp.utils.decorator_include import decorator_include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #登录
    # url(r'^$','webapp.account.views.wxlogin'),
    #url(r'^$','webapp.account.views.fake_wxlogin'),
    url(r'^$','webapp.account.views.fake_wxlogin2'),

    url(r'^phoneAuth/','webapp.account.views.bangding'),
    url(r'^sms/','webapp.account.views.sms_send'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),

	#公众号API
    url(r'^agent/gzh_message/$','webapp.agent.views.wechat'),
    url(r'^scenic/gzh_message/$','webapp.scenic.views.wechat'),
    url(r'^receive_eventmessage/(\w+)/$','webapp.scenic.views.eventmessage'),
    #公众号授权
    url(r'^receive_sysmessage/$','webapp.scenic.views.weixin_callback'),
    url(r'^wechat/$','webapp.scenic.views.wechat3pt'),
    url(r'^wechat/success/$', 'webapp.scenic.views.wechat3pt_success'),
    #登录认证
    url(r'^ausv(\d+)/rlogin/$', 'webapp.scenic.views.rlogin'),
    url(r'^ausv/loginc/$', 'webapp.scenic.views.loginc'),
    url(r'^ausv(\d+)/login/$', 'webapp.scenic.views.check'),
    url(r'^ausvpc(\d+)/login/$', 'webapp.scenic.views.check2'),
    url(r'^ausvpc(\d+)/alogin/$', 'webapp.scenic.views.connect'),
    url(r'^ausv(\d+)/alogin/$', 'webapp.scenic.views.portal'),
    url(r'^wxwifirz/$', 'webapp.scenic.views.wxwifirz'),
    
    url(r'^scenic/change/$','webapp.scenic.views.changeurl'),
    
    url(r'^nogz/(\w+)/$','webapp.scenic.views.nogz'),
    #设备定位
    url(r'^location/$', 'webapp.agent.views.location'),
    url(r'^coordinate/$', 'webapp.agent.views.coordinate'),
    url(r'^mac/$', 'webapp.agent.views.mac'),
    url(r'^mac_location/$', 'webapp.agent.views.mac_location'),

    #小程序支付
    url(r'^macc/$', 'webapp.agent.views.macc'),
    
    url(r'^headquar/', decorator_include(login_required, 'webapp.headquar.urls')),

    url(r'^agent/', decorator_include(login_required, 'webapp.agent.urls')),
	url(r'^cck/', 'webapp.agent.views.sceneImgUpload'),

    url(r'^scenic/', decorator_include(login_required, 'webapp.scenic.urls')),

    url(r'^api/', decorator_include(login_required, 'webapp.api.urls')),
	#临时用
    url(r'^pay/','webapp.agent.views.pay'),
    url(r'^line/','webapp.api.views.line'),

    url(r'^appapi/', include('webapp.appapi.urls')),

    url(r'^admin/$', include(admin.site.urls)),
	#vip
	url(r'^wxAppToolApi/getScenicNames', 'webapp.scenic.wxxcxapi.get_name'),
	url(r'^wxAppToolApi/getScienicType', 'webapp.scenic.wxxcxapi.get_facilities'),
	url(r'^wxAppApi/setScenicPos', 'webapp.scenic.wxxcxapi.get_point'),
	url(r'^wxAppApi/addScenicMarker', 'webapp.scenic.wxxcxapi.add_point'),
	url(r'^wxAppApi/delScenicMarker', 'webapp.scenic.wxxcxapi.del_point'),
	
	#hepei
	url(r'^wxAppToolApi/searchPoint/', 'webapp.scenic.wxxcxapi.search_point'),
	url(r'^wxAppToolApi/getweather/', 'webapp.scenic.wxxcxapi.weather'),
	url(r'^wxAppToolApi/Wxusername/', 'webapp.scenic.wxxcxapi.wxusername'),
	url(r'^wxAppToolApi/Collection/', 'webapp.scenic.wxxcxapi.collection'),
	url(r'^wxAppToolApi/Distinguish/', 'webapp.scenic.wxxcxapi.distinguish'),
	
	
	#daping
	url(r'^daping/getPhone/', 'webapp.api.daping.get_phone'),
	url(r'^daping/getVisitor/', 'webapp.api.daping.get_visitor'),
	url(r'^daping/getArea/', 'webapp.api.daping.get_area'),
	url(r'^daping/getNew/', 'webapp.api.daping.get_new'),
	url(r'^daping/getSex/', 'webapp.api.daping.get_sex'),
	url(r'^daping/getNum/', 'webapp.api.daping.get_num'),
]

