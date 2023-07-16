from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

from current_package.Application import Application


def main():
    qapp = QApplication(sys.argv)
    app = Application()
    app.show()

    sys.exit(qapp.exec_())


if __name__ == "__main__":
    main()
