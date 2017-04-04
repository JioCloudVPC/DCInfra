import json
with open('../data/hostnames.txt') as f:
    # json.dump(data, outfile)
    flag = True
    ip   = ""
    host = "" 
    my_dict={}
    for line in f:
    	if line != "\n":
			s = line.split(" ")
			if flag:
				ip = s[0]
			else:
				host = s[0]
				my_dict [ip] = host.strip("\n")
			flag = not flag			

#Open a file for writing
out_file = open("../extracted_data/ip_host.json","w")
json.dump(my_dict,out_file, sort_keys=True,indent=4)                                    

# Close the file
out_file.close()			