#!/usr/bin/env python3
# coding: utf-8

import boto3
import time

#setup del 1er stack

def run_vpn_monitor_CF(stname, templURL, templCA, templParams, awsprofile):

    # setup parameters for create the stack
    template1_capabilities = templCA
    template1_parameters = templParams
    template1_capabilities.append('CAPABILITY_NAMED_IAM')
    template1_parameters.append({"ParameterKey": 'SendAnonymousData', "ParameterValue": 'No'})

    # setup aws session and creation stack
    session = boto3.Session(profile_name=awsprofile)
    resource = session.client('cloudformation')

    stackid = resource.create_stack(
        StackName = stname,
        TemplateURL = templURL,
        Parameters = template1_parameters,
        Capabilities = template1_capabilities
    )

    stack_resource = session.resource('cloudformation')

    #Chequeo de la creación del stack
    waiting = True
    while waiting:
        if stack_resource.Stack(stname).stack_status == 'CREATE_COMPLETE':
            waiting = False
            msg = "Stack created successfully."
        elif stack_resource.Stack(stname).stack_status == 'ROLLBACK_IN_PROGRESS':
            waiting = False
            msg = "Error detected, executing rollback."
        elif stack_resource.Stack(stname).stack_status == 'CREATE_FAILED':
            waiting = False
            msg = "Error detected, creation failed."
        elif stack_resource.Stack(stname).stack_status == 'ROLLBACK_COMPLETED':
            waiting = False
            msg = "Error detected, rollback completed."
        else:
            print("Waiting for stack creation...")
            time.sleep(15)

    print(msg)
    print()
    return stackid

