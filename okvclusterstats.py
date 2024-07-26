import json
import subprocess
import os

cmd = "okv cluster info get"
# set environment variables
env_vars = {'JAVA_HOME': '/usr/lib/jvm/jdk-1.8-oracle-x64/jre', 'CLASSPATH' : '/home/oracle/okvrest/lib' , 'OKV_RESTCLI_CONFIG': '/home/oracle/okvrest/conf/okvrestcli.ini', 'PATH': '/home/oracle/okvrest/bin:/usr/bin/'}
# execute a command with environment variables
data = subprocess.run([cmd, '$JAVA_HOME $PATH'], env=env_vars, shell=True, capture_output=True, universal_newlines=True )

#print (data.stdout)

jsonData = json.loads(data.stdout)
output = ""
for key,value in jsonData.items():
    if key == 'value':
        for vkey, vvalue in value.items():
             if vkey == 'nodes':
                 for item in vvalue:
                     output=output + item['nodeName'] + ","
                     output=output + item['nodeID'] + ","
                     output=output + item['ipAddress'] + ","
                     output=output + item['mode'] + ","
                     output=output + item['status'] + ","
                     output=output + item['readWritePeer'] + ","
                     output=output + item['clusterSubgroup'] + ","
                     output=output + item['joinDate'] + ","
                     output=output + item['disableDate'] + ","
                     output=output + item['version'] 
                     output=output + "\n"
print(output)
