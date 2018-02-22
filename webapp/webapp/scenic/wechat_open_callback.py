#coding:utf-8
# Last modified: 2017-05-02 14:02:04
# by zhangdi http://jondy.net/
from Crypto.Cipher import AES
import base64
import socket
import struct
import xml.etree.cElementTree as ET
import requests
import json
import traceback

class WXDCrypt(object):
  """docstring for ClassName"""
  def __init__(self, key):
    self.key = key.decode('base64')

  def decrypt(self, from_xml):
    """docstring for decrypt"""
    xml_tree = ET.fromstring(from_xml)
    encrypt = xml_tree.find("Encrypt")
    text = encrypt.text
    cryptor = AES.new(self.key,AES.MODE_CBC,self.key[:16])
    plain_text  = cryptor.decrypt(base64.b64decode(text))

    pad = ord(plain_text[-1])
    # 去掉补位字符串
    #pkcs7 = PKCS7Encoder()
    #plain_text = pkcs7.encode(plain_text)
    # 去除16位随机字符串
    content = plain_text[16:-pad]
    xml_len = socket.ntohl(struct.unpack("I",content[ : 4])[0])
    xml_content = content[4 : xml_len+4]
    from_appid = content[xml_len+4:]
    return xml_content

  def get_ticket(self, from_xml):
    xml = self.decrypt(from_xml)
    xml_tree = ET.fromstring(xml)
    encrypt = xml_tree.find("ComponentVerifyTicket")
    if encrypt!='None' and encrypt!= None:
      text = encrypt.text
      return (text,'c')
    else:
      encrypt = xml_tree.find("InfoType")
      text = encrypt.text
      return (text,'i')

  def get_appid(self, from_xml):
    xml = self.decrypt(from_xml)
    xml_tree = ET.fromstring(xml)
    encrypt = xml_tree.find("AuthorizerAppid")
    text = encrypt.text
    return text



  def get_access_token(self, ticket):
    # 用于获取第三方平台令牌（component_access_token）
    url = 'https://api.weixin.qq.com/cgi-bin/component/api_component_token'
    data = {
        "component_appid": self.appid,
        "component_appsecret": self.appsecret,
        "component_verify_ticket": ticket,
      }
    try:
      r = requests.post(url, json.dumps(data))
      j = r.json()
      access_token = j["component_access_token"]
    except:
      access_token = ''
      traceback.print_exc()
    return access_token

  def get_pre_auth_code(self, access_token):
    # 获取预授权码
    url = 'https://api.weixin.qq.com/cgi-bin/component/api_create_preauthcode?component_access_token=' + access_token
    data = {
        "component_appid": self.appid,
      }
    try:
      r = requests.post(url, json.dumps(data))
      j = r.json()
      pre_code = j["pre_auth_code"].replace('\n', '').strip()
    except:
      pre_code = ''
      traceback.print_exc()
    return pre_code

if __name__ == '__main__':
  token = "SD9falXdfadDDFLK31"
  nonce = "319509210"
  appid = "wxf9732a54ef9911b8"                                                                                                          
  timestamp = "1449384070"
  msg_sign  = "d0a66d964cb22d8c72587973290d614d85c0c439"
  key = 'd8yoIawV43BehQFFRf0jBer1qsRwzQdjusEv1I3paYU'+'='

  from_xml = """<xml>
  <AppId><![CDATA[wxf9732a54ef9911b8]]></AppId>
  <Encrypt><![CDATA[gEKQV7xd5wHHtBEgRr7Ln5RIZ62hDd//+U3pQESZTULw4HddZs/yMws6qsnTAU/nD8sMJJH49fK0iXENg2ti8ilOD+GuxhyxCKdHPPrpG/AkE+4zYabFDpGovGPlsgaPYIyZJjcRFDs31k28OzfDKDUMqtUPLkumcInTjFCaUtmtHCJ/H96wkZQAi36iMxEUpKTxc+cT1T2QloD4CPIQFdLjfUshE9amqBmHXHy166muVjTzLqQZgw6dAOmDWBEajOZsIeK+S6deULe5VvZbffu0H5mIaw5C52hV7WoVPlQs0ByffoYVFQpQrjKS0xUPd4jhX0OXLm11S9ZSmhNxXqfiug/BQhe24xWXPKB9LI/qlJnO/c5yXuSIxIQfq8vACbS4VggdwlIuCPnMIIfeOLF7/9+6Ex47zR+gcIJ24vEX+LUf3QiZwx88rlRMy0N0ap/EJj+EupoC8+i1IuMTZQ==]]></Encrypt>
  </xml>"""
  from_xml= '''<xml>
      <AppId><![CDATA[wxf9732a54ef9911b8]]></AppId>
          <Encrypt><![CDATA[w9v5xnfvk2NwOH2Yzn8ot7Lw+cJ9ZTbH9M/vG5LOFjQu+nPm2lNQnmKZXGRh65sdY5EEj2r3NduqwitQK86q5wH/UNFOaz0eZRRKTxi4ICGomKhjNj1TBQm/9AIRKpyD1JdB4O1/HB3ugFRPXfuCUA77LKmuRxAvx9T13Ogta/BCm/iJOlM3atf/Lj2zRWxvRqJ0IaLlpyXAE6adpqGdaREGPL+w0xWnfupirLbFpL1EvftXkspadEbSVSkhOlc6ynBkWx9CbquqmpWTu3fsHAwkVB8gm6y7qF1e3CLDmAI6POj4GSP+XsPJkgCzAOFNXXFPZeSqLI/vqUiQODh7Cw==]]></Encrypt>
          </xml>
          '''

  a = WXDCrypt(key)
  a.appid = appid
  a.appsecret = 'fc97b52cb69ed3c6105150b4a4c2b5d5'
  #a.token = token
  #a.nonce = nonce
  #a.timestamp = timestamp
  #a.msg_sign = msg_sign
  #print a.decrypt(from_xml)
  #ticket = a.get_ticket(from_xml)
  #access_token = a.get_access_token(ticket)
  #pre_code = a.get_pre_auth_code(access_token)
  #print pre_code
  print a.decrypt(from_xml)
