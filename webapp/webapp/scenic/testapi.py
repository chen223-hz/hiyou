#coding:utf-8
''' api test '''
import json
import requests

#domain = 'localhost:8000'
domain = 'dev.api.doublecom.net'

aus_api_url = 'http://%s/api/aus' % domain
rosap_api_url = 'http://%s/api/rosap' % domain

def call_api(url, data):
    r = requests.post(url, json.dumps(data))
    return r.content

def get_aus_status():
    ''' 获取设备状态，参数为mac地址列表'''
    data = {
        'action': 'getlist',
        'macaddr': ['40:e0:b4:80:ef:0f']
    }
    print call_api(aus_api_url, data)

def get_aus_update_file(source_url,dst_filename,mac):
    '''通知认证服务器更新文件'''
    data = {
        'action': 'fetch_file',
        'macaddr': mac,
        'source_url': source_url,
        'dst_path': '/hotspot/',
        'dst_filename': dst_filename,
    }
    return call_api(aus_api_url, data)

def rosap_reboot():
    '''通知ap设备重启，参数mac地址'''
    data = {
        'action': 'reboot',
        'macaddr': '6C:3B:6B:4D:E5:C8'
    }
    print call_api(rosap_api_url, data)

def rosap_setssid():
    '''通知ap设备重启，参数mac地址'''
    data = {
        'action': 'set_wireless_ssid',
        'macaddr': '6C:3B:6B:4D:E5:C8',
        'ssid': 'testyanfa'
    }
    print call_api(rosap_api_url, data)

	
def aus_deauth(mac,target):
    ''' 认证服务器上强制用户离线 '''
    data = {
        'action': 'deauth',
        'macaddr': mac,  # 认证服务器mac
        'target': target  # 被离线的mac
    }
    print call_api(aus_api_url, data)
	

if __name__ == '__main__':
    rosap_reboot()
    #rosap_setssid()
    # get_rosap()
