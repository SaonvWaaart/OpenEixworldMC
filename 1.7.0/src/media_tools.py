# -*- coding: utf-8 -*-
"""media_tools — recovered from EixworldMC启动器 V1.7.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: scan@0x201a0
# unicode strings: 278   interned-from: 32

_STRINGS = (
    ' ',
    '.1f',
    ' B',
    ' GB',
    'None',
    '\n            QDialog { background: #ffffff; }\n            #mtTitle { color:#111111; font-size:18px; font-weight:800; }\n            #mtSub { color:#9a9aa2; font-size:12px; font-weight:600; }\n            #mtGhost {\n                background:#ffffff; color:#555555;\n                border:1px solid #e2e2e6; border-radius:8px;\n                font-size:12px; font-weight:700;\n            }\n            #mtGhost:hover { background:#f7f7f8; }\n            #mtPrimary {\n                background:#111111; color:#ffffff; border:none;\n                border-radius:8px; font-size:12px; font-weight:700;\n            }\n            #mtPrimary:hover { background:#2a2a2a; }\n            #shotList {\n                background:#fafafa; border:1px solid #ececf0;\n                border-radius:10px; padding:6px;\n            }\n            #shotPreview {\n                background:#fafafa; border:1px solid #ececf0;\n                border-radius:10px; color:#b0b0b8;\n                font-size:12px; font-weight:600;\n            }\n        ',
    '\n            QDialog { background: #ffffff; }\n            #mtTitle { color:#111111; font-size:18px; font-weight:800; }\n            #mtSub { color:#9a9aa2; font-size:12px; font-weight:600; }\n            #mtGhost {\n                background:#ffffff; color:#555555;\n                border:1px solid #e2e2e6; border-radius:8px;\n                font-size:12px; font-weight:700;\n            }\n            #mtGhost:hover { background:#f7f7f8; }\n            #mtPrimary {\n                background:#111111; color:#ffffff; border:none;\n                border-radius:8px; font-size:12px; font-weight:700;\n            }\n            #mtPrimary:hover { background:#2a2a2a; }\n            #shotList {\n                background:#fafafa; border:1px solid #ececf0;\n                border-radius:10px; padding:6px;\n                font-size:13px; color:#333333;\n            }\n        ',
    '%Y%m%d-%H%M%S',
    '共 ',
    ' 张',
    '确定删除 ',
    '？',
    '存档备份 - ',
    '截图 - ',
    ' 个备份',
    ' · 没有存档文件夹',
    '    ·    ',
    '还原会先自动备份当前存档，然后用所选备份覆盖。\n继续吗？',
    '.',
    '.bmp',
    '.jpeg',
    '.jpg',
    '.png',
    '这个版本还没有 saves 文件夹：\n',
    '.zip',
)


def _client(*args, **kwargs):
    ...

def _open(*args, **kwargs):
    ...

def _fmt_size(*args, **kwargs):
    ...

class ScreenshotDialog:
    def __init__(*args, **kwargs):
        ...

    def _build(*args, **kwargs):
        ...

    def reload(*args, **kwargs):
        ...

    def _on_pick(*args, **kwargs):
        ...

    def _delete(*args, **kwargs):
        ...

class BackupDialog:
    def __init__(*args, **kwargs):
        ...

    def _build(*args, **kwargs):
        ...

    def reload(*args, **kwargs):
        ...

    def _open_folder(*args, **kwargs):
        ...

    def _create(*args, **kwargs):
        ...

    def _restore(*args, **kwargs):
        ...

    def _delete(*args, **kwargs):
        ...
