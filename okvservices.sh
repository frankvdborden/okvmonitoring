. okvenv.sh
for i in `cat /home/oracle/bin/profiles`
do
	okv server status get --profile $i | jq '.value.services'
done
