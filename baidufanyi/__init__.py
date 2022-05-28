import requests
import random
import json
from hashlib import md5

class BaiduFanyi:
    def __init__(self, appid, appkey):
        self.appid = appid
        self.appkey = appkey
        endpoint = 'https://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        self.url = endpoint + path

    def _make_md5(self, s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self, text, fromLang="auto", toLang="zh"):
        query = text
        salt = random.randint(32768, 65536)
        sign = self._make_md5(self.appid + query
                              + str(salt) + self.appkey)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': self.appid, 'q': query, 'from': fromLang,
                   'to': toLang, 'salt': salt, 'sign': sign}

        r = requests.post(self.url, params=payload, headers=headers)
        result_json = json.loads(r.text)
        result_list = []
        for result in result_json["trans_result"]:
            result_list.append(result['dst'])
        return "\n".join(result_list)
