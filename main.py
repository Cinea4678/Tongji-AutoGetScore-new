"""

  入口程序

  Project Tongji-AutoGetScore
  Copyright (C) 2022 Cinea Zhan. All rights reserved.
  License: GNU General Public License v3.0

"""

import os

if __name__ == "__main__":
    """
    启动程序
    """
    currentDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(currentDir + "/src")
    if os.name == "nt":
        os.system("python main.py")
    elif os.system("python3 --version") == 0:
        os.system("python3 main.py")
    else:
        os.system("python main.py")
