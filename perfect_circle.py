import pyautogui
import math
from time import sleep

Radius = 430 # if the cursor is moving out of screen try to change the radius to smaller value

curvature = 120 # Please note that the perfect circle on neal.fun may appear as a triangle. To draw a conventional circle, adjust the curvature to '6'.

(x,y) = pyautogui.size() #Return the size of screen
(X,Y) = pyautogui.position(x/2,y/2) #Set the cursor to the center of the screen

print('\n--> Place your cursor on the website while on fullscreen.\n\n(Ctrl+C to stop)\n')
print('The Process is starting in..')

try:
    for i in range(5,-1,-1):
        print(i)
        sleep(1)
except KeyboardInterrupt:
    print('Process ended')
    quit()
    
pyautogui.moveTo(X+Radius,Y)
pyautogui.mouseDown()
for i in range(Radius):
    if i%curvature==0:
       pyautogui.moveTo(X+Radius*math.cos(math.radians(i)),Y+Radius*math.sin(math.radians(i)))
    
pyautogui.mouseUp()