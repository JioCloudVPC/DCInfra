import json
import re

def create_lshw_analysis_json():
	with open("../data/lshw_details.txt") as f:
		count   = 0
		product = 0
		my_dict = {}
		host	= ""
		s_dict  = {}
		for line in f:
			if ">>" in line:
				count=0
				flag=False
			if "Gen9" in line and not flag:
				product = "Gen9"
				flag = True
			if "Gen8" in line and not flag:
				product = "Gen8"
				flag = True
				if "SL4540" in line:
					product = "SL4540"
			if count==1:
				host = line		
			if count==3 or count==5:
				s_dict [line.split(":")[0].strip(" ")] = re.sub("[\(\[].*?[\)\]]", "", line.split(":")[1].strip("\n ")).strip(" ")
			if (product=="Gen8" and count == 308) or (product=="Gen9" and count == 413) or (product=="SL4540" and count == 346):
				# print host.strip("\n")
				# print line
				s_dict [line.split(":")[0].strip(" ")] = line.split(":")[1].strip("\n ")
				my_dict[host.strip("\n")] = s_dict
				s_dict={}		
			count+=1	

	#Open a file for writing
	out_file = open("../extracted_data/lshw_output.json","w")
	json.dump(my_dict,out_file, sort_keys=True,indent=4)                                    

	# Close the file
	out_file.close()						