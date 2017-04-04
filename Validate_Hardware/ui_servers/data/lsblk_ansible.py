# ansible commands for each ip 
import os
import time
for i in range(140,164):
	cm = "ansible 10.140.212." + str(i) + " -a lsblk >> lsblk_details.txt"
	os.system(cm)
	#time.sleep(2)	 
