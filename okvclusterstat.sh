. okvenv.sh
#okv cluster info get|jq '.value.nodes[] | "\(.nodeID),\(.nodeName) ,\(.status), \(.mode)"'|sed 's/"//g'
okv cluster info get|jq '.value.nodes[] | "\(.nodeName),\(.nodeID) ,\(.ipAddress), \(.mode),\(.status),\(.readWritePeer),\(.clusterSubgroup),\(.joinDate),\(.disableDate)"'|sed 's/"//g'
