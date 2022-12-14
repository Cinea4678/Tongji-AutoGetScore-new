"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import sys, os
from setuptools import setup

if sys.platform == 'darwin':
    sys.argv.append("py2app")
    APP = ['Tongji-AutoGetScore.py']
    DATA_FILES = ['src']
    OPTIONS = {
        'iconfile': 'src/sources/logo.icns',
        'plist': {
            'CFBundleName': 'Tongji-ScoreAutoGet',  # 应用名
            'CFBundleDisplayName': '同济成绩自动查询器',  # 应用显示名
            "CFBundleGetInfoString": "同济大学考试成绩自动后台查询器",
            'CFBundleVersion': '1.1.0',  # 应用版本号
            'CFBundleIdentifier': 'com.cinea.tongjiautoscore',  # 应用包名、唯一标识
            'NSHumanReadableCopyright': 'Copyright © 2022 Cinea Works (Individual). Use the GPL license.',  # 可读版权
            'LSEnvironment': {'QT_QPA_PLATFORM_PLUGIN': 'minimal'}
        },
        'includes': ['sip', 'loguru', 'PyQt6.QtCore', 'PyQt6.QtWidgets', 'PyQt6.QtGui',
                     'requests', 'easyTongjiapi', 'cv2', 'PIL', 'fastgm', 'opencv-python-headless']
         , 'arch': 'universal2'
    }

    setup(
        name="Tongji-ScoreAutoGet",
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )
elif sys.platform == 'win32':
    os.system("pyinstaller -D -i src/sources/nmck_bb.ico --noconsole Tongji-AutoGetScore.py")
