#coding:utf-8
from django import forms
from .models import *

class ScenicForm(forms.ModelForm):
  class Meta:
    model = Scenic
    fields = ('num', )