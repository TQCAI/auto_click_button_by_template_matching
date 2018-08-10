import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MainWindow import Ui_MainWindow
from pyhooked import Hook, KeyboardEvent
from PIL import ImageGrab
import numpy as np
import pylab as plt
import cv2
import win32api
import win32con
import win32gui
from ctypes import *
import time

class POINT(Structure):
	_fields_ = [("x", c_ulong), ("y", c_ulong)]

def get_mouse_point():
	po = POINT()
	windll.user32.GetCursorPos(byref(po))
	return int(po.x), int(po.y)


def mouse_click(x=None, y=None):
	if not x is None and not y is None:
		mouse_move(x, y)
		time.sleep(0.05)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def mouse_move(x, y):
	windll.user32.SetCursorPos(x, y)

# https://www.cnblogs.com/jikeboy/p/6526274.html

global win

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        # self.showM('消息')

    def mClied(self):
        pass

    def showM(self,msg):
        self.showMessage("提示", msg, self.icon)

    def showMenu(self):
        self.menu = QMenu()
        self.quitAction = QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("res/python.ico"))
        self.icon = self.MessageIcon()
        #设置图标

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        # self.parent().exit()
        qApp.quit()
        sys.exit()

class window(QDialog,Ui_MainWindow):
    trigger = pyqtSignal(str)

    def build_connect(self):
        self.b_write.clicked.connect(self.ButtonEvent('写入'))
        self.b_erase.clicked.connect(self.ButtonEvent('擦除'))
        self.b_select.clicked.connect(self.ButtonEvent('选择'))
        self.b_undo.clicked.connect(self.ButtonEvent('撤销'))
        self.b_redo.clicked.connect(self.ButtonEvent('重做'))
        self.b_clear.clicked.connect(self.ButtonEvent('清除'))
        self.b_quit.clicked.connect(sys.exit)

    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)
        ti = TrayIcon(self)
        self.trigger.connect(ti.showM)
        ti.show()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.Popup)
        self.build_connect()

    def ButtonEvent(self,msg):
        def fun():
            self.process(msg)
        return fun

    def process(self,mode):
        if self.c_info.checkState()==Qt.Checked:
            self.trigger.emit('您点击了【'+mode+'】快捷键')
        img = np.array(ImageGrab.grab())
        img2 = img.copy()
        template = plt.imread('object_images/'+mode+'.jpg')
        w, h, _ = template.shape
        img = img2.copy()
        method = cv2.TM_CCOEFF
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        pt = (bottom_right[0] + top_left[0]) // 2, (bottom_right[1] + top_left[1]) // 2
        origin_pt = get_mouse_point()
        mouse_click(pt[0], pt[1])
        mouse_move(origin_pt[0], origin_pt[1])

    def MyKeyPressEvent(self,key):
        if key=='W':
            self.process('写入')
        if key=='E':
            self.process('擦除')
        if key=='D':
            self.process('选择')
        if key=='Z':
            self.process('撤销')
        if key=='Y':
            self.process('重做')
        if key=='Q':
            self.process('清除')
        # print(key)

class WorkThread(QThread):
    trigger = pyqtSignal(str)
    def __int__(self):
        super(WorkThread, self).__init__()
    def handle_events(self,args):
        if isinstance(args, KeyboardEvent):
            if args.current_key == 'W' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('W')
            if args.current_key == 'E' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('E')
            if args.current_key == 'D' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('D')
            if args.current_key == 'Z' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('Z')
            if args.current_key == 'Y' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('Y')
            if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.trigger.emit('Q')
    def hook_thread(self):
        hk = Hook()  # make a new instance of PyHooked
        hk.handler = self.handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
        hk.hook()  # hook into the events, and listen to the presses
    def run(self):
        self.hook_thread()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    global win
    win = window()
    workThread = WorkThread()
    workThread.trigger.connect(win.MyKeyPressEvent)
    workThread.start()
    win.show()
    sys.exit(app.exec_())
