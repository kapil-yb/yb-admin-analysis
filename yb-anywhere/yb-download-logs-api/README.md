# yb-download-logs-api

Tool to download logs using Yugabyte Anywhere API for all the nodes. 

This program can ONLY download the current logs i.e. yb-tserver.INFO and yb-master.INFO ( Not the old logs)


### Execute the script with ipython

ipython yb-download-logs.py


### We will use download_logs API for downloading logs. Details of the API can be found at following link:

https://api-docs.yugabyte.com/docs/yugabyte-platform/bb3bff7432828-download-a-node-s-logs

### Downloaded logs will be named as <IP Address>-logs.tar.gz, which contains following log files:

tserver/logs/yb-tserver.INFO
master/logs/yb-master.INFO
