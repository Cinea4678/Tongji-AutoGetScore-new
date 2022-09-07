"""

  真正的入口程序

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import sys
import PyQt5.QtWidgets as QtWidgets
try:
    import src.ui.main as main
except ImportError:
    import ui.main as main

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main.MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
