# import os
# import re
# interface = ""
# # f = open("../../etc/network/interfaces",'r')
# f = open("interfaces",'r')
# newdata = f.readlines()
# f.close()
# ip = "10.10.1.1"
# data = []
# for line in newdata:
# 	if re.search(r'iface\s+(\w+)\s+inet\s+static',line):
# 		interface = re.search(r'iface\s+(\w+)\s+inet\s+static',line).group(1)
# 	line = re.sub(r'address\s+(\d+\.\d+\.\d+.\d+)',"address " + ip,line)
# 	line = re.sub(r'network\s+(\d+\.\d+\.\d+.\d+)',"network ",line)
# 	line = re.sub(r'netmask\s+(\d+\.\d+\.\d+.\d+)',"netmask ",line)
# 	line = re.sub(r'gateway\s+(\d+\.\d+\.\d+.\d+)',"gateway ",line)
# 	line = re.sub(r'broadcast\s+(\d+\.\d+\.\d+.\d+)',"broadcast ",line)

# 	data.append(line)			

# # f = open("../../etc/network/interfaces",'w')
# f = open("interfaces",'w')
# f.writelines(data)
# f.close()
# # exec_command = "sudo ifdown" + " " + interface
# # os.system(exec_command)
# # exec_command = "sudo sudo ip addr flush dev" + " " + interface
# # os.system(exec_command)
# # exec_command = "sudo ifup"+ " " + interface
# # os.system(exec_command)

import os
import re
interface = ""
f = open("interfaces",'r')
newdata = f.readlines()
f.close()
data=[]
for line in newdata:
	if re.search(r'iface\s+(\w+)\s+inet\s+static',line):
		interface = re.search(r'iface\s+(\w+)\s+inet\s+static',line).group(1)
	line = re.sub(r'address\s+(\d+\.\d+\.\d+.\d+)',"address 10.140.210.4",line)
	line = re.sub(r'network\s+(\d+\.\d+\.\d+.\d+)',"network 10.140.210.0",line)
	line = re.sub(r'netmask\s+(\d+\.\d+\.\d+.\d+)',"netmask 255.255.254.0",line)
	line = re.sub(r'gateway\s+(\d+\.\d+\.\d+.\d+)',"gateway 10.140.210.1",line)
	line = re.sub(r'broadcast\s+(\d+\.\d+\.\d+.\d+)',"broadcast 10.140.210.255",line)
	data.append(line)
f = open("interfaces",'w')
f.writelines(data)
f.close()
# exec_command = "sudo ifdown" + " " + interface
# os.system(exec_command)
# exec_command = "sudo sudo ip addr flush dev" + " " + interface
# os.system(exec_command)
# exec_command = "sudo ifup"+ " " + interface
# os.system(exec_command)