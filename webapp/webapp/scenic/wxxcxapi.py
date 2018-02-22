#coding:utf-8
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from .models import Wxusername
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from django.core.cache import cache
from webapp.account.views import _get_wx_api
import base64
from Crypto.Cipher import AES
import base64
import urllib, urllib2, sys
from lxml import etree
######################################### V I P ###############################################################
def render_api(data):
    response = HttpResponse(json.dumps(data, cls=DjangoJSONEncoder, indent=4), content_type='text/plain')
    response['Access-Control-Allow-Origin'] = '*'
    response['Contet-Type'] = 'text/plain'
    return response

def get_name(request):
    sid = request.GET.get('ScienicID')
    stype = request.GET.get('ScienicType')
    data = []
    if sid and stype:
        obj = Scenic.objects.filter(pk=sid).first()
        objs = obj.point_set.all()
        for obj in objs:
            temp = {}
            temp['MarkerId'] = obj.pk
            temp['MarkerName'] = obj.name
            temp['MarkerType'] = obj.facilities_point.name
            temp['MarkerTypeId'] = obj.facilities_point.pk
            temp['MarkerLng'] = str(eval(obj.latitude)[0])
            temp['MarkerLat'] = str(eval(obj.latitude)[1])
            data.append(temp)
    else:
        obj = Scenic.objects.filter(isdel=0)
        for obj in obj :
            temp = {}
            temp['ScenicName'] = obj.name
            temp['ScenicId'] = obj.pk
            data.append(temp)
    return render_api(data)


def get_facilities(request):
    obj = Facilities.objects.all()
    data = []
    if request.GET.get('MarkerTypeId') and request.GET.get('ScenicId'):
        tid = request.GET.get('MarkerTypeId')
        sid = request.GET.get('ScenicId')
        a = Facilities.objects.filter(pk=tid).first()
        b = Scenic.objects.filter(pk=sid).first()
        obj = Point.objects.filter(Q(facilities_point=a)&Q(scenic_point=b))
        for obj in obj:
            data.append({"MarkerId":obj.pk,"MarkerName":obj.name,"MarkerType":a.name,"MarkerTypeId":a.pk,"MarkerLng":str(eval(obj.latitude)[0]),"MarkerLat":str(eval(obj.latitude)[1])})
    else:
        for obj in obj:
            data.append({"TypeId":obj.pk,"TypeName":obj.name})
    return render_api(data)

@csrf_exempt
def get_point(request):
    mid = request.POST.get('MarkerId')
    lng = request.POST.get('MarkerLng')
    lat = request.POST.get('MarkerLat')
    data = {}
    if not mid or not lng or not lat:
        data['result'] = "error"
        data['msg'] = "请求失败"
        return HttpResponse(json.dumps(data))
    obj = Point.objects.filter(pk=mid).first()
    if not obj:
        data['result'] = "error"
        data['msg'] = "ID不存在"
        return HttpResponse(json.dumps(data))
    if obj:
        lt = []
        lt.append(float(lng))
        lt.append(float(lat))
        obj.latitude = lt 
        obj.save()
        data['result'] = "success"
    else:
        data['result'] = "error"
        data['msg'] = "数据库修改失败"
    return HttpResponse(json.dumps(data))

@csrf_exempt
def add_point(request):
    sid = request.POST.get('ScenicId')
    mname = request.POST.get('MarkerName')
    tid = request.POST.get('TypeId')
    mlng = request.POST.get('MarkerLng')
    mlat = request.POST.get('MarkerLat')
    data = {}
    if not sid or not mname or not tid or not mlng or not mlat:
        data['result'] = "error"
        data['msg'] = "请求失败"
        return HttpResponse(json.dumps(data))
    obj = Scenic.objects.filter(pk=sid).first()
    if not obj:
        data['result'] = "error"
        data['msg'] = "ScenicID不存在"
        return HttpResponse(json.dumps(data))
    if not Facilities.objects.filter(pk=tid).first():
        data['result'] = "error"
        data['msg'] = "typeID不存在"
        return HttpResponse(json.dumps(data))
    if obj and Facilities.objects.filter(pk=tid).first():
        lt = []
        lt.append(float(mlng))
        lt.append(float(mlat))
        pd = Point.objects.create(latitude=lt,facilities_point=Facilities.objects.filter(pk=tid).first(),scenic_point=obj,name=mname)
        data['result'] = "success"
        data['MarkerId'] = pd.pk
    else:
        data['result'] = "error"
        data['msg'] = "数据库修改失败"
    return HttpResponse(json.dumps(data))

@csrf_exempt
def del_point(request):
    mid = request.POST.get('MarkerId')
    data = {}
    if mid:
        obj = Point.objects.filter(pk=mid).first()
        if obj:
            obj.delete()
            data['result'] = "success"
        else:
            data['result'] = "error"
            data['msg'] = "MarkerId不存在"
        return HttpResponse(json.dumps(data))
    else:
        data['result'] = "error"
        data['msg'] = "请输入正确MarkerId"
        return HttpResponse(json.dumps(data))

########################################################################################################################

def search_point(request):
    pid = request.GET.get('MarkerId')
    unionid = request.GET.get('Unionid')
    code = request.GET.get('Wxid')
    url ='https://api.weixin.qq.com/sns/jscode2session?appid=wx65423a2f6908bc55&secret=3aad35233c0a762172f38b8f1d92630f&js_code=%s&grant_type=authorization_code'
    objs = None
    if code:
        url = url % code
        response = _get_wx_api(url)
        if response.has_key('errcode') and response["errcode"] == 40029:
            return render_api([{'text':'on'}])
        # 没有access_token也跳回首页
        unionid = response['unionid']
        objs = Wxusername.objects.filter(wxid=unionid)
    else:
        if unionid:
            objs = Wxusername.objects.filter(wxid=unionid[2:len(unionid)-8])
    obj = Point.objects.filter(pk=pid).first()
    data = []
    if obj:
        page = etree.HTML(obj.text.lower())
        ps = page.xpath(u"//p")
        imgs = page.xpath(u"//img")
        da = []
        for p in ps:
            temp = {}
            if p.text:
                temp['content'] = p.text
                temp['type'] = 'text'
                da.append(temp)

        for img in imgs:
            temp = {}
            temp['src'] = img.attrib['src']
            temp['type'] = 'img'
            da.append(temp)

        data.append({"MarkerName":obj.name,"MarkerLng":str(eval(obj.latitude)[0]),"MarkerLat":str(eval(obj.latitude)[1]),"MarkerText":da})

        if obj.video:
            data[0]["MarkerVideo"]="http://hiyoutest.doublecom.net/uploads/"+str(obj.video)
        if obj.image:
            data[0]["MarkerImg"]="http://hiyoutest.doublecom.net/uploads/"+str(obj.image)
        if objs:
            for o in objs.first().wxscenic_set.all():
                if o.point.pk == int(pid):
                    data[0]['unionid'] = 'false'
    else:
        data = {}
        data['result'] = "error"
        data['msg'] = "数据库修改失败"
    return render_api(data)

def weather(request):
    sid  = request.GET.get('pk') 
    data = [{'weather': cache.get(str(sid)+'t')},{'uptime':cache.get(str(sid)+'time')}]
    return render_api(data)

@csrf_exempt
def wxusername(request):
    opintid = request.POST.get('MarkerId')  
    code = request.POST.get('Wxid') 
    encryptedData = request.POST.get('encryptedData')
    signature = request.POST.get('signature')
    iv = request.POST.get('iv')
    url ='https://api.weixin.qq.com/sns/jscode2session?appid=wx65423a2f6908bc55&secret=3aad35233c0a762172f38b8f1d92630f&js_code=%s&grant_type=authorization_code'

    if code:
        url = url % code
        response = _get_wx_api(url)
        if response.has_key('errcode') and response["errcode"] == 40029:
            return render_api([{'text':'on'}])
        # 没有access_token也跳回首页
        print response

        pc = WXBizDataCrypt('wx65423a2f6908bc55', response['session_key'])
        respon = pc.decrypt(encryptedData, iv)
        unionId = respon['unionId']
        name = respon['nickName']
        point = Point.objects.get(pk=int(opintid))
        unid = 'wx' + unionId + 'nickname'
        sign = 0
        if Wxusername.objects.filter(wxid=unionId):
            wxuser = Wxusername.objects.get(wxid=unionId)
            for oo in wxuser.wxscenic_set.all():
                if oo.point.pk == int(opintid):
                    sign = 1
                    oo.delete()
            if not sign:
                Wxscenic.objects.create(point=point,wxuser=wxuser)
        else:
            obj = Wxusername.objects.create(name=name,wxid=unionId)
            Wxscenic.objects.create(point=point,wxuser=obj)
        return render_api([{'text':'yes','unionid':unid,'sign':sign}])
    return render_api([{'text':'no'}])


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

def collection(request):
    unionid = request.GET.get('Unionid')
    code = request.GET.get('Wxid')
    print code
    url ='https://api.weixin.qq.com/sns/jscode2session?appid=wx65423a2f6908bc55&secret=3aad35233c0a762172f38b8f1d92630f&js_code=%s&grant_type=authorization_code'
    objs = None
    if code:
        url = url % code
        response = _get_wx_api(url)
        if response.has_key('errcode') and response["errcode"] == 40029:
            return render_api([{'text':'on'}])
        # 没有access_token也跳回首页
        unionid = response['unionid']
        objs = Wxusername.objects.filter(wxid=unionid)
    else:
        objs = Wxusername.objects.filter(wxid=unionid[2:len(unionid)-8])
    data = []
    print objs
    if objs:
        for o in objs.first().wxscenic_set.all():
            temp = {}
            temp['id'] = o.point.pk
            temp['name'] = o.point.name
            data.append(temp)
    return render_api(data)

@csrf_exempt
def distinguish(request):
    img_base64=''
    faces = ''
    for chunk in request.FILES['plantImage'].chunks():
        faces = faces + chunk
    img_base64=base64.b64encode(faces)
    host = 'http://plantgw.nongbangzhu.cn'
    path = '/plant/recognize'
    method = 'POST'
    appcode = '57f728c2e73c4c36a010abdebd9411a8'
    querys = ''
    bodys = {}
    url = host + path
    bodys['img_base64']=img_base64
    post_data = urllib.urlencode(bodys)
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        return render_api(eval(content))
    else:
        return render_api([{'text':'on'}])