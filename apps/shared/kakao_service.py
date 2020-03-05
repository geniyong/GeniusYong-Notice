import requests
import urllib.parse
import urllib.request
import json

from geniusYong_notice.conf.utils import get_private_info_value

# ##################################################
# POST with urllib.request
# # Data dict
# data = { 'test1': 10, 'test2': 20 }
#
# # Dict to Json
# # Difference is { "test":10, "test2":20 }
# data = json.dumps(data)
#
# # Convert to String
# data = str(data)
#
# # Convert string to byte
# data = data.encode('utf-8')
#
# # Post Method is invoked if data != None
# req = urllib.request.Request('', data=data)
# #####################################################

class KakaoService(object):
    url = "https://kapi.kakao.com"
    talk_profile_url = "https://kapi.kakao.com/v1/api/talk/profile"
    send_msg_to_me_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    unlink_url = url + "/v1/user/unlink"
    code_url = url+'/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code'.format(
        app_key = get_private_info_value("KAKAO")['REST_API_KEY'],
        redirect_uri="http://127.0.0.1:8000/"
    )
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_private_info_value("KAKAO")['ACCESS_TOKEN']
    }

    def talk_get_profile(self):
        request = urllib.request.Request(self.talk_profile_url, headers=self.header)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)

    def unlink_to_service(self):
        request = urllib.request.Request(self.unlink_url, headers=self.header, method="POST")
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)

    def send_msg_to_me(self):
        example_data = {
            "template_object": {
                "object_type": "text",
                "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
                "link": {
                    "web_url": "https://developers.kakao.com",
                    "mobile_web_url": "https://developers.kakao.com"
                },
                "button_title": "바로 확인"
            }
        }
        data = json.dumps(example_data)
        data = str(data)
        data = data.encode('utf-8')
        print(data)
        request = urllib.request.Request(self.send_msg_to_me_url, headers=self.header, data=data)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
            print(response.read())

# from apps.shared.kakao_service import *
# a=KakaoService()
# a.send_msg_to_me()