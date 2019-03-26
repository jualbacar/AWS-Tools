#!/usr/bin/env python3
# coding: utf-8

import boto3
import json

# Discover vpnmetrics
def list_metrics(namespace,awsprofile):

    session = boto3.Session(profile_name=awsprofile)
    cloudwatch = session.client('cloudwatch')
    metrics = []

    # List metrics through the pagination interface, compose a list with all metrics
    paginator = cloudwatch.get_paginator('list_metrics')
    for response in paginator.paginate(Namespace=namespace):
        for metricname in response['Metrics']:
            # type List - metricname['Dimensions']
            metrics.append(metricname)
        return(metrics)

# Put alarms on metrics
def setup_alarms(list_of_metrics,namespace,snstopic,awsprofile):
    session = boto3.Session(profile_name=awsprofile)
    cloudwatch = session.client('cloudwatch')

    for metric in list_of_metrics:
        # HIGH Alarm
        cloudwatch.put_metric_alarm(
            AlarmName=metric['MetricName'] + ' - VPN_tunnels_state_HIGH',
            AlarmDescription='Check states from all tunnels in a VPN connection, if one fails then trigger HIGH',
            ComparisonOperator='LessThanOrEqualToThreshold',
            EvaluationPeriods=1,
            MetricName=metric['MetricName'],
            Namespace=namespace,
            Period=60,
            Statistic='Average',
            Threshold=1,
            ActionsEnabled=True,
            OKActions=[snstopic],
            AlarmActions=[snstopic],
            Dimensions=[
                {
                'Name': metric['Dimensions'][0]['Name'],
                'Value': metric['Dimensions'][0]['Value']
                },
                {
                'Name': metric['Dimensions'][1]['Name'],
                'Value': metric['Dimensions'][1]['Value']
                },
                {
                'Name': metric['Dimensions'][2]['Name'],
                'Value': metric['Dimensions'][2]['Value']
                }
            ],
            Unit='Seconds'
        )
        print("Alarm HIGH created for metric " + metric['MetricName'])
        # DISASTER Alarm
        cloudwatch.put_metric_alarm(
            AlarmName=metric['MetricName'] + ' - VPN_tunnels_state_DISASTER',
            AlarmDescription='Check states from all tunnels in a VPN connection, if onetwo fails then trigger DISASTER',
            ComparisonOperator='LessThanThreshold',
            EvaluationPeriods=1,
            MetricName=metric['MetricName'],
            Namespace=namespace,
            Period=60,
            Statistic='Average',
            Threshold=1,
            ActionsEnabled=True,
            OKActions=[snstopic],
            AlarmActions=[snstopic],
            Dimensions=[
                {
                'Name': metric['Dimensions'][0]['Name'],
                'Value': metric['Dimensions'][0]['Value']
                },
                {
                'Name': metric['Dimensions'][1]['Name'],
                'Value': metric['Dimensions'][1]['Value']
                },
                {
                'Name': metric['Dimensions'][2]['Name'],
                'Value': metric['Dimensions'][2]['Value']
                }
            ],
            Unit='Seconds'
        )
        print("Alarm DISASTER created for metric " + metric['MetricName'])
    print()
