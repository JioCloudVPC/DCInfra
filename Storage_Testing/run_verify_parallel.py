import os

if not os.path.exists("fio_verify_output"):
    os.makedirs("fio_verify_output")


from string import ascii_lowercase

### Creating scripts for each node to config network setting
cmd=""
for i in ascii_lowercase:
        # if i != "a" and i != "v" and i != "w" and i != "x" and i!="y" and i!="z":
        if i == "x" or i=="y" or i=="z":
        # if i != "a":
                cmd = cmd + "sudo fio config_files/verify_fio_disk_"+i+".fio --output=fio_verify_output/"+i+".log & "

cmd = cmd + "sudo fio config_files/verify_fio_disk_aa.fio --output=fio_verify_output/aa.log"

os.system(cmd)

