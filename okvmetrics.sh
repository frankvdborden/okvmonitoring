. okvenv.sh
for i in `cat /home/oracle/bin/profiles`
do
	echo "$i," `okv server info get --profile $i|jq '.value | "\(.caCertificateExpirationDate),\(.cpuCores) ,\(.diskInGB), \(.fraInGB), \(.memoryInKB), \(.platformCertificatesExpirationDate), \(.serverCertificateExpirationDate), \(.version)"'|sed 's/"//g'`
done
