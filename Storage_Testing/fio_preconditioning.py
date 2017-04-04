import os
from string import ascii_lowercase

cmd="sudo ~/block-storage-master/run.sh"
for i in ascii_lowercase:
	if i != "i" and i <"n":
		cmd = cmd + " --target=/dev/sd" + i
		
cmd = cmd + " --test=iops"
		
os.system(cmd)