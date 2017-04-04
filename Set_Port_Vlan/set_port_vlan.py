import pexpect
import sys
import json

in_file = open("../extracted_data/switch_ip.json","r")
ip_dict = json.load(in_file)
in_file.close()

def call_switch_config(ip,port,vlan):
	print ip,port,vlan
	sys.exit()
	fout = open('./logs/switch_log_'+ip+'.log','wb')
	child = pexpect.spawn('ssh -o StrictHostKeyChecking=no admin@'+ip)
    	child.logfile = fout
    	child.expect('Password:')
    	child.sendline('K!nde1@1024')
	child.expect('All rights reserved')
	child.expect('#')
	child.sendline('configure')
	child.expect('#')
	child.sendline('interface ethernet 1/'+port)
	child.expect('#')
	child.sendline('switchport mode access')
	child.expect('#')
	child.sendline('switchport access vlan '+vlan)
	child.expect('#')
	child.sendline('no shutdown')
	child.expect('#')
	child.sendline('exit')
	child.expect('#')
        child.sendline('exit')
	child.expect('#')
        child.sendline('exit')



if __name__ == "__main__":
	rack = sys.argv[1]
	port = sys.argv[2]
	vlan = sys.argv[3]
	ip   = ip_dict[rack] 
	# print ip,rack,port,vlan
	#sys.exit()
	call_switch_config(ip,port,vlan)

