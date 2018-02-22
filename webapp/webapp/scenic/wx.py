#coding:utf-8
from django.conf import settings
import json
import requests


"""获取公众号token以及刷新token"""
def get_token(obj):
  with open(settings.CONFIG2) as infile:
    config = json.load(infile)
  access_token = config.get("wechat",{}).get("access_token") 
  url = 'https://api.weixin.qq.com/cgi-bin/component/api_authorizer_token?component_access_token='+ access_token
  data = {
      "component_appid":'wxd9103590a61f46e0',
      "authorizer_appid":obj.authorizer_appid,
      "authorizer_refresh_token":obj.authorizer_refresh_token,
      }
  r = requests.post(url, json.dumps(data))
  access_token = eval(r.content)['authorizer_access_token']
  authorizer_refresh_token = eval(r.content)['authorizer_refresh_token']
  obj.authorizer_access_token = access_token
  obj.authorizer_refresh_token = authorizer_refresh_token
  obj.save()
