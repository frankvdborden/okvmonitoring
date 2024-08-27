import json
import subprocess
import os

cmd = "okv cluster info get"
# set environment variables
env_vars = {'JAVA_HOME': '/usr/lib/jvm/jdk-1.8-oracle-x64/jre', 'CLASSPATH' : '/home/oracle/okvrest/lib' , 'OKV_RESTCLI_CONFIG': '/home/oracle/okvrest/conf/okvrestcli.ini', 'PATH': '/home/oracle/okvrest/bin:/usr/bin/'}
# execute a command with environment variables
data = subprocess.run([cmd, '$JAVA_HOME $PATH'], env=env_vars, shell=True, capture_output=True, universal_newlines=True )


jsonData = json.loads(data.stdout)
jsonOut = {}
jsonNode = {}
nodeList = []
for key,value in jsonData.items():
    if key == 'value':
        for vkey, vvalue in value.items():
             if vkey == 'nodes':
                 for item in vvalue:
                     print('['+item['nodeName']+']')
                     print('server='+item['ipAddress'])
                     jsonNode["nodeName"] = item['nodeName']
                     nodeList.append(jsonNode.copy())
                 jsonOut[vkey] = nodeList
                 with open('okvNodes.json', 'w') as f: 
                     json.dump(jsonOut, f, ensure_ascii=False)

