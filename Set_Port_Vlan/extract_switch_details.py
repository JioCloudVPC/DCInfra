import json
import re
from set_port_vlan import *
from openpyxl import*

in_file = open("../extracted_data/switch_ip.json","r")
ip_dict = json.load(in_file)
in_file.close()

def extract_details(start_row,end_row,rack_column,vlan_column,port_column):
	wb = load_workbook(filename = '../data/switch_details.xlsx')
	sheets = wb.get_sheet_names()
	for sheet_name in sheets:
		sheet = wb.get_sheet_by_name(sheet_name)
		for i in range(int(start_row),int(end_row)):
			rack = sheet[rack_column+str(i)].value
			vlan = sheet[vlan_column+str(i)].value
			port = sheet[port_column+str(i)].value
			port = re.search(r'E1/+(\w+)',port).group(1)
			ip  = ip_dict[rack]
			call_switch_config(ip,port,vlan)

if __name__ == "__main__":
	start_row 		= sys.argv[1]
	end_row		 	= sys.argv[2]
	rack_column 	= sys.argv[3]
	vlan_column   	= sys.argv[4] 
	port_column		= sys.argv[5]
	extract_details(start_row,end_row,rack_column,vlan_column,port_column)
