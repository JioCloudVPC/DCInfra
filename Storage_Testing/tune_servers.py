#####################################################################
#       ***** Machine Tuning                                                                    
#       ***** Author: Yadnesh Patil Email ID: (yadnesh.patil@ril.com)   #
#       ***** Version: 1.0                                                                                              
#       ***** Date : 17/1/2017                                                                                               
#####################################################################
#####################################################################

# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import commands

#################################### Step1:  ##################################################

# exec_command = " sudo lscpu | grep '^CPU(s):'|awk '{print $2}'"
# no_of_cpu = commands.getoutput(exec_command)
# exec_command = "mkdir results_" + str(no_of_cpu) + "_cpus"
# os.system(exec_command)

# exec_command = "sudo su"
# os.system(exec_command)

disks = ['a','b','c','d','e','f','g','h','j','k','l','m']

for i in range(0,12):
        exec_command = "echo \"2\" > ../../sys/block/sd"+ disks[i] +"/queue/nomerges"
        os.system(exec_command)
        exec_command = "echo \"128\" > ../../sys/block/sd"+ disks[i] +"/queue/nr_requests"
        os.system(exec_command)
        exec_command = "echo \"0\" > ../../sys/block/sd"+ disks[i] +"/queue/read_ahead_kb"
        os.system(exec_command)
        exec_command = "echo \"0\" > ../../sys/block/sd"+ disks[i] +"/queue/rq_affinity"
        os.system(exec_command)

        exec_command = "echo deadline > ../../sys/block/sd"+ disks[i] +"/queue/scheduler"
        os.system(exec_command)
        exec_command = "echo 0 > ../../sys/block/sd"+ disks[i] +"/queue/iosched/fifo_batch"
        os.system(exec_command)
        exec_command = "echo 0 > ../../sys/block/sd"+ disks[i] +"/queue/iosched/front_merges"
        os.system(exec_command)
        exec_command = "echo 2 > ../../sys/block/sd"+ disks[i] +"/queue/iosched/read_expire"
        os.system(exec_command)        
        # sys.exit()