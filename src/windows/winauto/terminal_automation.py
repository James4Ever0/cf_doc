#you will need the win32 libraries for this snippet of code to work, Links below
import win32gui
import win32con
import win32api
import win32process
from time import sleep

import uuid

unique_id = str(uuid.uuid1())

import os

os.system("start cmd.exe /k \"title "+unique_id+"\"")
#target = proc.pid

def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
    text = win32gui.GetWindowText(hwnd)
#    className = win32gui.GetClassName(hwnd)
    #print hwnd, text, className
    if unique_id in text:
        windowList.append(hwnd)
sleep(0.1)
myWindows = []
# enumerate thru all top windows and get windows which are ours
win32gui.EnumWindows(enumWindowFunc, myWindows)
#print myWindows
assert len(myWindows)==1
hwndMain = myWindows[0]
#[hwnd] No matter what people tell you, this is the handle meaning unique ID, 
#["Notepad"] This is the application main/parent name, an easy way to check for examples is in Task Manager
#["test - Notepad"] This is the application sub/child name, an easy way to check for examples is in Task Manager clicking dropdown arrow
#hwndMain = win32gui.FindWindow("Notepad", "test - Notepad") this returns the main/parent Unique ID
#hwndMain = win32gui.FindWindow(None, "Administrator: "+unique_id)
print "main window handle", hwndMain
# check if the title is correct?
# if it is the direct window.

#["hwndMain"] this is the main/parent Unique ID used to get the sub/child Unique ID
#[win32con.GW_CHILD] I havent tested it full, but this DOES get a sub/child Unique ID, if there are multiple you'd have too loop through it, or look for other documention, or i may edit this at some point ;)
#hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD) this returns the sub/child Unique ID
#hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
hwndChild = hwndMain
#print(hwndMain) #you can use this to see main/parent Unique ID
#print(hwndChild)  #you can use this to see sub/child Unique ID

#While(True) Will always run and continue to run indefinitely
while(True):
    #[hwndChild] this is the Unique ID of the sub/child application/proccess
    #[win32con.WM_CHAR] This sets what PostMessage Expects for input theres KeyDown and KeyUp as well
    #[0x44] hex code for D
    #[0]No clue, good luck!
    #temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0) returns key sent
    temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)
# that is the letter D.
    #print(temp) prints the returned value of temp, into the console
    print temp 
    #sleep(1) this waits 1 second before looping through again
    sleep(1)