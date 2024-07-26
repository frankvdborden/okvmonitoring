import json
import subprocess
import os
from datetime import datetime
homedir = os.environ['HOME']
output = ''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("scriptdir")
args = parser.parse_args()

scriptdir = args.scriptdir

homedir = os.environ['HOME']
output = ''

with open(homedir+'/'+scriptdir+'/okvNodes.json') as okv_nodes:
    profiles = json.load(okv_nodes)
    okv_nodes.close()


# set environment variables
env_vars = {'JAVA_HOME': '/usr/lib/jvm/jdk-1.8-oracle-x64/jre', 'CLASSPATH' : '/home/oracle/okvrest/lib' , 'OKV_RESTCLI_CONFIG': '/home/oracle/okvrest/conf/okvrestcli.ini', 'PATH': '/home/oracle/okvrest/bin:/usr/bin/'}

now = datetime.now()

for key,value in profiles.items():
    if key == 'nodes':
        for item in value:
            cmd = "okv server info get --profile "+ item['nodeName']
# execute a command with environment variables
            data = subprocess.run([cmd, '$JAVA_HOME $PATH'], env=env_vars, shell=True, capture_output=True, universal_newlines=True )

            
            jsonData = json.loads(data.stdout)
            output = ""
            for key,value in jsonData.items():
                if key == 'value':

                     caexpdate = datetime.strptime(value['caCertificateExpirationDate'], "%Y-%m-%d %H:%M:%S")
                     cadaysremaining = (caexpdate - now).days
                     platformcertexpdate = datetime.strptime(value['platformCertificatesExpirationDate'], "%Y-%m-%d %H:%M:%S")
                     platformdaysremaining = (platformcertexpdate - now).days
                     servercertexpdate = datetime.strptime(value['serverCertificateExpirationDate'], "%Y-%m-%d %H:%M:%S")
                     servercertdaysremaining = (servercertexpdate - now).days
                     output=output + item['nodeName'] + ","
                     output=output + str(cadaysremaining) + ","
                     output=output + str(platformdaysremaining) + ","
                     output=output + str(servercertdaysremaining)
            print(output)

#.value.backupStatus
