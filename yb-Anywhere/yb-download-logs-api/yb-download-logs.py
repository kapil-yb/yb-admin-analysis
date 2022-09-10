#!/usr/bin/env python
# coding: utf-8

# # Download the logs from nodes using API. 
# 
# This program can ONLY download the current logs i.e. yb-tserver.INFO and yb-master.INFO ( Not the old logs)
# 
# Execute the script with ipython
# 
# ipython yb-download-logs.py



# Modules whcih are required for to run this program
# This program is written and tested on :
# Python 2.7.18
# YB Anywhere 2.14

#import http.client (For python3)
import httplib 
import requests


#Define Variables

# YB Anywhere platform IP Address
yb_platform_addr="10.9.123.49"

# Replace Customer UUID
cUUID="3a69de7a-f74e-4124-adcd-de19484006da"

#Replace Universe UUID
uniUUID="29705a22-c0e6-40cf-a446-65d2ed8d347b"

yb_user_token=" << Replace User Token here >>"

#Define Variables for connecting to YB Database

yb_node_name=['yb-dev-univ2-n1','yb-dev-univ2-n2','yb-dev-univ2-n3']




headers = {
    'Content-Type': "application/json",
    'X-AUTH-YW-API-TOKEN': yb_user_token
    }




print ("Logs download location")
get_ipython().system(u'pwd')


# We will use download_logs API for downloading logs. Details of the API can be found at following link:
# 
# https://api-docs.yugabyte.com/docs/yugabyte-platform/bb3bff7432828-download-a-node-s-logs



for node_name in yb_node_name:
    url="http://"+yb_platform_addr+"/api/v1/customers/"+cUUID+"/universes/"+uniUUID+"/"+node_name+"/download_logs"
    res=requests.get(url, headers=headers)
    open(res.headers['Content-Disposition'].split("filename=",1)[1], "wb").write(res.content)




get_ipython().system(u'ls -l ')


