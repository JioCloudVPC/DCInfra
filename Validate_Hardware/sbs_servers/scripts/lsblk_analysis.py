import json

# Open the HOST-IP json file for reading

in_file = open("../extracted_data/ip_host.json","r")
ip_dict = json.load(in_file)
in_file.close()

in_file = open("../extracted_data/lshw_output.json","r")
product_dict = json.load(in_file)
in_file.close()

in_file = open("../extracted_data/free_m.json","r")
free_m = json.load(in_file)
in_file.close()

with open("../data/lsblk_details.txt") as f:
	count   		= 0
	lsblk_dict 		= {}
 	small_dict  	= {}
 	storage_dict 	= {}
 	ip = "" 
	for line in f:
		# Check Node Data processing Complete or not
		if line == "\n":
			storage_dict["sda partitions"]	= str(count)
			small_dict["storage"]			= storage_dict
			lsblk_dict[ip_dict[ip]] 		= small_dict
			small_dict 						= {}
			storage_dict					= {}
		#split line into the words
		else:
			if ">>" in line:
				ip = line.split()[0]
				#Adding other hardare and memory data into the dictionary
				small_dict["ip"]	  		= ip
				small_dict["hardware"] 		= product_dict[ip_dict[ip]]
				small_dict["memory"] 		= free_m[ip]
				count = 0
			elif "sda1" in line or "sda2" in line or "sda3" in line or "sda5"in line:
				count+=1
			elif "sd" in line:
				storage_dict[line.split()[0]] = line.split()[3]

#Open a file for writing
out_file = open("../extracted_data/host_lsblk.json","w")
json.dump(lsblk_dict,out_file, sort_keys=True,indent=4)                                    
# Close the file
out_file.close()							