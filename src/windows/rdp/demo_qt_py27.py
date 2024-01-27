#coding: utf-8
import sys
from PyQt4 import QtGui, QtCore
import time
import win32ui
from threading import Thread
import random
from datetime import datetime
import cv2, numpy, win32gui, win32con
def getShot(hWnd):
    #获取后台窗口的句柄，注意后台窗口不能最小化
    # hWnd = win32gui.FindWindow("FaceRigWndClass", None)
    # hWnd=hWnd
    # nothing there. give it up. do not hide it.
    # hWnd = win32gui.FindWindow("NotePad",None) #窗口的类名可以用Visual Studio的SPY++工具获取
    #获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    #如果要截图到打印设备：
    ###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
    #result = windll.user32.PrintWindow(hWnd,saveDC.GetSafeHdc(),0)
    #print(result) #PrintWindow成功则输出1

    #保存图像
    ##方法一：windows api保存
    ###保存bitmap到文件
    # saveBitMap.SaveBitmapFile(saveDC,"img_Winapi.bmp")

    ##方法二(第一部分)：PIL保存
    # ###获取位图信息
    # bmpinfo = saveBitMap.GetInfo()
    # bmpstr = saveBitMap.GetBitmapBits(True)
    # ###生成图像
    # im_PIL = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
    ##方法二（后续转第二部分）

    ##方法三（第一部分）：opencv+numpy保存
    ###获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    ##方法三（后续转第二部分）
    # restart might be needed.
    #内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd, hWndDC)

    ##方法二（第二部分）：PIL保存
    ###PrintWindow成功,保存到文件,显示到屏幕
    # im_PIL.save("im_PIL.png") #保存
    # im_PIL.show() #显示

    ##方法三（第二部分）：opencv+numpy保存
    ###PrintWindow成功，保存到文件，显示到屏幕
    im_opencv = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    return im_opencv

def writeMe(a,im_opencv):
    cv2.imwrite(a, im_opencv, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  #保存

'''
def rejectExternal(event):
    if event.spontaneous():
        event.ignore()
        # not rejecting. wtf?
        print("spontaneous event ignored!")
    else:
        event.accept()
        print("internal event accepted!")
'''
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):               
        x, y = -99999,-99999 # hard core tricks? also vanish from the command palette!
#        x, y = 0, 0
        qbtn = QtGui.QPushButton('Quit', self)
        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.test)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        #qbtn.installEventFilter(self)

        self.setGeometry(x+0, y+0, 1024, 768)
        self.setWindowTitle('Quit button')    
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)
        self.show()
#        self.setVisible(False)
#        self.hide()
#        self.setShown(False)
#        painter = QtGui.QStylePainter()
#        painter.begin(self)
#        self.hide()
#        qbtn.show()

    def eventFilter(self,object,event):
	if event.type() in [QtCore.QEvent.MouseButtonPress,QtCore.QEvent.MouseButtonRelease,QtCore.QEvent.MouseButtonDblClick,QtCore.QEvent.MouseMove,QtCore.QEvent.KeyRelease,QtCore.QEvent.KeyPress,QtCore.QEvent.ShortcutOverride]:
	    return event.spontaneous()
        else:
            return False

    def test(self):
        print "show the position of mouse cursor in screen resolution: x is ?? , y is ??"

    def mousePressEvent(self, QMouseEvent):
        print 'press: (', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mousePressEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        print 'release: (', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mouseReleaseEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass

    def mouseMoveEvent(self, QMouseEvent):
        print 'moving!: ','(', QMouseEvent.x(), ', ', QMouseEvent.y(), ')',time.time()
        print 'isSpontaneous: ',QMouseEvent.spontaneous()
        if not QMouseEvent.spontaneous():
            print("internal event accepted!")
            super(Example,self).mouseMoveEvent(QMouseEvent)
        else:
            print("spontaneous event ignored!")
            pass
# this one is totally black, and cannot be used for fun.
# we shall consider some hide?

def shoot(widget):
    date = datetime.now()
    filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
# this is just wrong.
#    p = QtGui.QPixmap.grabWindow(application.winid(),*widget.geometry().getRect())
#    win_id = widget.windowHandle()
#    print win_id, "window handle"
#    print dir(widget.window())
    img = getShot(int(widget.winId()))
    writeMe(filename,img)
    #p = QtGui.QPixmap.grabWindow(widget.winId())
    #p.save(filename, 'jpg')
#    label.setPixmap(p)        # just for fun :)
    print "shot taken",filename

import win32gui

def shoot_thread(widget):
    time.sleep(2)
    print "shoot thread initialized!"
    # hwnd = int(widget.winId())
    # win32gui.ShowWindow(hwnd, False)
    while True:
        shoot(widget)
        time.sleep(2)

# when hidden, you cannot get the shot. what the fuck?
def some_args(window,mainWindow):
    time.sleep(2)
#    pid = window.applicationPid()
    rng = random.SystemRandom()
#    window.hide()
#    mainWindow.hide()
# yes you can hide this.
    def width(): return rng.choice(range(1024))
    def height(): return rng.choice(range(768))
    print "thread_waiting_finished!"
    while True:
        # exception found.
#        print "THIS IS THE PID OF THE MAIN APP",pid
        info = (width(),height())
        point = QtCore.QPoint(*info)
        print "Random moving destination",point
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove,point,QtCore.Qt.NoButton,QtCore.Qt.MouseButtons(),QtCore.Qt.KeyboardModifiers())
        window.sendEvent(mainWindow,event)
        time.sleep(0.3)


def main():
    # do threading here. wait till ready?
    app = QtGui.QApplication(sys.argv)
    ex = Example()
#    ex.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint)
#    ex.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint)
#    app.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#    ex.hide()
# to prove we need to take screenshots.
    app.installEventFilter(ex)
    ex.setMouseTracking(True)
    thread = Thread(target=some_args,args=(app,ex))
# this thread will be shutting down the window.
    thread.daemon = True
    thread.start()
    thread0 = Thread(target=shoot_thread,args=(ex,))
    thread0.daemon = True
    thread0.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
