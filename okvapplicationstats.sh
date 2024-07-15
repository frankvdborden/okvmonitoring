. okvenv.sh
FROM=`date --date=' 1 minutes ago'  +"%Y-%m-%d %H:%M:%S"`
#FROM=`date +"%Y-%m-%d %H:%M:%S"`
for i in `cat /home/oracle/bin/profiles`
do
	okv metrics application get --profile $i --start-time "$FROM" --end-time NOW --include ALL --interval PT15M --statistic MEAN
done
