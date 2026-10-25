# -*- coding: utf-8 -*-
"""msa_auth — recovered from EixworldMC启动器 V1.7.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: scan@0x14dc0
# unicode strings: 181   interned-from: 45

_STRINGS = (
    '）',
    'Bearer ',
    'Content-Type',
    '该微软账号没有 Minecraft（未购买或未关联）',
    '正在换取 Minecraft 令牌...',
    'Mozilla/5.0 EixWorld/0.1.0',
    'User-Agent',
    'XBL3.0 x=',
    'XSTS 授权失败（',
    '正在获取 XSTS 令牌...',
    'XSTS 授权失败（XErr=',
    '正在获取 Xbox 令牌...',
    'XboxLive.signin offline_access',
    ' 并输入代码 ',
    '登录代码已过期，请重试',
    '登录失败（',
    '等待授权超时，请重试',
    '正在获取玩家档案...',
    '所在国家/地区不可用',
    ';',
    '正在向微软请求登录代码...',
    '请在浏览器打开 ',
    'application/json',
    'application/x-www-form-urlencoded',
    'c36a9fb6-4f2a-41ff-90bd-ae7cc92031eb',
    'd=',
    'http://auth.xboxlive.com',
    'https://api.minecraftservices.com/authentication/login_with_xbox',
    'https://api.minecraftservices.com/minecraft/profile',
    'https://login.microsoftonline.com/',
    'https://user.auth.xboxlive.com/user/authenticate',
    'https://www.microsoft.com/link',
    'https://xsts.auth.xboxlive.com/xsts/authorize',
    '/oauth2/v2.0/devicecode',
    '/oauth2/v2.0/token',
    'rp://api.minecraftservices.com/',
    'urn:ietf:params:oauth:grant-type:device_code',
    'user.auth.xboxlive.com',
)


def _post_form(*args, **kwargs):
    ...

def _post_json(*args, **kwargs):
    ...

def _get_json(*args, **kwargs):
    ...

def device_code_start(*args, **kwargs):
    ...

def token_poll(*args, **kwargs):
    ...

def refresh(*args, **kwargs):
    ...

def xbox_live_auth(*args, **kwargs):
    ...

def xsts_auth(*args, **kwargs):
    ...

def minecraft_login(*args, **kwargs):
    ...

def minecraft_profile(*args, **kwargs):
    ...

def __defaults__(*args, **kwargs):
    ...

def full_login(*args, **kwargs):
    ...
