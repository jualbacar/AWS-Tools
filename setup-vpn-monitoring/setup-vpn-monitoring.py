#!/usr/bin/env python3
# coding: utf-8

import boto3
import time
import run_vpn_monitor_CF
import setup_cw_alarms
import setup_sns_vpn

# Setup MAIN
AWSprofile = 'linke'
SNS_topic_name = 'LNK-VPN-MONITOR'

# 1 - setup 1st stack
stackname='LNK-VPN-MONITOR'
template1url='https://s3.amazonaws.com/solutions-reference/vpn-monitor/latest/vpn-monitor.template'
template1_capabilities = []
template1_parameters = []
# Build del 1er stack (AWS VPN monitor)
try:
    firststackid = run_vpn_monitor_CF.run_vpn_monitor_CF(stackname, template1url, template1_capabilities, template1_parameters, AWSprofile)
    print(firststackid)
    print()
    time.sleep(15)
except Exception as e:
    print("ERROR: {}".format(e))
    exit(1)
1
# 2 - Creation of SNS topic for vpn monitoring
#setup_sns_vpn.setup_sns(SNS_topic_name,AWSprofile)

# 3 - Creation of cloudwatch alerts for each VPN metrics
namespace = 'VPNStatus'
snstopic = 'arn:aws:sns:eu-west-1:916238543656:testjuanpatchmanager'
vpn_list_metrics = setup_cw_alarms.list_metrics(namespace,AWSprofile)
setup_cw_alarms.setup_alarms(vpn_list_metrics,namespace,snstopic,AWSprofile)

# print(vpn_list_metrics[0]['MetricName'])
# print(vpn_list_metrics[0]['Dimensions'][0]['Name'])
# print(vpn_list_metrics[0]['Dimensions'][0]['Value'])
# print(vpn_list_metrics[0]['Dimensions'][1]['Name'])
# print(vpn_list_metrics[0]['Dimensions'][1]['Value'])
# print(vpn_list_metrics[1]['MetricName'])
# print(vpn_list_metrics[1]['Dimensions'][0]['Name'])
# print(vpn_list_metrics[1]['Dimensions'][0]['Value'])
# print(vpn_list_metrics[1]['Dimensions'][1]['Name'])
# print(vpn_list_metrics[1]['Dimensions'][1]['Value'])
# print(vpn_list_metrics[2]['Dimensions'][0]['Value'])
# print(vpn_list_metrics[3]['Dimensions'][0]['Value'])

# print(vpn_list_metrics[0]['Dimensions'][1]['Value'])
# print(vpn_list_metrics[1]['Dimensions'][1]['Value'])
# print(vpn_list_metrics[2]['Dimensions'][1]['Value'])
# print(vpn_list_metrics[3]['Dimensions'][1]['Value'])

# print(vpn_list_metrics[0]['Dimensions'][2]['Value'])
# print(vpn_list_metrics[1]['Dimensions'][2]['Value'])
# print(vpn_list_metrics[2]['Dimensions'][2]['Value'])
# print(vpn_list_metrics[3]['Dimensions'][2]['Value'])
