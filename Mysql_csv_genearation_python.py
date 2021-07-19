import sys
import os
import time
import pandas

timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)
import xlsxwriter
 
import subprocess

user="Read"
psw="\"R#@d123\""
port="3306"
ip="70.207.7.20"
script="\"select @@hostname as 'server name', mdlname, rlsno, rlsdate, insdate, type from nfr_ship.releasedetails where insdate > DATE_SUB(getdate(), INTERVAL 8 DAY);\""

cmd="mysql "+" -h "+ ip +" -u " + user+ " -p"+psw+" nfr_ship "+ " -e"+script

s1_file="D://Task//Deployment_status//replica_ws_s1//"+timestr+".txt"
s1_file_out="D://Task//Deployment_status//replica_ws_s1//release.csv"

#workbook = xlsxwriter.Workbook("D://Task//Deployment_status//replica_ws_s1//"+timestr+".xlsx")
#worksheet = workbook.add_worksheet("My sheet")
status='ONLINE'

print(cmd)
#s1_op=os.popen(cmd)

s1_op = subprocess.check_output(cmd, shell=True)
s1_op = s1_op.decode("utf-8")
print("result:"+str(s1_op))
#worksheet.write(str(s1_op))
# moving data from mysqldump output to text file
with open(s1_file,'w') as s1:
    s1.write(str(s1_op))
    #worksheet.write
s1.close()
# Convering from text to csv
account = pandas.read_csv(s1_file,
                      delimiter = "	")

# store dataframe into csv file
account.to_csv(s1_file_out,
               index = None)