import sys
import os
import time
import pandas
import xlsxwriter

# Call script
#Syntax: python Mysql_csv_genearation_python_v1.py "<db hostname/ip>" "<db port_no>" "<db user_name>" "<db passwrd>" "<db name>" 
# Ex: python Mysql_csv_genearation_python_v1.py "127.0.0.1" "3306" "Read" "R#@d" "abc"
import subprocess

host_name=sys.argv[1]
port_no=sys.argv[2]
user_name=sys.argv[3]
secure=sys.argv[4]
database_name=sys.argv[5]

timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)


user=str(user_name)
psw=str(secure)
port=str(port_no)
ip=str(host_name)
db_name=str(database_name)
script="\"select * from information_schema.tables;\""

cmd="mysql "+" -h "+ ip +" -u " + user+ " -p"+psw+" "+db_name+ " -e"+script

s1_file="D://Task//Deployment_status//replica_ws_s1//"+host_name+"_"+timestr+".txt"
s1_file_out="D://Task//Deployment_status//replica_ws_s1//"+host_name+"_"+timestr+"release.csv"


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