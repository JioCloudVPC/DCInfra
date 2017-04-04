# ansible commands for each ip 
import sys
import os
import time
def run_lsblk_ansible(lower,upper,ip):
	for i in range(int(lower),int(upper)+1):
		cm = "ansible "+ str(ip) + str(i) + " -a lsblk >> extracted_data/lsblk_details.txt"
		os.system(cm)
		#time.sleep(2)	 

if __name__ == "__main__":
	lower = sys.argv[1]
	upper = sys.argv[2]
	ip = sys.argv[3]
	run_lsblk_ansible(lower,upper,ip)
