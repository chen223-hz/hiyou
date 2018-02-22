#coding:utf-8
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from webapp.scenic.models import * 
from webapp.manuf.manuf import *
import requests
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from django.db.models import Q


def render_api(data):
    response = HttpResponse(json.dumps(data, cls=DjangoJSONEncoder, indent=4), content_type='text/plain')
    response['Access-Control-Allow-Origin'] = '*'
    response['Contet-Type'] = 'text/plain'
    return response


@csrf_exempt
def get_phone(request):
    uid = json.loads(request.body)['pk']
    obj = Scenic.objects.filter(pk=uid).first()
    objs = None
    date = json.loads(request.body)['date']['date'][0]
    if date == 'today':
        date = datetime.date.today()
        objs = obj.census_set.filter(date__gt=date)
    elif date == 'yesterday':
        date = datetime.date.today()-datetime.timedelta(days=1)
        objs = obj.census_set.filter(date__gte=date)
        if not objs:
            data = {}
            data['msg'] = 'error2'
            return render_api(data)
    elif date == 'week':
        date = datetime.date.today()-datetime.timedelta(days=7)
        objs = obj.census_set.filter(date__gte=date)
        if not objs:
            data = {}
            data['msg'] = 'error2'
            return render_api(data)
    elif date == 'month':
        date = datetime.date.today()-datetime.timedelta(days=30)
        objs = obj.census_set.filter(date__gte=date)
        if not objs:
            data = {}
            data['msg'] = 'error2'
            return render_api(data)
    else:
        data = {}
        data['msg'] = 'error'
        return render_api(data)
    data = []
    temp = {}
    temp['vivo'] = 0
    temp['apple'] = 0
    temp['oppo'] = 0
    temp['huawei'] = 0
    temp['samsung'] = 0
    temp['other'] = 0
    for obj in objs:
        temp['vivo'] = temp['vivo']+obj.vivo
        temp['apple'] = temp['apple']+obj.apple
        temp['oppo'] = temp['oppo']+obj.oppo
        temp['huawei'] = temp['huawei']+obj.huawei
        temp['samsung'] = temp['samsung']+obj.samsung
        temp['other'] = temp['other']+obj.other
    data.append(temp)
    return render_api(data)

@csrf_exempt
def get_visitor(request):
    uid = json.loads(request.body)['pk']
    date = json.loads(request.body)['date']['date'][0]
    obj = Scenic.objects.filter(pk=uid).first()
    objs = None
    if date == 'week':
        objs = obj.census_set.filter(date__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by('date')
    elif date == 'month':
        objs = obj.census_set.filter(date__gte=datetime.date.today()-datetime.timedelta(days=30)).order_by('date')
    temp = []
    for objs in objs:
        data = {}
        num = objs.vivo+objs.apple+objs.huawei+objs.samsung+objs.other
        date = objs.date.strftime('%m-%d')
        data['num'] = num
        data['date'] = date
        temp.append(data)
    time = []
    for aa in temp:
        time.append(aa['date'])
    time = list(set(time))
    qwe = []
    for cc in time:
        asd = {}
        num = 0
        for bb in temp:
            if bb['date'] == cc:
                num = num+bb['num']
        asd['date'] = cc
        asd['num'] = num
        qwe.append(asd)
    qwe.sort(key=lambda x:x["date"])
    return render_api(qwe)

@csrf_exempt
def get_area(request):
    uid = json.loads(request.body)['pk']
    obj = Scenic.objects.filter(pk=uid).first()
    objs = obj.area_set.filter(zhu=0)
    data = []
    for o in objs:
        temp = {}
        temp['name'] = o.name
        temp['num'] = o.num
        data.append(temp)
    return render_api(data)    

@csrf_exempt
def get_new(request):
    uid = json.loads(request.body)['pk']
    date = json.loads(request.body)['date']['date'][0]
    obj = Scenic.objects.filter(pk=uid).first()
    objs = None
    if date == 'today':
    	objs = obj.newo_set.filter(date=1).first()
    elif date == 'yesterday':
    	objs = obj.newo_set.filter(date=-1).first()
    elif date == 'week':
    	objs = obj.newo_set.filter(date=7).first()
    elif date == 'month':
    	objs = obj.newo_set.filter(date=30).first()
    data = {}
    data['new'] = objs.xin
    data['old'] = objs.lao
    return render_api(data)

@csrf_exempt
def get_sex(request):
    uid = json.loads(request.body)['pk']
    obj = Scenic.objects.filter(pk=uid).first()
    objs = obj.userinfo_set.all()
    data = {}
    man = []
    woman = []
    unknow = []
    for p in objs:
      if p.sex == 1:
        man.append(p)
      elif p.sex == 2:
        woman.append(p)
    data['man'] = len(man)
    data['woman'] = len(woman)
    return render_api(data)

@csrf_exempt
def get_num(request):
    uid = json.loads(request.body)['pk']
    obj = Scenic.objects.filter(pk=uid).first()
    objs = obj.area_set.filter(zhu=False)
    num = 0
    for objs in objs:
        num = num+objs.num
    numall = len(list(set(cache.get('usertoday'+str(uid)))))
    data = {}
    data['num_now'] = num
    data['num_all'] = numall
    return render_api(data)