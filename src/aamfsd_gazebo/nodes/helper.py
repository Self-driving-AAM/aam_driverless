import pyautogui
print("l then r")
x=input()
a=pyautogui.position()
x=input()
d=pyautogui.position()
while(1):
	x=input()
	if(x == 'a'):
		pyautogui.click(x=a[0], y=a[1])
	elif(x == 'd'):
		pyautogui.click(x=d[0], y=d[1])
