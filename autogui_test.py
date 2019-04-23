import pyautogui
pyautogui.FAILSAFE = True
print(pyautogui.size( ))
for i in range(1):
    pyautogui.moveTo(1000,100,duration=0.25)
    pyautogui.click(1000,100,button="left")
    pyautogui.moveTo(1000+i*20, 100, duration=1)
    pyautogui.click(1000+i * 20, 100, button="right")


#pyautogui.alert("这是一条alert",button="hjhj")
#print(pyautogui.prompt('This lets the user type in a string and press OK.'))
#pyautogui.typewrite('Hello world!')
im = pyautogui.screenshot("test_sac.png")   #输入文件名，则截屏会保存成指定的文件名
vcs=((pyautogui.locateOnScreen("vcs.PNG")))
pyautogui.click(vcs.left,vcs.top)
pyautogui.click(vcs.left,vcs.top+30*3)
im = pyautogui.screenshot("test_sac3.png")

pyautogui.click(vcs.left,vcs.top)

import subprocess

#subprocess.Popen(r"c:\windows\notepad.exe")
#x,y = pyautogui.position()
#print(x,y)
#pyautogui.click(x,y,button="left")
