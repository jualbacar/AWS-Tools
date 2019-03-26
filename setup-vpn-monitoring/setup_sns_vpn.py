#!/usr/bin/env python3
# coding: utf-8

import boto3

def setup_sns(sns_name, awsprofile):
    session = boto3.Session(profile_name=awsprofile)
    sns = session.client('sns')
    response = sns.create_topic(Name=sns_name)

    print(response)