import wx
import time

from win32gui import GetWindowText, GetForegroundWindow

start = time.time()
for i in range(1000000):
  GetWindowText(GetForegroundWindow())
end = time.time()
print(end - start)

'''
from ctypes import wintypes, windll, create_unicode_buffer
def getForegroundWindowTitle():
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        return buf.value
    else:
        return None

start = time.time()
for i in range(1000000):
  getForegroundWindowTitle()
end = time.time()
print(end - start)
'''

