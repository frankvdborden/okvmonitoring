. okvenv.sh
#okv cluster info get|jq '.value.nodes[] | "\(.nodeID),\(.nodeName) ,\(.status), \(.mode)"'|sed 's/"//g'
okv server status get --profile $1
