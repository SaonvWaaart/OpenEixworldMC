# -*- coding: utf-8 -*-
"""dialog — recovered from EixworldMC启动器 V1.7.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: scan@0x18d50
# unicode strings: 247   interned-from: 25

_STRINGS = (
    '#111111',
    '#2f6bd8',
    'None',
    'QMessageBox 的替身：同样的调用方式，换成卡片式弹窗。',
    '字符串常量，同时支持 `Yes | No` 这类按位或写法。',
    '.',
    '!',
    '×',
    ';\n                border-radius: 17px;\n                font-size: 18px;\n                font-weight: 900;\n            }\n            #dlgTitle {\n                color: ',
    '#c98a00',
    ';\n                color: ',
    '#d43a3a',
    '\n            #dlgCard {\n                background: #ffffff;\n                border: 1px solid #e8e8ec;\n                border-radius: 16px;\n            }\n            #dlgBadge {\n                background: ',
    '#eef3fd',
    '#f1f1f4',
    '#fdeceb',
    '#fdf5e4',
    ';\n                font-size: 17px;\n                font-weight: 800;\n            }\n            #dlgBody {\n                color: #3a3a42;\n                font-size: 13px;\n                font-weight: 600;\n            }\n            #dlgCap {\n                color: #6a6a72;\n                font-size: 12px;\n                font-weight: 700;\n            }\n            #dlgInput {\n                background: #ffffff;\n                color: #111111;\n                border: 1px solid #dcdce2;\n                border-radius: 8px;\n                padding: 0 10px;\n                font-size: 13px;\n                font-weight: 600;\n            }\n            #dlgInput:focus { border: 1px solid #111111; }\n            #dlgOk, #dlgGhost, #dlgDanger {\n                background: #ffffff;\n                color: #111111;\n                border: 1px solid #dcdce2;\n                border-radius: 9px;\n                font-size: 13px;\n                font-weight: 700;\n                padding: 0 16px;\n            }\n            #dlgOk:hover, #dlgGhost:hover, #dlgDanger:hover {\n                background: #f5f5f7;\n                border: 1px solid #c6c6ce;\n            }\n            #dlgOk:pressed, #dlgGhost:pressed, #dlgDanger:pressed {\n                background: #ececf0;\n            }\n            #dlgOk { border: 1px solid #111111; }\n            #dlgDanger { border: 1px solid #d43a3a; color: #d43a3a; }\n        ',
)


class CardDialog:
    def __init__(*args, **kwargs):
        ...

    def _qss(*args, **kwargs):
        ...

    def _on_ok(*args, **kwargs):
        ...

    def accept(*args, **kwargs):
        ...

    def mousePressEvent(*args, **kwargs):
        ...

    def mouseMoveEvent(*args, **kwargs):
        ...

    def mouseReleaseEvent(*args, **kwargs):
        ...

class _Btn:
    def __or__(*args, **kwargs):
        ...

    def __ror__(*args, **kwargs):
        ...

    def __and__(*args, **kwargs):
        ...

    def __rand__(*args, **kwargs):
        ...

class QMsgBox:
    def __init__(*args, **kwargs):
        ...

    def setWindowTitle(*args, **kwargs):
        ...

    def setText(*args, **kwargs):
        ...

    def setIcon(*args, **kwargs):
        ...

    def addButton(*args, **kwargs):
        ...

    def exec(*args, **kwargs):
        ...

    def _show(*args, **kwargs):
        ...

    def information(*args, **kwargs):
        ...

    def warning(*args, **kwargs):
        ...

    def critical(*args, **kwargs):
        ...

    def question(*args, **kwargs):
        ...

def __defaults__(*args, **kwargs):
    ...

class QInputDialogShim:
    def getText(*args, **kwargs):
        ...

def info(*args, **kwargs):
    ...

def warn(*args, **kwargs):
    ...

def error(*args, **kwargs):
    ...

def confirm(*args, **kwargs):
    ...

def ask_text(*args, **kwargs):
    ...
