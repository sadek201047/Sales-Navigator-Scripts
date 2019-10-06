import win32clipboard
import csv
import keyboard
import winsound
m =[]


while True:
    if keyboard.read_key() == "c":
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if data not in m:
         m.append(data)
         winsound.Beep(1000,200)
        #print(m)
        
        

    elif keyboard.read_key() == "tab":
       a=''
       for i in m:
        a = a + i +'#'
       print(a)
       m = []
       winsound.Beep(500,700)
    
