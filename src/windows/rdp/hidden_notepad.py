import subprocess
import win32gui
import time
import win32process

proc = subprocess.Popen(["notepad.exe"],shell=False)
# lets wait a bit to app to start
time.sleep(3)
target = proc.pid

def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
#    text = win32gui.GetWindowText(hwnd)
#    className = win32gui.GetClassName(hwnd)
    TId, PId = win32process.GetWindowThreadProcessId(hwnd)
    #print hwnd, text, className
    if PId == target:
        windowList.append(hwnd)

myWindows = []
# enumerate thru all top windows and get windows which are ours
win32gui.EnumWindows(enumWindowFunc, myWindows)

# now hide my windows, we can actually check process info from GetWindowThreadProcessId
# http://msdn.microsoft.com/en-us/library/ms633522(VS.85).aspx
for hwnd in myWindows:
    print hwnd,type(hwnd)
    win32gui.ShowWindow(hwnd, False)

# as our notepad is now hidden
# you will have to kill notepad in taskmanager to get past next line
proc.wait()
print "finished."