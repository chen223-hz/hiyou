#coding:utf-8
# Last modified: 2017-10-16 17:05:54
# by zhangdi http://jondy.net/
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.db.models.signals import post_save
from webapp.agent.models import *
from PIL import Image
import datetime
import json
from webapp.account.models import *
from ckeditor.fields import RichTextField
import time

def image_filename(instance, filename):
  n = timezone.now()
  ext = filename.split('.').pop().lower()
  return 'image/%s%s/%s/%s%s%s%s.%s' % (n.year,n.month,n.day,n.hour,n.minute,n.second,n.microsecond,ext)

  
def video_filename(instance, filename):
  n = timezone.now()
  ext = filename.split('.').pop().lower()
  return 'video/%s%s/%s/%s%s%s%s.%s' % (n.year,n.month,n.day,n.hour,n.minute,n.second,n.microsecond,ext)  


class Scenic(models.Model):
  name =models.CharField(max_length=512,blank=True, null=True)
  num = models.IntegerField(u'最大人数',null=True,blank=True)
  isdel = models.BooleanField(default=False)
  pub_date = models.DateTimeField(auto_now_add=True, editable = True)
  update_time = models.DateTimeField(auto_now=True, null=True)
  latitude = models.TextField(null=True,blank=True)
  authorizer_appid = models.CharField(max_length=512,blank=True,null=True)
  authorizer_access_token = models.CharField(max_length=512,blank=True,null=True)
  authorizer_refresh_token = models.CharField(max_length=512,blank=True,null=True)
  nick_name = models.CharField(max_length=512,blank=True,null=True)
  head_img = models.CharField(max_length=512,blank=True,null=True)
  shop_id = models.CharField(max_length=512,blank=True,null=True)
  shop_index = models.CharField(max_length=512,blank=True,null=True)
  mendian_name = models.CharField(max_length=512,blank=True,null=True)
  qrcode_url = models.CharField(max_length=512,blank=True,null=True)
  secretkey = models.CharField(max_length=512,blank=True,null=True)
  ssid = models.CharField(max_length=512,blank=True,null=True)
  template_id = models.CharField(max_length=512,blank=True,null=True)
  data = models.TextField(null=True,blank=True)
  probe = models.TextField(null=True,blank=True)
  agent = models.ForeignKey(Agent, null=True)
  group = models.ForeignKey(Group, null=True)

  class Meta:
    ordering = ['-id']

	
class UserInfo(models.Model):
  mac = models.CharField(max_length=512,blank=True,null=True)
  openid = models.CharField(max_length=512,blank=True,null=True)
  nickname = models.CharField(max_length=512,blank=True,null=True)
  sex = models.IntegerField(u'性别',null=True,blank=True)
  city = models.CharField(max_length=512,blank=True,null=True)
  country = models.CharField(max_length=512,blank=True,null=True)
  province = models.CharField(max_length=512,blank=True,null=True)
  headimgurl = models.CharField(max_length=512,blank=True,null=True)
  subscribe_time = models.CharField(max_length=512,blank=True,null=True)
  fbl = models.CharField(max_length=512,blank=True, null=True)
  update = models.DateTimeField(auto_now=True, null=True)
  scenic = models.ForeignKey(Scenic, null=True)

  class Meta:
    ordering = ['-id']

class Region(models.Model):
  name = models.CharField(max_length=512, blank=True, default='-')
  latitude = models.TextField(null=True)
  pub_date = models.DateTimeField(auto_now_add=True, editable = True,null=True)
  update_time = models.DateTimeField(auto_now=True, null=True)
  num = models.IntegerField(null=True,blank=True)
  scenic_region = models.ForeignKey(Scenic, null=True)

  class Meta:
    ordering = ['-id']

	
class Fenlei(models.Model):
  name = models.CharField(max_length=512, blank=True, default='-')
  
  class Meta:
    ordering = ['-id']


class Text(models.Model):
  num = models.IntegerField(blank=True,null=True)
  name = models.CharField(max_length=512, blank=True, default='-')
  direct = models.CharField(max_length=512, blank=True, default='-')
  update_time = models.DateTimeField(auto_now=True, null=True)
  scenic_text = models.ForeignKey(Scenic, null=True)

  
  class Meta:
    ordering = ['num']
	

class TextContent(models.Model):
  num = models.IntegerField(blank=True,null=True)
  title = models.CharField(max_length=512, blank=True, default='-')
  text = RichTextField(null=True)
  image = models.ImageField(upload_to=image_filename,null=True,blank=True)
  update_time = models.DateTimeField(auto_now=True, null=True)
  scenic_text = models.ForeignKey(Text, null=True)

  
  class Meta:
    ordering = ['num']



class Facilities(models.Model):
  name = models.CharField(max_length=512, blank=True, default='-')
  map_icon = models.ImageField(upload_to=image_filename,null=True,blank=True)
  list_icon = models.ImageField(upload_to=image_filename,null=True,blank=True)
  leixing = models.ForeignKey(Fenlei,null=True)
  
  class Meta:
    ordering = ['-id']

  def get_img(self):
      if self.map_icon:
          im = Image.open(self.map_icon)
          im.thumbnail((20, 20))
          im.save('./uploads/'+str(self.map_icon))
          return 


class Point(models.Model):
  name = models.CharField(max_length=512, blank=True, default='-')
  latitude = models.TextField(null=True,blank=True)
  image = models.ImageField(upload_to=image_filename,null=True,blank=True)
  video = models.FileField(upload_to=video_filename,null=True,blank=True)
  text = RichTextField(null=True)
  facilities_point = models.ForeignKey(Facilities, null=True)
  scenic_point = models.ForeignKey(Scenic, null=True)
  pub_date = models.DateTimeField(auto_now_add=True, editable = True,null=True)
  update_time = models.DateTimeField(auto_now=True, null=True)
  
  class Meta:
    ordering = ['-id']

	
class Area(models.Model):
  name = models.CharField(max_length=512, blank=True, default='-')
  latitude = models.TextField(null=True,blank=True)
  scenic_area = models.ForeignKey(Scenic, null=True)
  zhu = models.BooleanField(default=False)
  num = models.IntegerField(null=True,blank=True)

  class Meta:
    ordering = ['-id']	
	

class Domain(models.Model):
  latitude = models.TextField(null=True)
  area_domain = models.ForeignKey(Area, null=True)
  scenic_domain = models.ForeignKey(Scenic, null=True)

  class Meta:
    ordering = ['-id']	
	

class Wxusername(models.Model):
  name  = models.CharField(max_length=100, blank=True, default='-')
  wxid  = models.CharField(max_length=150, blank=True, default='-')

  class Meta:
    ordering = ['-id']	

class Wxscenic(models.Model):
  point = models.ForeignKey(Point, null=True)
  wxuser = models.ForeignKey(Wxusername, null=True)

  class Meta:
    ordering = ['-id']	

class Dev(models.Model):
  version  = models.CharField(max_length=50, blank=True, default='-')
  ssid = models.CharField(max_length=512,blank=True,null=True)
  macaddr = models.CharField(max_length=20)
  time_dev = models.CharField(max_length=500,blank=True,null=True)
  isonline = models.BooleanField(blank=True, default=False)
  pub_date = models.DateTimeField(auto_now_add=True, editable = True)
  online_time = models.CharField(max_length=500,blank=True,null=True)
  dev_type = models.CharField(max_length=400)
  latitude = models.CharField(max_length=512, null=True,blank=True, default='-')
  isdel = models.BooleanField( blank=True, default=False)
  scenic_dev = models.ForeignKey(Scenic, null=True)
  region_dev = models.ForeignKey(Region, null=True)
  agent_dev = models.ForeignKey(Agent, null=True)
  remarks = models.CharField(max_length=512, null=True,blank=True,)
  class Meta:
    ordering = ['-id']
  
  def get_type(self):
    if self.dev_type == '0':
      return 'AP'
    if self.dev_type == '1':
      return '探针'
    if self.dev_type == '2':
      return '认证服务器'
    else:
      return '-'
      
  def get_time(self):
    if not self.isonline:
      if self.online_time:
        tim = time.mktime(datetime.datetime.now().timetuple())-float(self.online_time)
        day = tim/(24*3600)
        shour = tim%(24*3600)/3600
        sminute = tim%(24*3600)%3600/60
        return '离线'+' '+str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'
      else:
        return '-'
    else:  
      if self.dev_type == '1' and self.time_dev:
        tim = time.mktime(datetime.datetime.now().timetuple())-float(self.time_dev)
        day = tim/(24*3600)
        shour = tim%(24*3600)/3600
        sminute = tim%(24*3600)%3600/60
        return '在线'+' '+str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'
      if self.dev_type == '0' and self.time_dev:
        tim = int(self.time_dev)
        day = tim/(24*3600)
        shour = tim%(24*3600)/3600
        sminute = tim%(24*3600)%3600/60
        return '在线'+' '+str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'
      if self.dev_type == '2' and self.time_dev:
        tim = int(self.time_dev)
        day = tim/(24*3600)
        shour = tim%(24*3600)/3600
        sminute = tim%(24*3600)%3600/60
        return '在线'+' '+str(int(day))+'天'+str(int(shour))+'小时'+str(int(sminute))+'分'



class Visitor(models.Model):
  mac = models.CharField(max_length=512,blank=True, null=True)
  openId = models.CharField(max_length=512,blank=True, null=True)
  tid = models.CharField(max_length=512,blank=True, null=True)
  isdel = models.BooleanField(blank=True, default=False)

  class Meta:
    ordering = ['-id']

class Tanz(models.Model):
  mac = models.CharField(max_length=512,blank=True, null=True)
  create = models.CharField(max_length=512,blank=True, null=True)
  num = models.IntegerField(null=True,blank=True)
  scenic = models.ForeignKey(Scenic, null=True)
  
  class Meta:
    ordering = ['-id']

# shard_tables = {}
# class ShardMixin():
#     @classmethod
#     def shard(cls):
#       today = datetime.datetime.today() 
#       ext = (today + datetime.timedelta(-1)).strftime('%Y%m%d')
#       _db_table = "%s%s" % (cls._meta.db_table , ext)  # 分表表名
#       if _db_table not in shard_tables:
#         class Meta:
#           db_table = _db_table
#         attrs = {
#           '__module__': cls.__module__,
#           'Meta': Meta,
#         }
#         shard_tables[_db_table] = type("%s%s" % (cls.__name__, ext), (cls, ), attrs)
#       return shard_tables[_db_table]

class Client(models.Model):
  mac = models.CharField(max_length=512,blank=True, null=True)
  statrtime = models.DateTimeField(null=True)
  endtime = models.DateTimeField(null=True)
  signal = models.CharField(max_length=512,blank=True, null=True)
  num = models.IntegerField(null=True,blank=True)
  typee = models.CharField(max_length=512,blank=True, null=True)
  tanz = models.ForeignKey(Tanz, null=True)
  scenic = models.ForeignKey(Scenic, null=True)
   
  class Meta:
    # abstract = True
    # db_table = "client_"
    ordering = ['-id']

class Census(models.Model):
    vivo = models.IntegerField(null=True,blank=True)
    apple = models.IntegerField(null=True,blank=True)
    oppo = models.IntegerField(null=True,blank=True)
    huawei = models.IntegerField(null=True,blank=True)
    samsung = models.IntegerField(null=True,blank=True)
    other = models.IntegerField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True, null=True)
    scenic = models.ForeignKey(Scenic, null=True)
    dev = models.ForeignKey(Dev, null=True)

    class Meta:
        ordering = ['-id']

class Newo(models.Model):
    xin = models.IntegerField(null=True,blank=True)
    lao = models.IntegerField(null=True,blank=True)
    scenic = models.ForeignKey(Scenic, null=True)
    date = models.IntegerField(null=True,blank=True)
    update = models.DateTimeField(auto_now=True, null=True)

class Commodity_Group(models.Model):
    name = models.CharField(max_length=512,blank=True, null=True)
    grounding = models.IntegerField(null=True,blank=True)
    date = date = models.DateTimeField(auto_now=True, null=True)
    scenic = models.ForeignKey(Scenic, null=True)

class Commodity(models.Model):
    name = models.CharField(max_length=512,blank=True, null=True)
    price = models.CharField(max_length=512,null=True,blank=True)
    price_old = models.CharField(max_length=512,null=True,blank=True)
    image = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    stock = models.IntegerField(null=True,blank=True)
    sales = models.IntegerField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True, null=True)
    grounding = models.CharField(max_length=512,blank=True, default=False)
    scenic = models.ForeignKey(Scenic, null=True)
    group = models.CharField(max_length=512,null=True)

    class Meta:
        ordering = ['-id']