# Recovered from PyInstaller archive of EixworldMC启动器 V1.7.0
# Entry script was real Python 3.13 bytecode (not Cython). V1.7.0 main.pyc
# decompiles to the same script as V1.6.0: same names, constants and control flow.
import os
import sys

import ctypes
import glob
import hashlib
import hmac
import json
import platform
import queue
import random
import re
import shutil
import socket
import stat
import subprocess
import tempfile
import threading
import time
import urllib.parse
import urllib.request
import uuid
import xml
import zipfile

try:
    import winreg
except Exception:
    pass

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, qInstallMessageHandler
from PyQt6.QtGui import QFont, QIcon
from eix_config import load_settings, get_base_dir
from ui import MainWindow
import welcome
from splash import Splash


def _qt_message(mode, context, message):
    if "qt.qpa.fonts" in message and "DirectWrite" in message:
        return
    if "QFont::setPointSize" in message:
        return
    try:
        if sys.stderr is not None:
            sys.stderr.write(message + "\n")
    except Exception:
        return


def _crash_log(exc_type, exc, tb):
    try:
        import traceback
        from eix_config import get_base_dir
        with open(os.path.join(get_base_dir(), "crash.log"), "w", encoding="utf-8") as f:
            traceback.print_exception(exc_type, exc, tb, file=f)
    except Exception:
        return


sys.excepthook = _crash_log


class EixWorldApp:
    def __init__(self):
        qInstallMessageHandler(_qt_message)
        try:
            scale = float(load_settings().get("ui_scale", 1.0))
        except Exception:
            scale = 1.0
        if 0.5 <= scale <= 2.0 and abs(scale - 1.0) > 0.001:
            os.environ["QT_SCALE_FACTOR"] = str(scale)
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.app.setFont(QFont("Microsoft YaHei UI", 9))
        icon_path = os.path.join(get_base_dir(), "Eix", "eixfun", "Eixfun.png")
        if os.path.isfile(icon_path):
            self.app.setWindowIcon(QIcon(icon_path))
        if welcome.needed():
            welcome.WelcomeDialog().exec()
        self.window = None
        self.splash = Splash()
        self.splash.start()
        QTimer.singleShot(60, self._boot)
        QTimer.singleShot(4000, self._force_show)

    def _boot(self):
        try:
            self.window = MainWindow()
        except Exception:
            try:
                self.splash.close()
            except Exception:
                pass
            raise
        try:
            self.window.show()
            self.window.raise_()
            self.window.activateWindow()
        except Exception:
            pass
        try:
            self.splash.finish(self.window)
        except Exception:
            try:
                self.splash.close()
            except Exception:
                pass

    def _force_show(self, *args):
        try:
            if self.window is None or self.window.isVisible():
                return
            try:
                self.splash.close()
            except Exception:
                pass
            self.window.show()
            self.window.raise_()
        except Exception:
            return

    def run(self):
        sys.exit(self.app.exec())


def _verify_env():
    try:
        import vip
        return bool(vip.guard())
    except Exception:
        return False


if __name__ == "__main__":
    if not _verify_env():
        try:
            from PyQt6.QtWidgets import QApplication, QMessageBox
            _app = QApplication(sys.argv)
            QMessageBox.critical(
                None,
                "环境校验失败",
                "程序文件不完整或已被修改，请从官方渠道重新下载。",
            )
        except Exception:
            pass
        sys.exit(1)
    EixWorldApp().run()
