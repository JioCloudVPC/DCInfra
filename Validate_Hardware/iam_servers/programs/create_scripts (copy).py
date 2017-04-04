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
	
	script_data="import os\ninterface = \"\"\nf = open(\"../../etc/network/interfaces\",'r')\nnewdata = f.read()\nf.close()\nf = open(\"../../etc/network/interfaces\")\nfor line in f:\n\tif \"static\" in line:\n\t\tinterface = line.split()[1].strip(\"\\n\")\n\tif \"network\" in line:\n\t\tnetwork = line.split()[1].strip(\"\\n\")\n\tif \"netmask\" in line:\n\t\tnetmask = line.split()[1].strip(\"\\n\")\n\tif \"gateway\" in line:\n\t\tgateway = line.split()[1].strip(\"\\n\")\n\tif \"broadcast\" in line:\n\t\tbroadcast = line.split()[1].strip(\"\\n\")\nf.close()\nnewdata = newdata.replace(\"" + i + "\",\"" + ip_dict[i]["ip"] + "\")\nnewdata = newdata.replace(network,\"" + ip_dict[i]["network"] + "\")\nnewdata = newdata.replace(gateway,\"" + ip_dict[i]["gateway"] + "\")\nnewdata = newdata.replace(netmask,\"" + ip_dict[i]["netmask"] + "\")\nnewdata = newdata.replace(broadcast,\"" + ip_dict[i]["broadcast"] + "\")\nf = open(\"../../etc/network/interfaces\",'w')\nf.write(newdata)\nf.close()\nexec_command = \"sudo ifdown\" + \" \" + interface\nos.system(exec_command)\nexec_command = \"sudo sudo ip addr flush dev\" + \" \" + interface\nos.system(exec_command)\nexec_command = \"sudo ifup\"+ \" \" + interface\nos.system(exec_command)"

	text_file.write(script_data)
	text_file.close()