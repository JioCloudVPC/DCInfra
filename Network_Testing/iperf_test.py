import os
import json
### read current IP to new IP and other details like gateway, netmask etc...
in_file = open("client_server.json","r")
ip_dict = json.load(in_file)
in_file.close()
exec_command = ""
### Creating scripts for each node to config network setting
for i in ip_dict.iterkeys():
	exec_command = "ansible " + i + " -a " + "\"iperf3 -c " + ip_dict[i] + "\""
	os.system(exec_command)
	