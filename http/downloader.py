# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:11

author @heyao
"""

import re
import socket
import requests
from urllib import urlencode

from http.response import Response
from selector.selector import Selector


class Downloader(object):
    def __init__(self, cookie_enable=False):
        self.cookie_enable = cookie_enable
        self.reg = re.compile(r"charset=(.*?)")
        self.cookie_dict = {}

    def download(self, url, headers=None, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, method='GET', **options):
        headers = headers or {}
        if data:
            method = 'POST'
        headers['User-Agent'] = 'Baiduspider'  # to avoid SVS
        options.update(dict(
            headers=headers,
            data=data,
            timeout=timeout,
        ))
        if self.cookie_enable:
            options.update(dict(
                cookies=self.cookie_dict
            ))
        response = requests.request(method, url, **options)
        self._cookie_format(response.cookies)
        response_obj = Response(response)
        sel = Selector(text=response.text)
        text = response.text
        setattr(response_obj, "text", text)
        setattr(response_obj, "content", response.content)
        encoding_str = sel.xpath('//meta[contains(@content, "charset")]/@content').extract_first()
        if encoding_str:
            encoding = self.reg.search(encoding_str).group(1)
            if encoding:
                setattr(response_obj, "encoding", encoding)
                text.decode(encoding, 'ignore')
        setattr(response_obj, "body", text)
        return response_obj

    def _cookie_format(self, cookies):
        for cookie in cookies:
            name = cookie.name
            self.cookie_dict[name] = cookie.value
        return urlencode(self.cookie_dict).replace('&', ';')


if __name__ == '__main__':
    downloader = Downloader(True)
    data = {
        'loginName': 15647238472,
        'loginPwd': 123,
        'qqCode': '',
        'sCookie': '',
        'imgcode': 26,
        'rnd': 0.45617345410825316,
    }
    response_post = downloader.download('http://www.xxsy.net/login/doLogin', data=data)
    pass
