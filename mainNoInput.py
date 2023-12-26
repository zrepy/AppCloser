import psutil 
import os
import time



Proc = "Notepad.exe"


while True:
	time.sleep(0.1)
	Checkproc = Proc in (i.name() for i in psutil.process_iter()) 
	
	if Checkproc == True:
		os.system("taskkill /f /im " + Proc)
	else:
		pass
