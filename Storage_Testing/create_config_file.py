import os
import sys
from optparse import OptionParser
from string import ascii_lowercase




# def create_config(arg_list):
##### Parse the parameters	


for i in ascii_lowercase:
	if i != "a" and i != "v" and i != "w" and i != "x" and i!="y" and i!="z":
		text_file = open("verify_fio_disk_"+i+".fio", 'w')
		script_data = "[global]\nioengine=libaio\ndirect=1\nnumjobs=1\niodepth=128\ngroup_reporting=1\nrefill_buffers\nscramble_buffers=1\nverify=crc32c-intel\nsize=1T\nbs=4k\n\n" + "[disk_"+ i + "_w]\nstonewall\nfilename=/dev/sd"+ i +"\nrw=write\ndo_verify=0\n\n" + "[disk_"+ i + "_r]\nstonewall\nruntime=120\nfilename=/dev/sd"+ i +"\nrw=read\ndo_verify=1\ncontinue_on_error=verify\n\n"
		text_file.write(script_data)
		text_file.close()


###### Main Method 
# if __name__ == "__main__":
# create_config(sys.argv[])
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",action="store_true", dest="verbose", default=True,help="don't print status messages to stdout")
(options, args) = parser.parse_args()
print options.verbose