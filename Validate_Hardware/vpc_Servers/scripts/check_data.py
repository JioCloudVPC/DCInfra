import json

# Open the HOST-IP json file for reading

in_file = open("../extracted_data/host_lsblk.json","r")
data_dict = json.load(in_file)
in_file.close()

for k in data_dict.iterkeys():
	flag = True
	if data_dict[k]["memory"]["total memory"] != "193330":
		print "For Host " + k + " Total Memory issue.\n"
	for i in data_dict[k]["storage"].iterkeys():
		if i == "sda": 
			if data_dict[k]["storage"][i] != "931.5G":
				flag = False
				print "For Host " + k + " sda size does not matched with standerd.\n"
		elif i == "sda partitions": 
			if data_dict[k]["storage"][i] != "3":
				flag = False
				print  "For Host " + k + " sda partitions are not equal to 3.\n"
		else :
			if data_dict[k]["storage"][i]	!=	"5.5T":
				flag = False
				print "For Host " + k + " " + i + " size not matched with standerd, actual size is: " + data_dict[k]["storage"][i] + ".\n"
	if len(data_dict[k]["storage"]) != 28:
		print "For Host " + k + "some drives are missing.\n"
	# elif flag:
	# 	print "Host " + k + " is Perfect.\n\n"		