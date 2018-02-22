#coding:utf-8
from django import forms
import datetime
import re
from .models import *
from webapp.scenic.models import *
from webapp.account.models import *

class CameoForm(forms.Form):
  def as_cameo(self):
    "Returns this form rendered as HTML <p>s."
    return self._html_output(
      normal_row='''<div class="form-group">
        <div class="col-sm-3 control-label">%(label)s</div>
        <div class="col-sm-9">%(field)s%(help_text)s</div>
      </div>''',
      error_row='%s',
      row_ender='</div>',
      help_text_html=' <span class="helptext">%s</span>',
      errors_on_separate_row=True)

class ScenicForm(CameoForm):
  name = forms.CharField(label=u'景区名称', 
  	  help_text='不能超过32个中文字',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':u'请输入代理商名称'}))

  username = forms.CharField(label=u'手机账号',
  	  help_text='登录账号必须为11位数字',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':u'手机账号'}))

  def __init__(self, *args, **kwargs):
    self.instance = kwargs.pop('instance')
    super(ScenicForm, self).__init__(*args, **kwargs)  

  def clean_name(self):
    name = self.cleaned_data.get('name','')
    if len(name)>96:
      raise forms.ValidationError(u'用户名超过32个中文!')
    if Scenic.objects.filter(name=name):
      raise forms.ValidationError(u'用户名已存在!')
    return name

  def clean_username(self):
    username = self.cleaned_data.get('username','')
    p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    if not p.match(username):
      raise forms.ValidationError(u'手机账号不是11位数字!')
    if User.objects.filter(cellphone=username):
      raise forms.ValidationError(u'手机账户已存在!')
    return username

  def save(self):
    obj = Group.objects.get(pk=self.instance.gaent.pk)
    objs = obj.children.all()
    if objs:
      ob = objs.filter(name=self.cleaned_data['name'])
      if ob:
        o = ob.first()
      else:
        o = Group.objects.create(role=2,name=self.cleaned_data['name'],parent=obj)
    else:
      o = Group.objects.create(role=2,name=self.cleaned_data['name'],parent=obj)

    u = Scenic.objects.create(name=self.cleaned_data['name'],group=o,agent=self.instance)
    User.objects.create(cellphone=self.cleaned_data['username'],group=o)

class SceniccForm(CameoForm):
  name = forms.CharField(label=u'代理商名称', 
      help_text='不能超过32个中文字',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':u'请输入代理商名称'}))

  def __init__(self, *args, **kwargs):
    self.instance = kwargs.pop('instance')
    self.sign = kwargs.pop('sign')
    super(SceniccForm, self).__init__(*args, **kwargs)  

  def clean_name(self):
    name = self.cleaned_data.get('name','')
    if len(name)>96:
      raise forms.ValidationError(u'用户名超过32个中文!')
    if Scenic.objects.filter(name=name):
      if not self.sign:
        raise forms.ValidationError(u'用户名已存在!')
    return name

  def save(self):
    obj = Scenic.objects.get(name=self.instance.name)
    obj.name = self.cleaned_data['name']
    obj.save()

class Scenic_userForm(CameoForm):
  username = forms.CharField(label=u'手机账号',
      help_text='登录账号必须为11位数字',
      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':u'手机账号'}))

  def __init__(self, *args, **kwargs):
    self.instance = kwargs.pop('instance')
    super(Scenic_userForm, self).__init__(*args, **kwargs)  

  def clean_username(self):
    username = self.cleaned_data.get('username','')
    p=re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    if not p.match(username):
      raise forms.ValidationError(u'手机账号不是11位数字!')
    if User.objects.filter(cellphone=username):
      raise forms.ValidationError(u'手机账户已存在!')
    return username

  def save(self):
    obj = User.objects.create(cellphone=self.cleaned_data['username'],group=self.instance)

  
