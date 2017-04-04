import json
import re
with open("../data/lshw_details.txt") as f:
	count   = 0
	product = 0
	my_dict = {}
	host	= ""
	s_dict  = {}
	for line in f:
		if ">>" in line:
			count=0
		if "Gen9" in line:
			product = "Gen9"
		if "Gen8" in line:
			product = "Gen8"
			
		if count==1:
			host = line		
		if count==3 or count==5:
			s_dict [line.split(":")[0].strip(" ")] = re.sub("[\(\[].*?[\)\]]", "", line.split(":")[1].strip("\n ")).strip(" ")
		if (product=="Gen8" and count == 308) or (product=="Gen9" and count == 2290):
			s_dict [line.split(":")[0].strip(" ")] = line.split(":")[1].strip("\n ")
			my_dict[host.strip("\n")] = s_dict
			s_dict={}		
		count+=1	

#Open a file for writing
out_file = open("lshw_output.json","w")
json.dump(my_dict,out_file, sort_keys=True,indent=4)                                    

# Close the file
out_file.close()						