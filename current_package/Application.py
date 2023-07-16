from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from current_package.DarkWindow import WinDarkWindow


class Application(WinDarkWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
