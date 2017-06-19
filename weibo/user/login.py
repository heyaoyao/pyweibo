# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:40

author @heyao
"""

import re
import binascii
from time import time
from urllib2 import quote
from copy import deepcopy

from utils.basen import bnencode
from utils.rsa_ import Rsa
from http import weibo_downloader
from weibo.default import API, FORMDATA
from parser.parse_response import parse_pre_login, parse_user_info


def redirect(text):
    reg = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
    redirect_url = reg.search(text).group(1)
    return redirect_url


def login(username, password, vcode=None):
    pre_url = API['PRE_LOGIN'].format(timestamp=int(time()))
    response = weibo_downloader.download(pre_url)
    login_params, pubkey = parse_pre_login(response)

    login_data = FORMDATA['LOGIN']
    username = _username_encode(username)
    password = _password_encrypt(password, login_params, pubkey)
    login_data.update(dict(
        su=username,
        sp=password
    ))
    login_data.update(login_params)

    login_url = API['LOGIN']
    headers = {
        "Host": "login.sina.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Referer": "http://weibo.com/",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = weibo_downloader.download(login_url, data=login_data, headers=headers)
    redirect_url = redirect(response.body)
    redirect_response = weibo_downloader.download(redirect_url)
    user_info = parse_user_info(redirect_response)
    return user_info['userinfo']['uniqueid'], user_info['userinfo']['userdomain']


def _username_encode(username):
    return bnencode(quote(username))


def _password_encrypt(password, login_params, n16):
    rsa_cryptor = Rsa()
    pubkey = rsa_cryptor.key_from_n16(n16)
    msg_data = deepcopy(login_params)
    msg_data.update(dict(
        password=password
    ))
    message = '{servertime}\t{nonce}\n{password}'.format(**msg_data)
    return binascii.b2a_hex(rsa_cryptor.encrypt(message, pubkey))


if __name__ == '__main__':
    username = ''
    password = ''
    user_id, user_domain = login(username, password)
    user_url = API['USER_HOME'].format(user_id=user_id, page=1)
    response = weibo_downloader.download(user_url)
    cookie = weibo_downloader.cookie_dict
    ind = response.body.find(u'我的主页')
    pass
