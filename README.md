# pyweibo

## Overview
API for weibo.com.

## Install
***目前尚未支持安装***
``` commandline
git clone https://github.com/heyaoyao/pyweibo.git
cd pyweibo
python setup.py install
```

## Requirements
rsa >= 3.4.2
lxml >= 3.7.3
Python2.7

## Documentation
### quick start
```python
from pyweibo.http import weibo_downloader
url = 'http://weibo.com/u/2662018234'
response = weibo_downloader.download(url)
```

## Classes
> ### class pyweibo.http.downloader.Downloader
微博的下载器，封装了requests
TODO: 添加download_delay和proxy支持
 
####***download()***

| 参数      | 类型     | 是否必需 | 描述                       |
| ------- | ------ | ---- | ------------------------ |
| url     | str    | 是    | 需要获取的页面链接                |
| headers | dict   | 否    | 请求头                      |
| data    | dict   | 否    | 在post时使用，表单域             |
| timeout | double | 否    | 下载超时时间                   |
| method  | str    | 否    | 下载方式，默认为                 |
| kwargs  | dict   | 否    | 其他参数选项，见requests.request |

> ### class pyweibo.parser.parse_response
微博页面解析器

> ### class pyweibo.selector.Selector
数据选择器，目前可以通过xpath定位数据

> ### class pyweibo.weibo.*
一些常用功能的实现

## Settings
未来添加自定义设置支持
