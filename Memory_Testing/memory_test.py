#####################################################################
#       ***** MEMORY BENCHMARKING SCRIPT                                                                #       
#       ***** Author: Yadnesh Patil Email ID: (yadnesh.patil@ril.com)   #
#       ***** Version: 1.0                                                                                              #
#       ***** Date : 13/11/2016                                                                                 #               
#####################################################################
#####################################################################
#       Note: proxy settings and Problem Size are hadcoded.                     #
#         Please change it according to your setting.                           #                               
#####################################################################


# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import commands

no_of_times = 40
array_size  = 5500000000

#################################### Step0: Install Dependencies ##################################################

# exec_command = "export http_proxy=http://10.140.192.134:10000"
# os.system("exec_command")
# exec_command = "export https_proxy=https://10.140.192.134:10000"
# os.system("exec_command")
# exec_command = "sudo -E apt-get install gcc"  
# os.system("exec_command")
# exec_command = "sudo -E wget http://www.cs.virginia.edu/stream/FTP/Code/stream.c"
# os.system(exec_command)

#################################### Step1: Setup directory ##################################################

exec_command = " sudo lscpu | grep '^CPU(s):'|awk '{print $2}'"
no_of_cpu = commands.getoutput(exec_command)
exec_command = "mkdir results_" + str(no_of_cpu) + "_cpus"
os.system(exec_command)


#################################### Step2: Stream Test ###########################################################

for i in range(0,no_of_times):
        exec_command = "gcc -fopenmp -D_OPENMP -DSTREAM_ARRAY_SIZE=" + str(array_size) + " -mcmodel=medium -O stream.c -o stream"
        os.system(exec_command)
        exec_command = "export OMP_NUM_THREADS=" + str(no_of_cpu)
        os.system(exec_command)
        exec_command = "./stream | tee results_" + str(no_of_cpu) + "_cpus/stream_result_" + str(i)
        os.system(exec_command)
