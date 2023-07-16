from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import qdarktheme

from ctypes import byref, c_bool, sizeof, windll
from ctypes.wintypes import BOOL, MSG
from winreg import QueryValueEx, HKEY_CURRENT_USER, OpenKey, KEY_READ
from ctypes import byref, c_bool, sizeof, windll


class WinDarkWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dwmapi = windll.LoadLibrary("dwmapi")
        self.__dwmSetWindowAttribute = dwmapi.DwmSetWindowAttribute
        self.__themes = {
            "dark": qdarktheme.load_stylesheet("dark"),
            "light": qdarktheme.load_stylesheet("light")
        }
        self.setCurrentWindowsTheme()

    def nativeEvent(self, e, message):
        if MSG.from_address(message.__int__()).message == 26:
            self.setCurrentWindowsTheme()
        return super().nativeEvent(e, message)

    def setCurrentWindowsTheme(self):
        try:
            root_key = OpenKey(
                HKEY_CURRENT_USER,
                r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                0,
                KEY_READ
            )
            lightThemeValue, _ = QueryValueEx(
                root_key,
                'AppsUseLightTheme'
            )
            if lightThemeValue == 0:
                self.setDarkTheme()
            elif lightThemeValue == 1:
                self.setLightTheme()
            else:
                raise Exception(f'Unknown value "{lightThemeValue}".')
        except FileNotFoundError:
            print('AppsUseLightTheme not found.')
        except Exception as e:
            print(e)

    def setDarkTheme(self):
        self.__setDarkTheme(True)

    def setLightTheme(self):
        self.__setDarkTheme(False)

    def __setDarkTheme(self, f: bool):
        self.__dwmSetWindowAttribute(
            int(self.winId()),
            20,
            byref(c_bool(f)),
            sizeof(BOOL)
        )
        self.setStyleSheet(
            self.__themes["dark" if f else "light"]
        )
