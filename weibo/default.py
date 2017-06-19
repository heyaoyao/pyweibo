# -*- coding: utf-8 -*-
"""
create on 2017-06-19 上午12:40

author @heyao
"""

VERSION = 'v1.4.18'

API = dict(
    PRE_LOGIN='https://login.sina.com.cn/sso/prelogin.php?'
              'entry=weibo&callback=sinaSSOController.preloginCallBack&su=&'
              'rsakt=mod&client=ssologin.js({version})%s'.format(version=VERSION) % '&_={timestamp}',
    LOGIN='http://login.sina.com.cn/sso/login.php?client=ssologin.js({version})'.format(version=VERSION),
    USER_HOME='http://weibo.com/{user_id}/profile?'
              'is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={page}#feedtop'
)

FORMDATA = dict(
    LOGIN={
        "entry": "weibo",
        "gateway": "1",
        "from": "",
        "savestate": "7",
        "useticket": "1",
        "pagerefer": "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F",
        "vsnf": "1",
        "su": '',
        "service": "miniblog",
        "servertime": '',
        "nonce": '',
        "pwencode": "rsa2",
        "rsakv": '',
        "sp": '',
        "sr": "1280*800",
        "encoding": "UTF-8",
        "url": "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "META"
    }
)
