# ansible commands for each ip 
import sys
import os
import time

cm = "ansible all -a \"hostname\" > data/hostsnames.txt"
os.system(cm)
time.sleep(1)

cm = "ansible all -a \"free -m\" > data/free_m.txt"
os.system(cm)
time.sleep(1)

cm = "ansible all -a \"lshw\" > data/lshw_details.txt"
os.system(cm)
time.sleep(1)

