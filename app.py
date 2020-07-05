import wx
import time

import win32gui

# win32gui.GetWindowText(win32gui.GetForegroundWindow())

def click(hWnd, x, y, *, absolute=False, doClick=True):
    if not absolute:
      left, top, right, bottom = win32gui.GetWindowRect(hWnd)
      x += left
      y += top
    '''
    lParam = win32api.MAKELONG(x, y)
    win32api.SendMessage(hWnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    '''
    win32api.SetCursorPos((x,y))
    if doClick:
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(0.05)

import win32api
import win32con

# There are many of these...
class ZPMenuClass:
  def __init__(self):
    self.hWnd = win32gui.FindWindow("ZPMenuClass", "ZPFloatControlPanelMgrWnd")
    print(self.hWnd)
    if (self.hWnd == 0):
      raise Exception("No menu found")

class ZPAnnotatePanelClass:
  def __init__(self):
    self.hWnd = win32gui.FindWindow("ZPAnnotatePanelClass", "Annotation tools")
    if (self.hWnd == 0):
      raise Exception("No annotation panel found")
    print(f"ZPAnnotatePanelClass:{self.hWnd}")
  def pressSelect(self):
    click(self.hWnd, 35, 21)
  def pressText(self):
    click(self.hWnd, 90, 21)
  def pressEraser(self):
    click(self.hWnd, 325, 21)
  def pressUndo(self):
    click(self.hWnd, 425, 21)
  def pressRedo(self):
    click(self.hWnd, 480, 21) 
  def setColor(self, color):
    # Americans...
    self.setColour(color)
  def setColour(self, colour: int):
    # ZPMenuClass()
    click(self.hWnd, 375, 21, doClick=False)
    assert(type(colour) is int and colour <= 14)
    # TODO: Colours
    baseX = 385
    baseY = 75
    click(self.hWnd, baseX + (colour % 5 * 35), baseY + (colour // 5 * 35))
  def setPen(self):
    click(self.hWnd, 145, 21, doClick=False)
    click(self.hWnd, 140, 65)
  def clearAll(self):
    click(self.hWnd, 535, 21, doClick=False)
    click(self.hWnd, 535, 65)
  def clearMine(self):
    click(self.hWnd, 535, 21, doClick=False)
    click(self.hWnd, 535, 90)
  def clearOthers(self):
    click(self.hWnd, 535, 21, doClick=False)
    click(self.hWnd, 535, 120)

def fastClick(hWnd, x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(0.00001)

import math

class ZoomAnnotationMsgWndWinXP:
  def __init__(self):
    self.hWnd = win32gui.FindWindow("ZoomAnnotationMsgWndWinXP", "Annotation Message Window")
    if (self.hWnd == 0):
      raise Exception("No annotation panel found")
    print(f"ZoomAnnotationMsgWndWinXP:{self.hWnd}")
  def draw(self):
    xBase, yBase, _, _ = win32gui.GetWindowRect(self.hWnd)
    for i in range(360):
      r = 100
      x = int(r * math.cos(math.radians(i)))
      y = int(r * math.sin(math.radians(i)))
      fastClick(self.hWnd, xBase + 500 + x, yBase + 500 + y)
    
ZPAnnotatePanel = ZPAnnotatePanelClass()
ZPAnnotatePanel.clearAll()
ZPAnnotatePanel.setPen()
ZPAnnotatePanel.setColour(10)

ZoomWhiteboard = ZoomAnnotationMsgWndWinXP()
ZoomWhiteboard.draw()

