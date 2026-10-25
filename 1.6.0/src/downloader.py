# -*- coding: utf-8 -*-
"""downloader — recovered from EixworldMC启动器 V1.6.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: scan@0x21720
# unicode strings: 203   interned-from: 32

_STRINGS = (
    '.',
    'Content-Length',
    'Content-Range',
    'Content-Type',
    'Mozilla/5.0 EixWorld',
    'SHA1 校验失败（期望 ',
    'User-Agent',
    '）',
    '下载失败: ',
    '/',
    '-',
    '探测失败: ',
    '合并失败: ',
    '源返回了网页（可能被拦截）',
    '，实际 ',
    'bangbang93.com',
    'bytes=',
    'bytes=0-0',
    'bytes=%d-',
    'mcimirror.top',
    '.part',
    'text/html',
    'timed out',
    '.tmp',
    'ustc.edu.cn',
)


def set_profile(*args, **kwargs):
    ...

def profile_workers(*args, **kwargs):
    ...

def _chunk_threads(*args, **kwargs):
    ...

def _open_url(*args, **kwargs):
    ...

def _is_html_response(*args, **kwargs):
    ...

def sha1_file(*args, **kwargs):
    ...

def download(*args, **kwargs):
    ...

def _probe_ranges(*args, **kwargs):
    ...

def _cleanup_parts(*args, **kwargs):
    ...

def download_chunked(*args, **kwargs):
    def make_cb(*args, **kwargs):
        def _f(*args, **kwargs):
            ...

    def get_part(*args, **kwargs):
        ...
