import json
import subprocess
import os
import argparse
homedir = os.environ['HOME']
output = ''
parser = argparse.ArgumentParser()
parser.add_argument("scriptdir")
args = parser.parse_args()

scriptdir = args.scriptdir

with open(homedir+'/'+scriptdir+'/okvNodes.json') as okv_nodes:
    profiles = json.load(okv_nodes)
    okv_nodes.close()


# set environment variables
env_vars = {'JAVA_HOME': '/usr/lib/jvm/jdk-1.8-oracle-x64/jre', 'CLASSPATH' : '/home/oracle/okvrest/lib' , 'OKV_RESTCLI_CONFIG': '/home/oracle/okvrest/conf/okvrestcli.ini', 'PATH': '/home/oracle/okvrest/bin:/usr/bin/'}

for key,value in profiles.items():
    if key == 'nodes':
        for item in value:
            cmd = "okv server status get --profile "+ item['nodeName']
# execute a command with environment variables
            data = subprocess.run([cmd, '$JAVA_HOME $PATH'], env=env_vars, shell=True, capture_output=True, universal_newlines=True )


            jsonData = json.loads(data.stdout)
            output = ""
            for key,value in jsonData.items():
                if key == 'value':
                    for vkey, vvalue in value.items():
                         if vkey == 'cpu':
                             output=output + item['nodeName'] + ","
                             output=output + vvalue['usagePercentage'] + ","
                             output=output + vvalue['cpuCores'] 
            print(output)
