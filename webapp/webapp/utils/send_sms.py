#coding:utf-8
# Last modified: 2016-02-02 10:10:19
# by zhangdi http://jondy.net/
from django.conf import settings
import urllib
import requests
import hashlib
import datetime

# 3位毫秒
#microsecond = int(datetime.datetime.now().microsecond*1e-3)
def send_sms0(to, name, vcode, timeout, tmpl='37752', appid=settings.UCPAAS_APPID):
  url = 'http://www.ucpaas.com/maap/sms/code'
  TIME = datetime.datetime.now().strftime('%Y%m%d%H%M%S000')
  params = {
      'sid': settings.UCPAAS_SID,
      'appId': appid,
      # 验证信息，使用MD5加密（账户id+时间戳+账户授权令牌），共32位（小写）
      'sign': hashlib.md5(settings.UCPAAS_SID+TIME+settings.UCPAAS_TOKEN).hexdigest(),
      'time': TIME,
      'templateId': tmpl,
      'to': to,
      'param': vcode,#','.join([vcode,timeout])
    }
  req = requests.get(url, params=params)
  try:
    return req.json()
  except:
    return req.json

# 华兴软通
def send_sms1(to, name, vcode, timeout, tmpl=None):
  url = u"http://www.stongnet.com/sdkhttp/sendsms.aspx?reg=101100-WEB-HUAX-274655&pwd=QTTMMFLL&sourceadd=&phone=%s&content=您的验证码为%s【多倍通】" % (to, vcode)
  req = requests.get(url)
  return {'resp': {'respCode':'000000'}}
