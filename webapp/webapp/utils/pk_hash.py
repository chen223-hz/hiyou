#coding:utf-8
# Last modified: 2016-05-03 18:06:15
# by zhangdi http://jondy.net/
from hashids import Hashids
from django.conf import settings

def get_encrypt(pk):
  hashids = Hashids(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', salt=settings.HASHIDS_KEY)
  hashid = hashids.encrypt(pk)
  return hashid

def get_decrypt(hashid):
  hashids = Hashids(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', salt=settings.HASHIDS_KEY)
  return hashids.decrypt(hashid)[0]
