#coding:utf-8
import re

def isMac(addr):
  #if isinstance(addr, unicode): return False
  if not addr: return False
  if not re.match(r'^[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}$',addr):
    return False
  return True

def isDomain(domain):
  if not domain: return False
  if not re.match(r'^[a-z0-9]([a-z0-9-]+\.){1,}[a-z0-9]+\Z', domain):
    return False
  return True
