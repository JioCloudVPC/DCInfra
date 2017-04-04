import os
import json
### read current IP to new IP and other details like gateway, netmask etc...
in_file = open("../extracted_data/ip_newip.json","r")
ip_dict = json.load(in_file)
in_file.close()
exec_command = ""
### Creating scripts for each node to config network setting
for i in ip_dict.iterkeys():
	text_file = open("shell_scripts/"+i, 'w')
	
	script_data="import os\nimport re\ninterface = \"\"\nf = open(\"../../etc/network/interfaces\",'r')\nnewdata = f.readlines()\nf.close()\ndata=[]\nfor line in newdata:\n\tif re.search(r'iface\s+(\w+)\s+inet\s+static',line):\n\t\tinterface = re.search(r'iface\s+(\w+)\s+inet\s+static',line).group(1)\n\tline = re.sub(r'address\s+(\d+\.\d+\.\d+.\d+)',\"address " + ip_dict[i]["ip"] + "\",line)\n\tline = re.sub(r'network\s+(\d+\.\d+\.\d+.\d+)',\"network " + ip_dict[i]["network"] + "\",line)\n\tline = re.sub(r'netmask\s+(\d+\.\d+\.\d+.\d+)',\"netmask "+ ip_dict[i]["netmask"] + "\",line)\n\tline = re.sub(r'gateway\s+(\d+\.\d+\.\d+.\d+)',\"gateway " + ip_dict[i]["gateway"] + "\",line)\n\tline = re.sub(r'broadcast\s+(\d+\.\d+\.\d+.\d+)',\"broadcast " + ip_dict[i]["broadcast"] + "\",line)\n\tdata.append(line)\nf = open(\"../../etc/network/interfaces\",'w')\nf.writelines(data)\nf.close()\nexec_command = \"sudo ifdown\" + \" \" + interface\nos.system(exec_command)\nexec_command = \"sudo sudo ip addr flush dev\" + \" \" + interface\nos.system(exec_command)\nexec_command = \"sudo ifup\"+ \" \" + interface\nos.system(exec_command)"

	text_file.write(script_data)
	text_file.close()