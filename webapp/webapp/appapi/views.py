#coding:utf-8
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from webapp.scenic.models import *
from .models import found_item

def render_api(data):
    response = HttpResponse(json.dumps(data, cls=DjangoJSONEncoder, indent=4), content_type='text/plain')
    response['Access-Control-Allow-Origin'] = '*'
    response['Contet-Type'] = 'text/plain'
    return response

def home(request):
    obj = Scenic.objects.get(pk=13)
    objs = Facilities.objects.all()
    data = {}
    for obj in objs:
        data[obj.name]=[]
        for obj2 in Scenic.objects.get(pk=13).point_set.filter(facilities_point=obj.pk):
            lng = str(eval(obj2.latitude)[0])
            lat = str(eval(obj2.latitude)[1])
            data[obj.name].append({'lng':eval(obj2.latitude)[0],
                'lat':eval(obj2.latitude)[1],
                'url':"/luxian/view/"+lng+"/"+lat+"/",
                'name':obj2.name,
                'summary': u'这个坐标的简介',
                'img': 'http://hiyoutest.doublecom.net/uploads/'+str(obj2.image),
                'icon':'http://hiyoutest.doublecom.net/uploads/'+str(obj2.facilities_point.map_icon),
                'href1': u'介绍',
                'href1link': u'/xiangqing/',
                'href2': u'',
                'href2link': u'',
                'href3': u'到这里去',
                'href3link': u'/luxian/view/%s/%s/' % (lng, lat),
            })
    return render_api(data)

def rim_index(request):
    obj = Fenlei.objects.all()
    data = {}
    for obj in obj:
        data[obj.name]=[]
        for obj2 in obj.facilities_set.all():
            data[obj.name].append({'title':obj2.name,
                'icon':'http://hiyoutest.doublecom.net/uploads/'+str(obj2.list_icon),
                'href':'/card/view/%s/' %(obj2.name),
                })
    return render_api(data)

def found_view(request, target):
    data = found_item.get(target, {
        "title": target,
        "content": "hehe"
    })
    return render_api(data)

def found_index(request):
    data = {
        "imgbtn2": [
            {
                "title": "米奇大街",
                "img": "http://appdata.doublecom.net/hiyou/found/miqi.jpg",
                "href": "/content/view/found/miqi/"
            },
            {
                "title": "奇想花园",
                "img": "http://appdata.doublecom.net/hiyou/found/qixiang.jpg",
                "href": "/content/view/found/qixiang/"
            },
            {
                "title": "梦幻世界",
                "img": "http://appdata.doublecom.net/hiyou/found/menghuan.jpg",
                "href": "/content/view/found/menghuan/"
            }
        ],
        "imgbtn3": [
            {
                "title": "《狮子王》演出",
                "img": "http://appdata.doublecom.net/hiyou/found/shiziwang.jpg",
                "href": "/content/view/found/shiziwang/"
            },
            {
                "title": "水上游玩",
                "img": "http://appdata.doublecom.net/hiyou/found/shuishang.jpg",
                "href": "/content/view/found/shuishang/"
            }
        ]
    }
    return render_api(data)

def cards_index(request):
    obj = Scenic.objects.get(pk=13)
    objs = Facilities.objects.all()
    objss = obj.point_set.all()
    data = {}
    for obj in objs:
        data[obj.name]={}
        data[obj.name]['title'] = Scenic.objects.get(pk=13).name
        data[obj.name]['cards'] = []
        for obj2 in objss:
            data[obj.name]['cards'].append({"img":"http://hiyoutest.doublecom.net/uploads/"+str(obj2.image),
                "title":obj2.name,
                "summary":"summary",
                "btn1":"详情",
                "href1":"/content/view/gaikuang/menghuan/",
                "btn2":"语音详解",
                "href2":"http://hiyoutest.doublecom.net/uploads/"+str(obj2.video),
                "btn3":"路线导航",
                "href3":"/luxian/view/莘东置业大厦/虹桥机场/"},
                )
    return render_api(data)
