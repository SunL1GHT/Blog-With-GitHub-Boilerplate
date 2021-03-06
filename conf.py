# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Glog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "SunL1GHT/Glog@gh-pages"
}

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "Qfx7wPzFC0seMwMOD4EjMXAm-9Nh9j0Va",
    "appKey": "isein6ywuR67g1GTcKYVRodg",
}


# 站点设置
site_name = "三缄其口 | 九九帰一"
site_logo = "${static_prefix}slogan.png"
background_img = "${static_prefix}fushihui.jpg"
site_build_date = "2020-02-10T16:51+08:00"
author = "Gary"
email = "Garygu9426@gmail.com"
author_homepage = "http://SunL1GHT.github.io/glog"
description = "永远相信美好的事情即将发生。"
key_words = [ '人生自留地', '黑暗森林', '我来自过去']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
       {
        "name": "摘引",
        "url": "${site_prefix}archives/箴言晓录/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/Gary0Gu",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/SunL1GHT",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/3182176652/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />

<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
'''

footer_addon = ''

body_addon = ''
