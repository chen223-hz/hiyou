#coding:utf-8
from django.core.management.base import BaseCommand,CommandError 
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from webapp.scenic.models import * 
from webapp.api.views import *
from webapp.manuf.manuf import * 
import requests
import datetime
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        aa = None
        label = None
        while True:
            filename = '/home/www/hiyoutest/logs/tanz.log'
            data = []
            aa = open(filename,'r')
            if cache.get('label'):
                try:
                    aa.seek(cache.get('label'),0)
                except:
                    pass
            while True:
                line = aa.readline()
                label = aa.tell()
                aa.seek(label,0)
                data.append(line)
                if not line:
                    break
            ##按景区存
            obj = Scenic.objects.filter(isdel=0)
            scenic = {}
            p = MacParser()
            today = datetime.datetime.today().strftime('%Y-%m-%d')
            for obj in obj:
                scenic['name'+str(obj.pk)] = {}
                objs = obj.dev_set.filter(dev_type='1',isonline=1)
                qwe = []
                for objs in objs:
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)] = {}
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other'] = []
                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['macaddr'] = objs.macaddr
                    for ww in data:
                        try:
                            typ = self.mac_type(p,eval(ww)['mac'])
                            if eval(ww)['macaddr'] == objs.macaddr:
                                if typ == 'vivo':
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo'].append(eval(ww)['mac'])
                                elif typ == 'apple':
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple'].append(eval(ww)['mac'])
                                elif typ == 'huawei':
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei'].append(eval(ww)['mac'])
                                elif typ == 'oppo':
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo'].append(eval(ww)['mac'])
                                elif typ == 'samsung':
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung'].append(eval(ww)['mac'])
                                else:
                                    scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other'].append(eval(ww)['mac'])
                                qwe.append(eval(ww)['mac'])
                        except:
                            pass
                    if not cache.get('tztoday'):
                        Census.objects.create(scenic=obj,dev=objs,vivo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo']))),apple=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple']))),huawei=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei']))),oppo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo']))),samsung=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung']))),other=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other']))))
                    else:
                        ww = Census.objects.filter(scenic=obj,dev=objs).first()
                        if cache.get('tztoday')['name'+str(ww.scenic.pk)].has_key('dev'+str(ww.dev.pk)) == False:
                            ww.delete()
                            Census.objects.create(scenic=obj,dev=objs,vivo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo']))),apple=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple']))),huawei=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei']))),oppo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo']))),samsung=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung']))),other=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other']))))             
                        else:
                            if ww.date < datetime.datetime.strptime(today, "%Y-%m-%d"):
                                Census.objects.create(scenic=obj,dev=objs,vivo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo']))),apple=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple']))),huawei=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei']))),oppo=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo']))),samsung=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung']))),other=len(list(set(scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other']))))
                            else:
                                ww.vivo = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['vivo']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo'])))
                                ww.apple = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['apple']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple'])))
                                ww.huawei = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['huawei']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei'])))
                                ww.oppo = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['oppo']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo'])))
                                ww.samsung = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['samsung']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung'])))
                                ww.other = len(list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['other']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other'])))
                                ww.save()
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['vivo'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['vivo']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['vivo']))
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['apple'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['apple']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['apple']))
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['huawei'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['huawei']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['huawei']))
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['oppo'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['oppo']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['oppo']))
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['samsung'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['samsung']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['samsung']))
                                scenic['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['other'] = list(set(cache.get('tztoday')['name'+str(ww.scenic.pk)]['dev'+str(ww.dev.pk)]['other']+scenic['name'+str(obj.pk)]['dev'+str(objs.pk)]['other']))
                nn = []
                for sz in scenic['name'+str(obj.pk)]:
                    for sz2 in sz:
                        for sz3 in sz2:
                            nn.append(sz3)
                ##################今天新老用户####################
                tt = list(set(qwe))
                pp = []
                ll = cache.get('usertoday'+str(obj.pk))
                if ll:
                    for kk in tt:
                        if kk not in ll:
                            pp.append(kk)
                uu = []
                ob = Client.objects.filter(scenic_id=obj.pk)
                for ob in ob:
                    uu.append(ob.mac)
                uu = list(set(uu))
                if pp:
                    new = len(list(set(uu+pp)))-len(uu)
                    old = len(pp) - new
                else:
                    new = len(list(set(tt+uu)))-len(uu)
                    old = len(tt) - new
                if not Newo.objects.filter(scenic_id=obj.pk,date=1):
                    Newo.objects.create(scenic=obj,xin=new,lao=old,date=1)
                    cache.set('usertoday'+str(obj.pk),tt,12*60*60)
                else:
                    oo = Newo.objects.filter(scenic_id=obj.pk,date=1).first()
                    if oo.update>datetime.datetime.strptime(today, "%Y-%m-%d"):
                        oo.xin = oo.xin+new
                        oo.lao = oo.lao+old
                        cache.set('usertoday'+str(obj.pk),ll+pp,12*60*60)
                    else:
                        cache.delete('usertoday'+str(obj.pk))
                        oo.xin = new
                        oo.lao = old
                        cache.set('usertoday'+str(obj.pk),tt,12*60*60)
                    oo.save()
                ##################昨天新老用户####################
                tt = Client.objects.filter(scenic_id=obj.pk,statrtime__lt=today,statrtime__gte=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 1))
                rr = []
                uu = []
                for tt in tt:
                    rr.append(tt.mac)
                rr = list(set(rr))
                ob = Client.objects.filter(scenic_id=obj.pk,statrtime__lt=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 1))
                for ob in ob:
                    uu.append(ob.mac)
                uu = list(set(uu))
                new = len(list(set(rr+uu)))-len(uu)
                old = len(rr)-new
                if not Newo.objects.filter(scenic_id=obj.pk,date=-1):
                    Newo.objects.create(scenic=obj,xin=new,lao=old,date=-1)
                else:
                    oo = Newo.objects.filter(scenic_id=obj.pk,date=-1).first()
                    oo.xin = new
                    oo.lao = old
                    oo.save()
                ################一周新老用户######################
                tt = Client.objects.filter(scenic_id=obj.pk,statrtime__gte=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 6))
                rr = []
                uu = []
                for tt in tt:
                    rr.append(tt.mac)
                rr = list(set(rr+nn))
                ob = Client.objects.filter(scenic_id=obj.pk,statrtime__lte=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 6))
                for ob in ob:
                    uu.append(ob.mac)
                uu = list(set(uu))
                new = len(list(set(rr+uu)))-len(uu)
                old = len(rr)-new
                if not Newo.objects.filter(scenic_id=obj.pk,date=7):
                    Newo.objects.create(scenic=obj,xin=new,lao=old,date=7) 
                else:
                    cc = Newo.objects.filter(scenic_id=obj.pk,date=7).first()
                    cc.xin = new
                    cc.lao = old
                    cc.save()
                ###############一个月新老用户#####################
                tt = Client.objects.filter(scenic_id=obj.pk,statrtime__gte=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 29))
                rr = []
                uu = []
                for tt in tt:
                    rr.append(tt.mac)
                rr = list(set(rr+nn))
                ob = Client.objects.filter(scenic_id=obj.pk,statrtime__lt=datetime.datetime.strptime(today, "%Y-%m-%d")-datetime.timedelta(days = 29))
                for ob in ob:
                    uu.append(ob.mac)
                uu = list(set(uu))
                new = len(list(set(rr+uu)))-len(uu)
                old = len(rr)-new
                if not Newo.objects.filter(scenic_id=obj.pk,date=30):
                    Newo.objects.create(scenic=obj,xin=new,lao=old,date=30)
                else:
                    bb = Newo.objects.filter(scenic_id=obj.pk,date=30).first()
                    bb.xin = new
                    bb.lao = old
                    bb.save()
            today = datetime.datetime.today().strftime('%Y-%m-%d')
            if Census.objects.all() and Census.objects.order_by("date").last().date>datetime.datetime.strptime(today, "%Y-%m-%d"):
                cache.set('tztoday',scenic,12*60*60)
                cache.set('label',label,12*60*60)
            else:
                cache.delete('tztoday')
                cache.delete('label')
            aa.close()
            time.sleep(5*60)

    def mac_type(self,p,key):
        typ = ''
        ty = p.get_manuf(key)
        if ty:
            if 'HuaweiTe' in ty: typ = 'huawei'
            elif 'OppoDigi' in ty:
                typ = 'oppo'
            elif 'VivoMobi' in ty:
                typ = 'vivo'
            elif 'SamsungE' in ty: typ = 'samsung'
            elif 'Apple' in ty: typ = 'apple'
            else: typ = 'other'
        return typ
