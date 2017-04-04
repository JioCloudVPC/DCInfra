import json
with open('../data/free_m.txt') as f:
    # json.dump(data, outfile)
    m_dict 		= {}
    small_dict	= {}
    ip 			= ""
    for line in f:
		# Check Node Data processing Complete or not
		if line == "\n":
			m_dict[ip] 		= small_dict
			small_dict 		= {}
		#split line into the words
		else:
			if ">>" in line:
				ip = line.split()[0]
			elif line.split()[0] == "Mem:":
				small_dict["total memory"] 		= line.split()[1]
				small_dict["used memory"]  		= line.split()[2]
				small_dict["free memory"] 		= line.split()[3]
				small_dict["shared"] 			= line.split()[4]
				small_dict["buffers"]			= line.split()[5]
				small_dict["cached"]			= line.split()[6]
			elif line.split()[0] == "Swap:":
				small_dict["total swap"] 		= line.split()[1]
				small_dict["used swap"]			= line.split()[2] 	
#Open a file for writing
out_file = open("../extracted_data/free_m.json","w")
json.dump(m_dict,out_file, sort_keys=False,indent=4)                                    

# Close the file
out_file.close()			