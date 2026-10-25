# -*- coding: utf-8 -*-
"""titlebar — recovered from EixworldMC启动器 V1.7.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: scan@0xd980
# unicode strings: 131   interned-from: 8

_STRINGS = (
    '.',
    '#2a2a2a',
    '#e81123',
    '#e8e8ec',
    '#ffffff',
    '\n            #titlebar { background: transparent; }\n            #titleLabel {\n                color: #333333;\n                font-size: 13px;\n                font-weight: 800;\n            }\n            #winBtn {\n                background: transparent;\n                border: none;\n            }\n            #winBtnClose {\n                background: transparent;\n                border: none;\n            }\n        ',
)


class WinButton:
    def __init__(*args, **kwargs):
        ...

    def enterEvent(*args, **kwargs):
        ...

    def leaveEvent(*args, **kwargs):
        ...

    def paintEvent(*args, **kwargs):
        ...

class TitleBar:
    def __init__(*args, **kwargs):
        ...

    def _init_ui(*args, **kwargs):
        ...

    def mousePressEvent(*args, **kwargs):
        ...

    def mouseMoveEvent(*args, **kwargs):
        ...

    def mouseReleaseEvent(*args, **kwargs):
        ...
