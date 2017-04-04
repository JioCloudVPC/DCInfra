import os
import json
in_file = open("../extracted_data/ip_newip.json","r")
ip_dict = json.load(in_file)
in_file.close()




#host_dict = {"10.140.192.135":"infra1","10.140.192.137":"infra2"}
exec_command = ""

for i in ip_dict.iterkeys():
	exec_command = " scp -o \"StrictHostKeyChecking no\" shell_scripts/" + i + " " + i +":config_network.py"  
	os.system(exec_command)