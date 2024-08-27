These python scripts are using the Oracle Key Vault (OKV) "RESTFul Service Utility" that can be downloaded from the OKV appliance. They provide monitoring information from the OKV (cluster) that can be used in so called "Metric Extensions" in Oracle Enterprise Manger (OEM).

To use follow the steps below:

    1) assign a host that will be used to remotely monitor the status of the OKV cluster
    2) make sure that OEM agent is deployed to the host and the host target is visible in OEM
    3) in the $HOME directory of the monitoring user the agent runs as (typically oracle) create a directory to contain the scripts (e.g. okvmonitoring)
    4) Make sure the RESTful service utility is configured (okvrest/conf/okvrestcli.ini) correctly
    5) run 
	$ python3 okvclusternodes.py 
       this will show on stdout profiles to add to your okvrestcli.ini file and also it will create a file okvNodes.json that will be used by the other scripts to contact the nodes in the cluster.
    6) Import the metric extensions using emcli or via the UI of OEM 
	$ emcli import_metric_extension -file_name=okvbackupstatus.zip 
	$ emcli import_metric_extension -file_name=okvcerts.zip 
	$ emcli import_metric_extension -file_name=okvclusterstatus.zip 
	$ emcli import_metric_extension -file_name=okvcpu.zip 
	$ emcli import_metric_extension -file_name=okvdisk.zip 
	$ emcli import_metric_extension -file_name=okvfra.zip 
	$ emcli import_metric_extension -file_name=okvmemory.zip 
	$ emcli import_metric_extension -file_name=okvservices.zip
    7) Next make the ME deployable by running for each ME the following commands: 
	$ emcli save_metric_extension_draft -target_type=host -name='ME$okvfra' -version=4 
	$ emcli publish_metric_extension -target_type=host -name='ME$okvfra' -version=4
    8) Finally go to OEM UI and from Enterprise->Monitoring->Metric Extensions select all MEs you want to deploy and hit "Deploy to targets"
    9) After this is done check to see the result of the deployment by going to the host target in OEM and from the Host drop down go to Monitoring->All Metrics where you will find the MEs with a name starting with OKV


