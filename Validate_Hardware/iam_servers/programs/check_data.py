import json

# Open the HOST-IP json file for reading

in_file = open("../extracted_data/host_lsblk.json","r")
data_dict = json.load(in_file)
in_file.close()

for k in data_dict.iterkeys():
	if data_dict[k]["memory"]["total memory"] != "128902":
		print "For Host " + k + " Total Memory issue.\n"
	# elif flag:
	# 	print "Host " + k + " is Perfect.\n\n"		