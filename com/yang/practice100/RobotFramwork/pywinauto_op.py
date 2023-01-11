# -- coding: utf-8 --
# 导入pywinauto库
from pywinauto import application
# 直接启动记事本
app = application.Application().start('notepad.exe')